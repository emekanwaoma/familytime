from rest_framework import serializers
from resumes.models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "file", "applicant_name", "summary", "date_created"]
        read_only_fields = ["applicant_name", "summary", "date_created"]

