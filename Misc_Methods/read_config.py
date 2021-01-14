import configparser
from Misc_Methods.get_path import GetPath


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser(interpolation=None)
        self.config.read(GetPath().get_config('data.ini'))
        self.user_config = configparser.ConfigParser(interpolation=None)
        self.user_config.read(GetPath().get_config('user_data.ini'))

    def get_url(self):
        return self.config['DEFAULT']['BASE_URL']

    def search_text(self):
        return self.config['DEFAULT']['TEXT_TO_SEARCH']

    def get_wishlist_url(self):
        return self.config['DEFAULT']['WISHLIST_URL']

    def get_user_email(self):
        return self.user_config['DEFAULT']['EMAIL']

    def get_user_email_password(self):
        return self.user_config['DEFAULT']['PASSWORD']
