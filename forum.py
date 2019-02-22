import feedparser
from datetime import datetime, timedelta
from database import Database

from webhook import Webhook

class Forum(Webhook):

   def checkForum(self, url):
      pubg_news = feedparser.parse(url)

      # check 5 last news
      n = 5

      for x in range(0, n):
         entry = pubg_news['entries'][x]['link']
         id = pubg_news['entries'][x]['id']
         post_date = pubg_news['entries'][x]['published']

         with Database() as dbconn:
            c = dbconn.cursor()
            c.execute('SELECT id FROM news WHERE id = ?', (id,))
            data = c.fetchone()

            if (data is None):
               if self.checkDate(post_date) is True:
                  self.postWebhook(entry)
                  c.execute('INSERT INTO news VALUES (?, ?)', (id, datetime.now()))
                  dbconn.commit()

   def run(self):
      self.checkForum('https://forums.pubg.com/forum/10-bug-reports-known-issues.xml/')
      self.checkForum('https://forums.pubg.com/forum/5-pc-news-patch-notes.xml/')
