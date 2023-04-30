from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27025466"))
API_HASH = getenv("API_HASH", "750ca688d4a6e58826e48d321ae4d498")

BOT_TOKEN = getenv("BOT_TOKEN", "5950392081:AAF9s8jyq_XQ7a8yPqwLoeU7bAP_V1i1qeM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

OWNER_ID = int(getenv("OWNER_ID", "5615921474"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg")

SESSION = getenv("SESSION", "BQAhIHQAk3xaBh1ymAM9KbLBbQYQ6LG-lIX_FJE9aTSvLME0_baPUUKMp-0d1-Npn51TqQb1ytKk0rTcrPFaTElc0jhwmIJLOqgyPAkNcNDPYp5zrfXQvnu6p5LMp926jbtIThDVU60prl_FX28s0i4l03kaCdhV9D5JV52yMulWCeP2JQxDDICXrtL1BTVlqw6TrPYaugRwPDYGT6M8cqWwYZc87KiUQG7WNQPQmorLe9jzQtaF4IfXwVolytWovWErARR1dpQPeHasxAlIrXZr8W3PBdVB9khvimLgB_ftqaCSUtbTINXgNjM0ddDo8EWGYeyomkDZGcINnrQUJx6q5wAaigAAAABl18tsAA")

MUST_JOIN = getenv("MUST_JOIN", "raingerproject")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/raingersupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/raingerproject")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615921474").split()))


FAILED = "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg"
