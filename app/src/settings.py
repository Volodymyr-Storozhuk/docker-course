import logging
import os

from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARNING)
load_dotenv()

try:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
except KeyError as err:
    logging.critical(f"Can`t read token from enviroment variable. Message: {err}")
    raise KeyError(err)

# for testing the settings module
if __name__ == "__main__":
    print(BOT_TOKEN)