import requests
import json
import random
import string
from time import sleep

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = "chillency's spammer"
    message = "@everyone get spammed by chillency's webhook spammer lmao. https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E https://discord.gg/BnDDnKse6E "
    avatar = "https://cdn.discordapp.com/icons/970593154371829761/e7b8da06f3ca9850c426dd3529237bee.webp?size=56".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            print("Too many requests.. - waiting before retying..")
        else:
            print("Failed to send message!")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print("S̶e̶n̶d̶i̶n̶g̶ M̶e̶s̶s̶a̶g̶e̶s̶!̶")
        return True
print ("m̶a̶d̶e̶ b̶y̶ c̶h̶i̶l̶l̶e̶n̶c̶y̶#̶0̶6̶3̶7̶")
webhook = input("W̶e̶b̶h̶o̶o̶k̶ U̶R̶L̶: ")
attempt_count = 0
sent_count = 0

print("S̶p̶a̶m̶m̶i̶n̶g̶ t̶h̶e̶ w̶e̶b̶h̶o̶o̶k̶!̶ P̶r̶e̶s̶s̶ C̶T̶R̶L̶+̶C̶ t̶o̶ s̶t̶o̶p̶!̶")
sleep(1)

failed_previous = False

try:
    while True:
        if (send_message(webhook)):
            sent_count += 1
            failed_previous = False
        else:
            if failed_previous:
                print("Waiting 30 seconds! - didn't work second time!")
                sleep(30)
            else:
                sleep(1)
            failed_previous = True
        attempt_count += 1
except KeyboardInterrupt:
    print("Stopped! Send {} messages and did {} attempts.".format(sent_count, attempt_count))
    pass
