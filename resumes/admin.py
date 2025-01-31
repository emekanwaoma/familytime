from django.contrib import admin
from resumes.models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("applicant_name", "summary", "date_created")
    search_fields = ("applicant_name", "summary")
    readonly_fields = ("summary", "applicant_name")
