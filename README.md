# discord-webhook-pubg
* It checks "News & Announcements" and "Patch Notes & Known Issues" from https://forums.playbattlegrounds.com/. If the post is not older than 3 days and not posted before it sends a webhook to your discord channel.

# requirements
* feedparser
* requests

# installation
* pip -r requirements.txt
* add your id and token to config.py
* For more information see INSTALL.md file or wiki.
# run
* crontab -e
* add (for checking news every 5 minutes):
*/5 * * * * python /path/to/discord-webhook-pubg/hook.py 

# add you to my webhook
if you want in on my runnin webhook mail me at fredrik@ffj.no
