from django.db import models

from resume_summarizer.models import BaseModel

class Resume(BaseModel):
    file = models.FileField(upload_to="resumes/")
    applicant_name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
