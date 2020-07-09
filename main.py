import pyautogui as sc
import time


class Bot:
    def __init__(self, query=0, speed=0.1):
        (self.width, self.height) = sc.size()
        self.query = query
        self.speed = speed

    def start(self):
        img = sc.screenshot(region=(self.width / 2 - self.width / 8 + 10, self.height / 2 - self.height / 4, 100, 100))
        colors = img.getcolors()
        if colors:
            for RGB in colors:
                if RGB[1] == (83, 83, 83) or RGB[1] == (169, 169, 169) or RGB[1] == (115, 115, 115):
                    if RGB[0] > 100:
                        sc.press("up")
                        # img.save("detected/" + self.query.__str__() + ".png")
                        # print(self.query, RGB[0])
        self.query += 1

    def getSpeed(self):
        return self.speed


bot = Bot()
while True:
    # time.sleep(bot.getSpeed())
    bot.start()
