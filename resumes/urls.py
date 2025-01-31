from django.urls import path

from resumes.views import ResumeDetailAPIView, ResumeListAPIView, UploadResume

urlpatterns = [
    path('upload-resume/', UploadResume.as_view()),
    path('resumes/', ResumeListAPIView.as_view()),
    path('resumes/<int:id>/', ResumeDetailAPIView.as_view()),
]