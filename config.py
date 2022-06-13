## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACLeEI69ZgSGA2GAHGFH6EkwYbAPY0IO7I-DImJLbkJBrJ-mI9LRjadfMBREafR2PrTxuu30MDIjf7rOZC_0vhfMwlvnlI8cdcqWr17GSGwfw9-MwWecwWUcU2Ou0WmPklNbrgk_GhoAPsd18Lz8O25YX56P9J-NK8WpmoBZSQ987pVfiWByYAleSCOL1orsHT5zuKywCB5DodIhpcVvIKFsIcj0-JI0JsW_-Jl7SQc8GBLXOPirlCFNcBgKu9Ynpr0CIDUjKaGV7upzphm5GNc17C6wBIj6JiNLLrZQtCs4SpK4uiiojyl5HvPUXFvFYfTryoeUeADXbJzjcM2N2m4AAAAAUsLU6gA")
BOT_TOKEN = getenv("BOT_TOKEN", "5469458401:AAGl1rj37Wafoi86wYj6C94mv5EzWWSUYqg")
BOT_NAME = getenv("BOT_NAME", "DARK")
API_ID = int(getenv("API_ID", "9722125"))
API_HASH = getenv("API_HASH", "90ecefa4067ec33cd995e0d39c95a958")
OWNER_NAME = getenv("OWNER_NAME", "Spyrx")
OWNER_USERNAME = getenv("OWNER_USERNAME", "HHSPQ")
ALIVE_NAME = getenv("ALIVE_NAME", ".")
BOT_USERNAME = getenv("BOT_USERNAME", "HHALXBOT")
OWNER_ID = getenv("OWNER_ID", "5554000808")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "HHALXBOT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "apilogin")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SPYRC")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2022024843").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
