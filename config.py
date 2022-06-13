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
BOT_NAME = getenv("BOT_NAME", "spyrx")
API_ID = int(getenv("API_ID", "9722125"))
API_HASH = getenv("API_HASH", "90ecefa4067ec33cd995e0d39c95a958")
OWNER_NAME = getenv("OWNER_NAME", "Spyrx")
OWNER_USERNAME = getenv("OWNER_USERNAME", "HHSPQ")
ALIVE_NAME = getenv("ALIVE_NAME", "Spyrx ")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5554000808").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
