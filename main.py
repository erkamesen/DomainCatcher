from app.fetch import DomainCatcher
from dotenv import load_dotenv
import os
from app.tele import Telebot
from app.utils import get_yaml, message
from app.model import Database
load_dotenv()

EXTENSIONS, CHAT_IDS = get_yaml("config.yaml")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

logger = Telebot(TELEGRAM_TOKEN, CHAT_IDS)

catcher = DomainCatcher(EXTENSIONS)
domains = catcher.run()
for domain in domains:
    domain_name = domain.get("domain")
    with Database("domains.sqlite3") as db:
        if db.get(table_name="domains", condition=f"domain = '{domain_name}'"):
            print(f"{domain_name} is already exist.")
        else:
            db.add("domains", domain)
            resp = message(*domain.values())
            logger.info(resp)
