from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve
from django.contrib.auth.decorators import login_required

from django.db.models import Q


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def search(request):
    template='blog/home.html'

    query=request.GET.get('q')

    result=Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by=2
    context={ 'posts':result }
    return render(request,template,context)
   


def getfile(request):
   return serve(request, 'File')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = 'blog/post_form.html'
#     fields = ['title', 'content', 'file']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
        

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Assuming the form has a 'file' URL passed in from the frontend
        if 'file' in self.request.POST:
            form.instance.file = self.request.POST['file']  # Set the S3 URL

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def post_delete_confirm_view(request,pk):
    post = get_object_or_404(Post,id = pk)
    return render(request,'blog/post_confirm_delete.html',{"post":post})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.user != post.author:
        raise Http404("You do not have permission to delete this post.")
    
    # Log details for debugging
    print(f"Post ID: {post.id}")
    print(f"File: {post.file}")
    print(f"File URL: {post.file.url if post.file else 'No file'}")

    # Delete the file if it exists
    if post.file:
        try:
            post.file.delete(save=False)
            print("File deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("No file associated with this post.")
    
    # Delete the post itself
    post.delete()
    print("Post deleted successfully.")
    
    return redirect('/')



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

import requests
from django.contrib.auth.decorators import login_required

@login_required
def download_file(request, pk):
    # Fetch the file object
    post = get_object_or_404(Post, pk=pk)
    file_url = post.file.url  # URL of the file on S3

    try:
        # Fetch the file content from the URL
        response = requests.get(file_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Create an HTTP response for downloading the file
        download_response = HttpResponse(
            response.content, 
            content_type="application/octet-stream"
        )
        # Set the Content-Disposition header to force download
        download_response['Content-Disposition'] = f'attachment; filename="{file_url.split("/")[-1]}"'

        return download_response

    except requests.RequestException as e:
        # Handle request errors (e.g., file not found, network error)
        return HttpResponse(f"Error downloading file: {str(e)}", status=400)
    
    