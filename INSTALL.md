# INSTALL
setup your id and token. See: https://github.com/IsekaiDevPlugins/de.isekaidev.discord.wbbBridge/wiki/How-to-get-Webhook-ID-&-Token

git clone https://github.com/stupedama/discord-webhook-pubg.git

cd discord-webhook-pubg

virtualenv --python=python3 venv

source venv/bin/activate

pip -r requirements.txt

vim hook.py and add token and id

crontab -e

where you add this line for running the script every 5 minutes:

*/5 * * * * /path/to/virtualenv/bin/python /path/to/discord-webhook-pubg/hook.py
