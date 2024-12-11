from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    post_delete_view,
    post_delete_confirm_view,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', post_delete_confirm_view, name='post-delete-confirm'),
    path('delete/<int:pk>/',post_delete_view,name='post-delete'),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='blog-about'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
