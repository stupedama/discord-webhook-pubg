import requests
import json
import database as Database
from datetime import datetime, timedelta
import config


class Webhook:

    def __init__(self, id, token, username):
        self.hookId = id
        self.token = token
        self.url = "https://discordapp.com/api/webhooks/" + self.hookId + "/" + self.token
        self.headers = {
            'user-agent': 'discord-webhook-pubg ' + config.version,
            'Content-Type': 'application/json'
        }
        self.username = username


    def database(self):
        # sqlite3 setup
        with Database() as dbconn:
            c = dbconn.cursor()

            try:
                c.execute('''CREATE TABLE news (id text, date timestamp)''')
            except sqlite3.OperationalError:
                print("sqlite table already exists")


    def postWebhook(self, message):
        w = {'embeds': message, 'username': self.username}
        r = requests.post(self.url, headers=self.headers, data=json.dumps(w))

    def checkDate(self, post_date, how_old=3):
        """
         Checks if the post are not more than x (3 is default) days old.
         """
        date = datetime.now() - timedelta(days=how_old)
        # timezones is not supported well
        post = datetime.strptime(post_date.rsplit(' ', 1)[0], "%a, %d %b %Y %H:%M:%S")
        if date < post:
            return True
        else:
            return False


    def lastPost(self, interval=2):
        """
         checks if theres already been posted since (default) 2 hours ago.
         """
        date = datetime.now() - timedelta(hours=interval)
        with Database() as dbconn:
            c = dbconn.cursor()
            c.execute('''SELECT date as "date [timestamp]" FROM news ORDER BY date DESC LIMIT 1''')

        data = c.fetchone()
        if date > data[0]:
            return True
        else:
            return False
