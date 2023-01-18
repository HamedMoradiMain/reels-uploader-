try:
    import tkinter as tk
    from PIL import ImageTk,Image
    from tkinter import messagebox 
    from modules.db import Database
    import webview as wb
    import time 
    import pathlib
    import random
    import os
    from pytube import YouTube
    import threading
    import multiprocessing
except Exception as e:
    print(e)
class Aplication(tk.Frame):
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
        self.space = tk.Label(self.master, text="  ", font=("Raleway",12), bg="black", fg="white", height=2, width=15)
        self.space.grid(row=10,column=0)
        self.instructions = tk.Label(root, text="Accounts Loaded!",  font=("Raleway",12), bg="black", fg="white", height=2, width=15)
        self.instructions.grid(columnspan=3, column=0, row=11)
    def add_accounts(self):
        print("Add Account!")
    def add_posts(self):
        print("Add Posts")
    def open_post(self):
        print("Open Post")
    def next_post(self):
        print("Next Post")
    def select_post(self):
        print("Select Post")
    def start_editing(self):
        print("Start Editing")
    def load_song(self):
        print("Load Song")
    def post(self):
        print("Post")
    
if __name__ == "__main__":
    root = tk.Tk()
    bot = Aplication(master=root)
    bot.mainloop()