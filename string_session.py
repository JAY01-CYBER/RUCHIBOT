from telethon.sessions import StringSession
from telethon.sync import TelegramClient
ruchi = input("✵ Enter y/yes to continue: ")
if ruchi == 'y' or 'yes':
 print("\nPlease go to my.telegram.org and get your API Id and API Hash to proceed\n\n 𒊹︎︎︎ɢɪᴛʜᴜʙ ʀᴇᴘᴏ ɪs ➪➪ https://github.com/jayanti01/RUCHIBOT")
print("""\n\nWelcome To RuchiBot String Session\nGenerator By @jayanti01\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit Our Telegram Group For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing RuchiBot Have A Good Time...."
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +916354471314! Kindly Retry"
        )
        print("")
        continue
    break
