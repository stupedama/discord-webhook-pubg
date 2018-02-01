import requests
import sqlite3
import re
from datetime import datetime, timedelta

from webhook import Webhook

_version = "0.2-krabbetein"

# sqlite3 setup
conn = sqlite3.connect('pubg.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
try:
   c.execute('''CREATE TABLE news (id text, date timestamp)''')
except sqlite3.OperationalError:
   print("sqlite table already exists")


class Reddit(Webhook):
   
   def checkForum(self, url, score_likes=100):
      """
      Checks pubg subreddit for 20 top posts and if they have more than (default) 100 likes,
      if theres no older post than (default) 2 hours since last post, send webhook. 
      """
      reddit = requests.get(url, headers = {'User-agent': "discord-webhook-pubg " + _version}).json()
      
      # check if theres already posted a webhook recently
      if(self.lastPost(interval=2) is True): 
         # check 20 top posts if they pass our quality check
         # 20 is maximum otherwise it will fail.
         n = 20
         for x in range(0, n):
            media = reddit['data']['children'][x]['data']['media']
            score = reddit['data']['children'][x]['data']['score']
            id = reddit['data']['children'][x]['data']['id']

            c.execute('SELECT id FROM news WHERE id = ?', (id,))
            data = c.fetchone()

            if((media is not None) and (score >= score_likes) and (data is None)):
               try:
                  ## no full video when posted on discord.
                  e = reddit['data']['children'][x]['data']['media']['reddit_video']['dash_url']
                  #entry = re.sub('DASHPlaylist.mpd$', '', e)
                  #self.postWebhook(entry)
                  #c.execute('INSERT INTO news VALUES (?, ?)', (id, datetime.now()))
                  #conn.commit()
                  pass
               except KeyError:
                  try:
                     is_video = reddit['data']['children'][x]['data']['is_video']
                     entry = reddit['data']['children'][x]['data']['url']
                     self.postWebhook(entry)
                     c.execute('INSERT INTO news VALUES (?, ?)', (id, datetime.now()))
                     conn.commit()
                  except KeyError:
                     pass
      else:
         print("less than 2 hours") 
   def run(self):
      self.checkForum('https://www.reddit.com/r/pubg.json')
      self.checkForum('https://www.reddit.com/r/PUBATTLEGROUNDS.json')
