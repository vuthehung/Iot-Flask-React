from telegram import Bot as TelegramBot, InputFile
from datetime import datetime

TELEGRAM_BOT_TOKEN = '6507947206:AAFitvK7N_-hmIBnOWtVgF1i14eqLca05yk'
TELEGRAM_CHAT_ID = '6061876850'

telegram_bot = TelegramBot(token=TELEGRAM_BOT_TOKEN)

def send_notification_with_video(video_path, datetimeDetect, name):
    try:
        caption = f"Phát hiện chuyển động của người lạ ở khu vực {name} vào thời điểm @{datetimeDetect}"

        with open(video_path, 'rb') as video_file:
            telegram_bot.send_video(chat_id=TELEGRAM_CHAT_ID, video=InputFile(video_file), caption=caption)
        print("send success")
    except Exception as ex:
        print("Error", ex)