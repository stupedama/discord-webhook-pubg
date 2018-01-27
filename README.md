# discord-webhook-pubg
a discord webhook for pubg news

# requirements
* feedparser
* requests

# installation
* pip -r requirements.txt

# run
* crontab -e
* add (for checking news every 5 minutes):
* 5 * * * * python /path/to/discord-webhook-pubg/hook.py 

