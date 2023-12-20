from app.fetch import DomainCatcher
from dotenv import load_dotenv
import os
from app.tele import Telebot
from app.utils import get_yaml
load_dotenv()

EXTENSIONS, CHAT_IDS = get_yaml("config.yaml")
TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")



logger = Telebot(TELEGRAM_TOKEN, CHAT_IDS)


# catcher = DomainCatcher(EXTENSIONS)
# tes = catcher.run()
# for t in tes:
#     logger.info(t)

logger.info("test")
