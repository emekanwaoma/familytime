from resumes.models import Resume
from resumes.services.resume_processor import ResumeProcessor


class ProcessResumeUseCase:

    def __init__(self, processor_service: ResumeProcessor=ResumeProcessor()):
        self.processor_service = processor_service

    def execute(self, resume: Resume) -> None:
        file_path = resume.file.path
        text = self.processor_service.extract_text(file_path)
        
        summary = self.processor_service.process(text)
        resume.summary = summary.get("summary")
        resume.applicant_name = summary.get("name")
        resume.save()
