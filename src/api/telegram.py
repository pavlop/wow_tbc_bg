# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

class MyTelegramClient:
    # get your api_id, api_hash, token
    # from telegram as described above
    api_id = 17479427
    api_hash = '9d2b8bd76b882fc29ba41777560f0c56'
    token = '5275580262:AAHbitHHhArVllnCSiBs_sgdDp6vFEmByXo'
    # your phone number
    phone = '+16504475170'
    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)
    username = ""


    def __init__(self, username):
        """
        Parameter username:str must start with @, example: username=@thereisnospoon
        """

        self.username = username

    def send_message(self, msg):
        msg = self.username + " " + msg
        # connecting and building the session
        self.client.connect()

        # in case of script ran first time it will
        # ask either to input token or otp sent to
        # number or sent or your telegram id
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)

            # signing in the client
            self.client.sign_in(self.phone, input('Enter the code: '))

        try:
            # receiver user_id and access_hash, use
            # my user_id and access_hash for reference
            receiver = self.client.get_input_entity("https://t.me/wowBotAlerts")

            # sending message using telegram client
            self.client.send_message(receiver, msg, parse_mode='html')
        except Exception as e:

            # there may be many error coming in while like peer
            # error, wrong access_hash, flood_error, etc
            print(e);

        # disconnecting the telegram session
        self.client.disconnect()