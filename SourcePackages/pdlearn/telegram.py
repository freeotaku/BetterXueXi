import telebot
from telebot import apihelper
from pdlearn.config import cfg_get


class TelegarmHandler:
    def __init__(self, token, secret, proxy=None):
        self.bot = telebot.TeleBot(token)
        self.master = secret
        if proxy and cfg_get("addition.telegram.use_proxy", False):
            apihelper.proxy = {'http': proxy, 'https': proxy}
            try:
                info = self.bot.get_me()  # 尝试通过代理获取西信息
                info.full_name
            except Exception as e:
                apihelper.proxy = {}
                print("代理请求异常，已关闭代理:"+str(e))

    def send_message(self, message, chat_id=None):
        if chat_id == None:
            chat_id = self.master
        try:
            self.bot.send_message(chat_id, message)
        except Exception as e:
            print(str(e))
            print(message)

    def send_qrurl(self, url, chat_id=None):
        if chat_id == None:
            chat_id = self.master
        try:
            self.bot.send_photo(chat_id, url)
        except Exception as e:
            print(str(e))
