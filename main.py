import pyautogui as sc


class Bot:
    def __init__(self):
        self.query = query
        self.speed = speed

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



bot = Bot()
while True:
    bot.start()
