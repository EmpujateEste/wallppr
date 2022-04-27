import requests
import cloudscraper
from time import sleep
from random import randint, choice
from re import findall

try:

    scraper = cloudscraper.CloudScraper()

    def dl_image(url, file_path, file_name):
        full_path = file_path + file_name + ".jpg"

        img = scraper.get(url).content

        with open(full_path, 'wb') as f:
            f.write(img)
            f.close()

    def getImage(num):

        v = choice(["space-planets", "cosmos"])

        url = f"https://wallpapercave.com/{v}-wallpapers"

        req = scraper.get(url)

        html = req.text

        measures = findall(r"<img src=\"\/wp\/wp(.*?)\.(jpg|png)\" width=\"(\d+)\" height=\"(\d+)\"", html)
        n = randint(0, len(measures) - 1)
        imgURL = f"https://wallpapercave.com/wp/wp{measures[n][0]}.jpg"

        print(v)
        print(imgURL)
        print(measures[n])
        print("-----------------------------------------")

        width = int(measures[n][2])
        height = int(measures[n][3])

        if width > height:
            if req.status_code != 200:
                print("something went wrong.")
            else:
                dl_image(imgURL, '/Users/sudo/Pictures/', f"wlpr{num}")
        else:
            print("new")
            return getImage(num)

    val = 0

    for i in range(3):

        if val < 3:
            getImage(val)
            val += 1
            sleep(15)
        else:
            val = 0
            getImage(0)
            sleep(15)
        
except (requests.ConnectionError, requests.Timeout) as exception:
 	print("No internet connection.")
