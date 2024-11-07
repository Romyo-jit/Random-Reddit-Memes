import requests
import json
import os, time
import threading

os.chdir("/sdcard/Documents/Pydroid3/My_Projects/RandomRedditMemes")
url = "https://meme-api.com/gimme/wholesomememes/"
def task():
    while True:
        a = json.loads(requests.get(url).text).get("preview")
        meme = requests.get(a[-1])
        with open("pic.jpg", 'wb') as flip:
            flip.write(meme.content)
        print("Random Meme Accepted")
        #time.sleep(5)

def server():
    os.system("python -m http.server ")
    

t2 = threading.Thread(target=task)
t1 = threading.Thread(target=server)

t2.start()
t1.start()

t1.join()
t2.join()
