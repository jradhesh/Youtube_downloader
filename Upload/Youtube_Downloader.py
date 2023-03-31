from tkinter import ttk
from tkinter import *
from pytube import YouTube
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askdirectory

root = Tk()
root.title("Youtube Downloader")
root.configure(bg="#212F3D")
root.geometry('292x250+50+50')
root.resizable(False, False)

s = ttk.Style()
s.theme_use('alt')
s.configure("yellow.Horizontal.TProgressbar", background='#E67E22')


def resource_path(relative_path):
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)


bgimg= ImageTk.PhotoImage(Image.open(resource_path("downloader2.png")))
photo= ImageTk.PhotoImage(Image.open(resource_path("q.ico")))


root.iconphoto(False, photo)


#Define the PhotoImage Constructor by passing the image file
#img= PhotoImage(file='downloader2.png', master= root)
img_label= Label(root,image=bgimg,bg="#212F3D")

#define the position of the image
img_label.place(x=15, y=15)


w = Label(root, fg="#FFFFFF",bg="#212F3D",text ='Free YouTube\nHD Videos Downloader',font=("Arial", 13)) 
w.place(x = 100,y = 35) 


E1 = Entry(root, bd =1,width=43)
#E1.insert(0, "This is the default text")
E1.place(x = 15,y = 105)


p = Label(root, fg="#FFFFFF",bg="#212F3D",text ='Paste the URL here...',font=("Arial", 8)) 
p.place(x = 90,y = 125)


def clear_all():
    E1.delete(0, END)

def save_to():
    directory = askdirectory()
    os.chdir(directory)

S = Button(root, text ="Save to", command = save_to, bg='#1F618D', fg="#FFFFFF")
S.place(x = 15,y = 145)


B = Button(root, text ="Clear", command = clear_all, bg='#F1C40F')
B.place(x = 67,y = 145)

def video_downloader():
    import time
    time.sleep(1)
    progress_bar['value'] = 10
    root.update_idletasks()
    percentagelabel['text']=progress_bar['value'],'%'
    

    url = E1.get()
    progress_bar['value'] = 20
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'



    my_video = YouTube(url)

    progress_bar['value'] = 30
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'


    progress_bar['value'] = 40
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'


    progress_bar['value'] = 50
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'


    progress_bar['value'] = 60
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'


    
    my_video = my_video.streams.get_highest_resolution()

    progress_bar['value'] = 70
    root.update_idletasks()
    time.sleep(0.50)
    percentagelabel['text']=progress_bar['value'],'%'
    
    my_video.download()

    progress_bar['value'] = 80
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'

    progress_bar['value'] = 90
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'


    time.sleep(1)
    progress_bar['value'] = 99
    root.update_idletasks()
    percentagelabel['text']=progress_bar['value'],'%'
    time.sleep(0.25)

    progress_bar['value'] = 100
    root.update_idletasks()
    time.sleep(0.25)
    percentagelabel['text']=progress_bar['value'],'%'
    time.sleep(0.25)
    percentagelabel['text']= 'Completed'
    clear_all()
    

B1 = Button(root, text ="Click here to Download", command = video_downloader, bg='#27AE60',width=23)
B1.place(x = 108,y = 145)


progress_bar = ttk.Progressbar(root, orient='horizontal', length=262, mode='determinate',style='yellow.Horizontal.TProgressbar')
progress_bar.place(x = 15,y = 180)

percentagelabel = Label(root, text='0%', bg='#212F3D',fg="#FFFFFF")
percentagelabel.place(x = 125,y = 200)

feedbacklabel = Label(root, text='Please send your feedback to: radhesh.j@luminad.com', bg='#212F3D',fg="#F7DC6F",font=("Arial", 8))
feedbacklabel.place(x = 7,y = 220)


root.mainloop()
