import requests
from environs import Env

env = Env()
env.read_env()

def telegram_bot_sendtext(bot_message):
    bot_token = env.str('TELEBOT_TOKEN')
    bot_chatID = env.str('TELEBOT_CHAT_ID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
