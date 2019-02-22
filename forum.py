import feedparser
from datetime import datetime
from database import Database
from embed import Embed
import config

from webhook import Webhook

class Forum(Webhook):

   def checkForum(self, url):
      pubg_news = feedparser.parse(url)

      # check 5 last news
      n = 5

      for x in range(0, n):
         link = pubg_news['entries'][x]['link']
         id = pubg_news['entries'][x]['id']
         title = pubg_news['entries'][x]['title']
         post_date = pubg_news['entries'][x]['published']

         image = "https://content.invisioncic.com/r273030/monthly_2017_07/PUBG_Logo_color_RGB5.png.05a3748e744a03bcc597cc88afef9533.png"


         with Database() as dbconn:
            c = dbconn.cursor()
            c.execute('SELECT id FROM news WHERE id = ?', (id,))
            data = c.fetchone()

            if (data is None):
               if self.checkDate(post_date) is True:
                  e = Embed()
                  entry = e.make_embed(link, title, image)


                  self.postWebhook(entry)
                  c.execute('INSERT INTO news VALUES (?, ?)', (id, datetime.now()))
                  dbconn.commit()


   def run(self):
      if config.enable_bug_reports is True:
         self.checkForum('https://forums.pubg.com/forum/10-bug-reports-known-issues.xml/')

      if config.enable_news is True:
         self.checkForum('https://forums.pubg.com/forum/5-pc-news-patch-notes.xml/')
