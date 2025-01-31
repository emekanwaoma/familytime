from abc import ABC, abstractmethod
from django.conf import settings
from openai import OpenAI

class BaseLLMService(ABC):
    @abstractmethod
    def summarize(self, text: str) -> dict:
        pass


class GPTClient(BaseLLMService):
    api_key = settings.OPENAI_API_KEY

    def summarize(self, text: str) -> dict:
        client = OpenAI(api_key=self.api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Extract name and summarize:\n{text}"},
            ],
        )

        output = response.choices[0].message.content

        name, summary = output.split("\n", 1) if "\n" in output else ("Unknown", output)
        return {"name": name.strip(), "summary": summary.strip()}


class AISummarizerFactory:

    @staticmethod
    def get_summarizer():
        provider = settings.AI_PROVIDER
        match provider:
            case "openai":
                return GPTClient()
            case _:
                raise ValueError("Invalid AI provider selected")
