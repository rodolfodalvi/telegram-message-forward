from telethon import TelegramClient, events, sync
from telethon.tl.types import UpdateShortMessage

api_id = 1848166
api_hash = '169a2dda0b24775a09bafd56069f815b'

global client
client = TelegramClient('forwardMessage', api_id, api_hash)
client.start()
print("Detalhes da conta:\n")
print(client.get_me().stringify())

global group_receiver
group_receiver = 467381774
global group_sender
group_sender = 467381774

client.connect() 

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    user = sender.username
    print(chat.id)
    print(event.raw_text)
    print(event)
    print(chat)
    if chat.id==group_receiver:
        message = event.raw_text
        await client.send_message(group_sender,message)
       
   
while (1==1):
    x = 1
    client.connect() 
        
