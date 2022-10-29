import requests
from bs4 import BeautifulSoup


class Parser:
    BASE_URL = 'https://t.me/s/'

    def get_url(self, channel):
        cls = self.__class__
        return cls.BASE_URL + channel

    def get_page(self, channel):
        r = requests.get(self.get_url(channel))
        return r

    def parse(self, cnannel):
        # s
        pass

if __name__ == '__main__':
    parser = Parser()
    # print(parser.get_page('english_easily/latest').text)
    print(parser.parse('english_easily/latest'))

