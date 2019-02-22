import sqlite3
from forum import Forum
from database import Database
import config


def check_database():
   with Database() as dbconn:
      c = dbconn.cursor()
      try:
         c.execute('''CREATE TABLE news (id text, date timestamp)''')
      except sqlite3.OperationalError:
         print("sqlite table already exists")

def main():
   # pubg forum
   f = Forum(config.id, config.token, config.bot_name)
   f.run()


if __name__ == '__main__':
   check_database()

   if(config.id and config.token):
      main()
   else:
      print("Please add your token and id to file config.py")