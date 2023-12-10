from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from datetime import datetime
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
import time
import datetime
import time
import requests
api_id = 16748685
api_hash = 'f0c8f7e4a7a50b5c64fd5243a256fd2f'
with TelegramClient(StringSession('1BJWap1wBu2E1jhX4RILc2DWBY1QHSTp69CzsYRjOttaJGvC8xdtuqSSAXceHEBV9sZ00tHMi7uAIZuP9xasQPtXg2cyqiG16RuYdv141oeP6oJlv6BdpSUSLugOQ9VJTULYesE5hZyk0FRMYm1z3t4np2-mPegAiVzxJiVnOPa46lWynxBRYNJ_HjSocr0nPS4-cj4HN4KeG2HZXE9QhmcbKLJOBoTB9XrjVUblYBgx0sfCfVvI3kVfskRVP8Z9uAZx7F1vOI6AlWAtmUXSkmVSB9ccQDIpVw22TFkn_t6VMXKL_Z0HOSrqaoLJeFMAnr7UavaRIvn4PhU4X4gEHSswEvwoYvB0='), api_id, api_hash) as client:
    print(client.session.save())
@client.on(events.NewMessage)
async def upd_name(event):
    while True:
        iraq_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
        hours = divmod(iraq_time.hour, 12)[1]
        name = f"\r{hours}:{iraq_time.strftime('%M:%S')}"
        time.sleep(1)
        await client(UpdateProfileRequest(first_name=name))
client.start()
client.run_until_disconnected()
