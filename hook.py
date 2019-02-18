import sqlite3
from forum import Forum
from reddit import Reddit

_version = "0.2-krabbetein"

# webhook setup
username = 'PUBG webhook'
id = ''
token = ''

# sqlite3 setup
conn = sqlite3.connect('pubg.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
try:
   c.execute('''CREATE TABLE news (id text, date timestamp)''')
except sqlite3.OperationalError:
   print("sqlite table already exists")


# run
def main():
   # pubg forum
   f = Forum(id, token, username)
   f.run()

   ## currently a little buggy.
   # pubg reddit
   #r = Reddit(id, token, username)
   #r.run()

   #sqlite3
   conn.close()


if __name__ == '__main__':
   if(token and id):
      main()
   else:
      print("Please add tokenid and/or id to hook.py")
