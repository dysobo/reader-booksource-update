import requests
import json

class ReaderClient:
    def __init__(self, username, password, reader_url):
        self.username = username
        self.password = password
        self.reader_url = reader_url
        self.session = requests.Session()

    def login(self):
        url = f"{self.reader_url}/login"
        data = {"username": self.username, "password": self.password, "isLogin": True}
        headers = {"Content-Type": "application/json"}
        response = self.session.post(url, data=json.dumps(data), headers=headers)
        print(json.dumps(response.json(), sort_keys=True, indent=4))

    def get_book_sources(self, source_url):
        response = requests.get(source_url)
        return response.json()

    def send_book_sources(self, source_url):
        data = self.get_book_sources(source_url)
        url = f"{self.reader_url}/saveBookSources/"
        headers = {"Content-Type": "application/json"}
        response = self.session.post(url=url, headers=headers, json=data)
        print(response.json())

# 多个账号和书源地址
accounts = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
]

book_source_urls = [
    "https://www.gitlink.org.cn/api/yi-c/yd/raw/sy.json?ref=master",
    "https://www.another-source.com/books.json"
]

reader_url = "http://192.168.0.39:7777/reader3"  # reader地址，自己改

for account in accounts:
    for source_url in book_source_urls:
        client = ReaderClient(account["username"], account["password"], reader_url)
        client.login()
        client.send_book_sources(source_url)
