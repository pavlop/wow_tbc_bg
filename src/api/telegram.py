# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import requests

class MyTelegramClient:
    # get your api_id, api_hash, token
    # from telegram as described above
    api_id = 17479427
    token = '5275580262:AAHbitHHhArVllnCSiBs_sgdDp6vFEmByXo'
    # creating a telegram session and assigning
    # it to a variable client
    bot_chat_id = "-1001759146091"

    def __init__(self, username):
        """
        Parameter username:str must start with @, example: username=@thereisnospoon
        """

        self.username = username

    def send_message(self, msg):
        msg = self.username + " " + msg
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.bot_chat_id + '&parse_mode=Markdown&text=' + msg
        response = requests.post(send_text)
        print(response.text)