import pdfplumber
from .ai_providers import AISummarizerFactory, BaseLLMService

class ResumeProcessor:
    def __init__(self, ai_service: BaseLLMService = AISummarizerFactory.get_summarizer()):
        self.ai_service = ai_service

    def extract_text(self, file_path: str) -> str:
        with pdfplumber.open(file_path) as pdf:
            return " ".join([page.extract_text() or "" for page in pdf.pages])

    def process(self, text: str) -> dict:
        return self.ai_service.summarize(text)