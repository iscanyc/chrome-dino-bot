import pyautogui as sc


class Bot:
    def __init__(self, query=0, speed=0.1):
        (self.width, self.height) = sc.size()
        self.query = query
        self.speed = speed
        self.old = 1

    def start(self):
        img = sc.screenshot(region=(209, 371, 100, 100))
        colors = img.getcolors()
        if colors:
            for RGB in colors:
                if RGB[1] == (83, 83, 83):
                    if RGB[0] > 100:
                        sc.press("up")
                        print("Hit")
                        # img.save("detected/" + self.query.__str__() + ".png")
        self.query += 1

    def getSpeed(self):
        return self.speed


bot = Bot()
while True:
    # time.sleep(bot.getSpeed())
    bot.start()
