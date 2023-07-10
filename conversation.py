import openai


GPT4 = "GPT4"
GPT35 = "GPT35"
MODELS = {
    GPT4: "gpt-4",
    GPT35: "gpt-3.5-turbo-0613"
}

class Conversation:

    def __init__(self, model_name: str = GPT4, message_limit: int = 20) -> None:
        self.model = MODELS[model_name]
        self.message_limit = message_limit
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful, polite, middle-aged English assistant. Answer "
                    "the user prompt with a bit of humor."
                )
            }
        ]

    def answer(self, prompt: str) -> str:
        self._update("user", prompt)

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=0
        )

        content = response.choices[0].message.content
        self._update("assistant", content)
        return content

    def _update(self, role: str, content: str) -> None:
        self.messages.append({
            "role": role,
            "content": content
        })

        if len(self.messages) > self.message_limit:
            self.messages.pop(0)
