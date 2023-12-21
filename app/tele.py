from enum import Enum
import requests


class Condition(Enum):

    INFO = "✅"


class Telebot:

    def __init__(self, token, chat_ids):
        self._token = token
        self._chat_ids = chat_ids
        self._url = f"https://api.telegram.org/bot{token}/"

    def log(self, message, chat_id, condition=None):
        text = message
        if condition is not None:
            text = f"{condition.value} {text}"

        url = self._url + "sendMessage"
        resp = requests.post(
            url=url,
            params={
                "chat_id": chat_id,
                "text": text
            }
        )
        resp.raise_for_status()

    def info(self, message):
        for chat_id in self._chat_ids:
            self.log(message, chat_id, Condition.INFO)
