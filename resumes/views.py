from django.shortcuts import get_object_or_404
from resumes.serializers import ResumeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from resumes.models import Resume
from django.core.files.storage import default_storage

from resumes.usecases.summarize_resumes import ProcessResumeUseCase

class UploadResume(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".pdf"):
            return Response({"error": "Invalid file format."}, status=status.HTTP_400_BAD_REQUEST)

        default_storage.save(file.name, file)
        summary_service = ProcessResumeUseCase()
        resume = Resume.objects.create(file=file)
        summary_service.execute(resume)

        response = { "message": "Resume uploaded successfully"}

        return Response(response, status=status.HTTP_201_CREATED)

class ResumeListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        resumes = Resume.objects.all()
        return Response(ResumeSerializer(resumes, many=True).data)
    
class ResumeDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id: int):
        resume = get_object_or_404(Resume, id=id)
   
        return Response(ResumeSerializer(resume).data)
