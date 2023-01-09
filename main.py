from instagrapi import Client
class InstaBot:
    USER = ""
    PASS = ""
    cl = Client()
    cl.login(USER,PASS)
    PATH = input("put your video path:>").strip()
    CAPTION = input("put your video caption").strip()
    def main(self):
        self.cl.clip_upload(self.PATH,self.CAPTION)
    def run(self):
        self.main()
if __name__ == "__main__":
    bot = InstaBot()
    bot.run() 