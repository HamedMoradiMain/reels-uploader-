try:
    import tkinter as tk
    from PIL import ImageTk,Image
    from tkinter import messagebox 
    import webview as wb
    import time 
    import pathlib
    import random
    import os
    from pytube import YouTube
    import threading
    import multiprocessing
    from tkinter.filedialog import askopenfile
    import re
    import os # os module 
    import sys # sys module
    from bs4 import BeautifulSoup
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import time # time module 
    import re
    import json
    import random
    import requests # request img from web
    from pathlib import Path
    import instascrape
except Exception as e:
    print(e)
class Aplication(tk.Frame):
    BASE_DIR = Path(".").resolve()
    print(BASE_DIR)
    accounts = []
    posts = []
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        master.configure(background="black")
        master.title("Social Media Bot")
        master.geometry("290x550")
        master.resizable(0, 0)
        self.create_widgets()
    def create_widgets(self):
        # Social Media Bot Label 
        self.social = tk.Label(self.master, text="Social Media Bot", font=("Bold",12), bg="black", fg="white", height=2, width=15)
        self.social.grid(columnspan=3, column=0, row=0)#,sticky=tk.W)
        self.aat = tk.StringVar()
        self.acb = tk.Button(self.master, textvariable=self.aat, command=lambda:self.add_accounts(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.aat.set("Load Accounts")
        self.acb.grid(row=1, column=0,sticky=tk.W)
        # Posts Button
        self.apt = tk.StringVar()
        self.apt.set("Load Posts")
        self.apb = tk.Button(self.master, textvariable=self.apt, command=lambda:self.add_posts(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.apb.grid(row=1, column=1,sticky=tk.W)
        # Open Post, Next Post and Select Post Buttons
        self.opt = tk.StringVar()
        self.opt.set("Open Post")
        self.apb = tk.Button(self.master, textvariable=self.opt, command=lambda:self.open_post(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.apb.grid(row=2, column=0,sticky=tk.W)
        self.spt = tk.StringVar()
        self.spt.set("Select Post")
        self.apb = tk.Button(self.master, textvariable=self.spt, command=lambda:self.select_post(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.apb.grid(row=2, column=1)
        # Load Audio Entry and Button 
        self.lat = tk.StringVar()
        self.lat.set("Load Audio")
        self.lab =tk.Button(self.master, textvariable=self.lat, command=lambda:self.load_song(), font="Raleway", bg="#20bebe", fg="white", height=2, width=31)
        self.lab.grid(row=3,column=0,columnspan=3,sticky=tk.W)
        # where to start 
        self.stt = tk.StringVar()
        self.seb = tk.Button(self.master, textvariable=self.stt, command=lambda:self.start_editing(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.stt.set("Start Editing")
        self.seb.grid(row=4, column=1)
        self.wts = tk.StringVar()
        self.s_e = tk.Entry(self.master,textvariable=self.wts,bg="#20bebe", fg="white", font=("Raleway",30),width=6)
        self.s_e.grid(row=4,column=0)
        # Load Spotify Details, Entry and Button 
        self.st = tk.StringVar()
        self.fsbt = tk.StringVar()
        self.s_e = tk.Entry(self.master,textvariable=self.st,bg="#20bebe", fg="white", font=("Raleway",30),width=6)
        self.s_e.grid(row=5,column=0)
        self.lsd = tk.Button(self.master, textvariable=self.fsbt, command=lambda:self.load_song(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.fsbt.set("Load Song Details")
        self.lsd.grid(row=5, column=1)
        # Open Results Post Buttons 
        # YouTube, TikTok and Instagram Radio Buttons
        self.insta_var = tk.IntVar()
        self.you_var = tk.IntVar()
        self.tik_var = tk.IntVar()
        self.ofv = tk.Button(self.master, text="Open Final Video", command=lambda:self.load_song(), font="Raleway", bg="#20bebe", fg="white", height=2, width=31)
        self.ofv.grid(row=6,column=0,columnspan=4,sticky=tk.W)
        self.pb = tk.Button(self.master, text="Post", command=lambda:self.post(), font="Raleway", bg="#20bebe", fg="white", height=2, width=31)
        self.pb.grid(row=7,column=0,columnspan=2,sticky=tk.W)
        # working logs 
        self.itv = tk.StringVar()
        self.space = tk.Label(self.master, text="  ", font=("Raleway",12), bg="black", fg="white", height=2, width=15)
        self.space.grid(row=10,column=0)
        self.instructions = tk.Label(root, textvariable=self.itv,  font=("Raleway",10), bg="black", fg="white", height=2, width=30)
        self.itv.set("Ready to use!")
        self.instructions.grid(columnspan=3, column=0, row=11)
    def add_accounts(self):
        self.itv.set("Loading... ")
        self.aat.set("loading...")
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("Text file", "*.txt")])
        if file:
           for item in file:
                if item not in self.accounts:
                    self.accounts.append(item)
                    print(item)
        self.itv.set("Accounts Loaded Sucessfully!")
        self.aat.set("Load Accounts")
    def add_posts(self):
        self.itv.set("Ready to use!")
        self.itv.set("Loading... ")
        self.apt.set("loading...")
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("Text file", "*.txt")])
        if file:
           for item in file:
                item = re.sub("\s{1,1000}","",item)
                if item not in self.posts:
                    self.posts.append(item)
                    print(item)
        self.apt.set("Load Posts")
        self.itv.set("Posts Loaded Sucessfully!")
    def open_post(self):
        self.opt.set("Next Post")
        self.itv.set("Liked the post?")
        self.post = random.choice(self.posts)
        print(self.post)
        def call_back():
            with open(f"{self.BASE_DIR}/resources/user_agent.txt","r") as f:
                user_agents = [agent for agent in f.readlines()]
                f.close()
            options = Options()
            options.add_argument(f'user-agent={random.choice(user_agents)}')
            driver = webdriver.Chrome(executable_path=f"{self.BASE_DIR}/resources/chromedriver.exe",options=options)
            driver.set_window_size(500,700)
            driver.get(self.post)
            time.sleep(25)
            driver.close()
        p = threading.Thread(target=call_back)
        p.start()
    def select_post(self):
        self.opt.set("Open Post")
        self.itv.set("Post Has Been Selected!")
        save_path = f"{self.BASE_DIR}/resources/raw_video/"
        def call_back():
            if "youtube" in self.post:
                try:
                    self.itv.set("Downloading the Short from YouTube")
                    os.system(f"yt-dlp --ffmpeg-location {self.BASE_DIR}/resources/ --path {save_path} -x --format mp4 {self.post}")
                except Exception as e:
                    print(e)
                else:
                    self.itv.set("Download Successful!")
            if "tiktok" in self.post:
                self.itv.set("Downloading the Video from TikTok")
                def downloadVide(link,id):
                    cookies = {

                    }
                    headers = {

                    }
                    params = {
                        'url':'dl',
                    }
                    data = {
                        'id': link,
                        'locale': 'en',
                        'tt': 'NDZuMTU2',
                    }
                    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
                    downloadSoup = BeautifulSoup(response.text, "html.parser")
                    downloadLink = downloadSoup.a["href"]
                    mp4File = urlopen(downloadLink)
                    # Feel free to change the download directory
                    with open(f"{self.BASE_DIR}/resources/raw_video/{id}.mp4", "wb") as output:
                        while True:
                            data = mp4File.read(4096)
                            if data:
                                output.write(data)
                            else:
                                break
                    with open(f"{self.BASE_DIR}/resources/user_agent.txt","r") as f:
                        user_agents = [agent for agent in f.readlines()]
                        f.close()
                    options = Options()
                    options.add_argument(f'user-agent={random.choice(user_agents)}')
                    driver = webdriver.Chrome(executable_path=f"{self.BASE_DIR}/resources/chromedriver.exe",options=options)
                    driver.get(self.post)
                    time.sleep(1)
                    scroll_pause_time = 1
                    screen_height = driver.execute_script("return window.screen.height;")
                    i = 1
                    while True:
                        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
                        i += 1
                        time.sleep(scroll_pause_time)
                        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
                        if (screen_height) * i > scroll_height:
                            break
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    # this class may change, so make sure to inspect the page and find the correct class
                    videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
                    print(len(videos))
                    for index, video in enumerate(videos):
                        downloadVideo(video.a["href"], index)
                        time.sleep(10)
            if "instagram" in self.post:
                self.itv.set("Downloading the Reel from Instagram")
                session_id = r"7250764387%3Atg8kJqBKbymLpU%3A3%3AAYe2hg0WpfUhI5uDTRchjdyUnZ1hhcgf5AvJUIXSHw"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
                    "cookie":f'sessionid={session_id};'}
                google_reel=instascrape.Reel(self.post)
                google_reel.scrape(headers=headers)
                google_reel.download(fp=f"{save_path}reel.mp4")
                self.itv.set("Download Successful!")
        t = threading.Thread(target=call_back)
        t.start()
    def load_song(self):
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("Audio file", "*.mp3")])
    def start_editing(self):
            print("Start Editing")
    def post(self):
        print("Post")
    def reset(self):
        pass
if __name__ == "__main__":
    root = tk.Tk()
    bot = Aplication(master=root)
    bot.mainloop()