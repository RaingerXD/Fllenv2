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

SESSION = getenv("SESSION", "BQAhIHQAre_ajeznaafgzJPNJcTWfT4Zu9YlrpYtjHv16nmzNai6FWAGOF-UtNcCJ8vLXGB4AWPQySpCZqJMob7zijj_Vr17MjGKCt5yzmY1ElGsHRwSkQiLTETp70pqFJLxxHFMgFRkGMU5Fh05LmkXiolGmeOj0YUnsu2Ah2LYMjxXzuGa_sNamf4lix9iR72oluCUYFt99h1D63WsJIySPR_9GKhORRFKsrCh7f4UkEq-5kV8YVDAv79OpHZdfF39a9oWHyi_WQstNZuneocrEqfQKZFz30NX4T_GiNkbh6LtG6fLsRhZPIYTg_Ad8WT9SEG14VW_UM8NJ879xMxTXX2DhwAAAABl18tsAA")

MUST_JOIN = getenv("MUST_JOIN", "raingerproject")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/raingersupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/raingerproject")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5615921474").split()))


FAILED = "https://telegra.ph/file/2e2a2cd8c9db45ae73de6.jpg"
