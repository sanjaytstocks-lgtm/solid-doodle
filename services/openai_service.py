from openai import OpenAI

from config.settings import settings


class AIService:

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def ask(self, prompt: str):

        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )

        return response.output_text