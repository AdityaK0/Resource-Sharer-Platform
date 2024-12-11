# Resource Center

A web-based platform built using the Django framework that allows users to upload, manage, and download various resources.
The platform is designed to facilitate resource sharing among users with a focus on simplicity, efficiency, and scalability. 
Authentication is integrated for secure access and personalized user experiences.

---

## Features

### User Management
- **User Authentication:**
  - Secure login and registration system.
  - Password reset functionality.
  - Integration with Django’s built-in `auth` system for robust authentication.

- **User Profiles:**
  - Users can upload profile pictures.
  - Editable profiles for managing user information.

### Resource Management
- **Upload Resources:**
  - Users can upload various types of files, including images, videos, and documents.
  - Supported file types: `.jpg`, `.jpeg`, `.png`, `.mp4`, `.pdf`, etc.

- **Download Resources:**
  - Users can download files uploaded by others.
  - A notification system informs users when a download starts.

- **Preview Resources:**
  - Image previews for supported formats.
  - Video playback directly on the platform.

### Dynamic Content Handling
- **File Metadata:**
  - Automatically extract and display file details such as name, size, and type.

- **Content Filtering:**
  - Filter resources by uploader, type, or keywords.

### Responsive Design
- **Frontend Design:**
  - Clean and responsive UI built with HTML, CSS, and Bootstrap.
  - Optimized for both desktop and mobile devices.

### Deployment and Infrastructure
- **Backend:**
  - Django framework powers the backend logic.
  - PostgreSQL hosted on [Neon](https://neon.tech/) for reliable database management.

- **Frontend Hosting:**
  - Serverless deployment on [Vercel](https://vercel.com/) for scalability and performance.

- **File Storage:**
  - Resource files are securely stored on **AWS S3 buckets**.



---

## Installation

### Prerequisites
1. Python 3.10+
2. PostgreSQL
3. AWS S3 bucket credentials
4. Vercel CLI (optional for deployment)
5. Django (5+)

### Modules
crispy-bootstrap4
Django
django-allauth
django-crispy-forms
django-bootstrap4
gunicorn
pillow
psycopg
psycopg2-binary
tzdata
django-storages
boto3
python-dotenv
requests

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https:https://github.com/AdityaKO2/Resource-Sharer-Platform.git
   cd django_web_app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the `DATABASES` configuration in `settings.py` with your Neon credentials.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. Configure AWS S3:
   - Add your AWS credentials and bucket name to the environment variables.
   - Update `settings.py` for S3 integration.

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Deployment

### Backend
1. Deploy the backend to Vercel:
   - Install Vercel CLI:
     ```bash
     npm install -g vercel
     ```
   - Initialize Vercel:
     ```bash
     vercel
     ```

2. Configure environment variables on Vercel:
   - Add `DATABASE_URL` for Neon.
   - Add AWS credentials.

### Frontend
- The frontend is integrated into the Django templates and hosted on Vercel for serverless deployment.

---

## Technologies Used

### Backend
- **Django Framework:** Robust backend development.
- **PostgreSQL:** Database management, hosted on Neon.
- **AWS S3:** Scalable file storage.

### Frontend
- **HTML/CSS/Bootstrap:** Responsive and clean UI.
- **JavaScript:** Interactive and dynamic features.

### Hosting & Deployment
- **Vercel:** Serverless hosting for the Django project.
- **Neon:** Cloud-hosted PostgreSQL database.

---

## Future Enhancements
1. **Search Functionality:**
   - Advanced search and filtering options.

2. **Commenting and Rating:**
   - Enable users to comment on and rate uploaded resources.

3. **API Support:**
   - Expose REST APIs for third-party integration.

4. **Enhanced Analytics:**
   - Dashboard for viewing upload/download statistics.

---


---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

---

## Contact
For any queries or suggestions, please reach out to:
- **Email:** aditya123905@gmail.com
- **GitHub:** AdityaKO2

