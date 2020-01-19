# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:27:33 2019

@author: Flora
flora.danan@ens.fr
"""

# importing libraries 

import tkinter as tk
from xlwt import Workbook 
import glob
from os import startfile
import sys, os
from pathlib import Path
import tkinter.tix as tktix

#Define objects
class video(object) :
    
    def __init__ (self,name='') :
        self.nom=name
    
    def jouer_video(self):
        
        startfile(self.nom)
            
        
class image(object) :
    
    def __init__ (self,name='') :
        self.nom=name
        
    def montrer_image(self) :
        
        startfile(self.nom)

#Define outputs (responses)   
def sortie() :
    global note_image, note_video, valence_video, images, videos, path
    
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    
    for i in range(len(note_image)) :
    
        sheet1.write(i,0,note_image[i].get())
        sheet1.write(i,1,os.path.basename(images[i]))
        
    for i in range(len(note_video)) :
        
        sheet1.write(len(note_image)+i,0,note_video[i].get())
        sheet1.write(len(note_image)+i,1,valence_video[i].get())
        sheet1.write(len(note_image)+i,2,os.path.basename(videos[i]))
    
    wb.save(path+'/Excel.xls')
    
    fenetre.destroy()
    
# Define notation structure
def reset() :
    global note_image, note_video
    
    for i in range(len(note_image)) :
        note_image[i].set(0)
        
    for i in range(len(note_video)) :
        note_video[i].set(0)
    
    for i in range(len(valence_video)) :
        valence_video[i].set(0)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=700,height=500)

#Define frame 
## Videos 
##Boutons 
def boutons() :
    
    for i in range(len(videos)) :

        objet_video.append(tk.Frame(master=newframe,background="azure"))
        objet_video[i].grid(row=i,column=0,columnspan=2)
        
        bouton_video.append(tk.Button(objet_video[i],command=video(videos[i]).jouer_video,text="Vidéo "+str(i+1),bg='LightSkyBlue1',font=("Constantia",12,'bold')))
        bouton_video[i].grid(padx=5,pady=5,row=i,column=0)
##Scales

        valence_video.append(tk.Scale(objet_video[i],from_=0, to=1,orient='horizontal',resolution=1,label="Négatif             Positif",background="azure",highlightbackground="azure",font=("Constantia",10,'italic')))
        valence_video[i].grid(padx=15,pady=15,ipady=15,ipadx=15,row=i,column=1)
        
        note_video.append(tk.Scale(objet_video[i],from_=0, to=20,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_video[i].grid(padx=5,pady=5,row=i,column=2)

##Images
    for i in range(len(images)) :
        
    
        objet_image.append(tk.Frame(master=newframe,background="azure"))
        objet_image[i].grid(row=i,column=2,columnspan=2)
        
        bouton_image.append(tk.Button(objet_image[i],command=image(images[i]).montrer_image,text="Image "+str(i+1),bg='SteelBlue1',font=("Constantia",12,'bold')))
        bouton_image[i].grid(padx=5,pady=5,row=i,column=2)
        
        note_image.append(tk.Scale(objet_image[i],from_=0, to=10,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_image[i].grid(padx=5,pady=5,row=i,column=3)


##Define the path to access videos (mp4 format)   
path = Path("Project").parent.absolute()
path=str(path)

images=glob.glob(path+"/*.jpg")
videos=glob.glob(path+"/*.mp4")

#Define responses of subjects 
objet_video=[]
bouton_video=[]
note_video=[]
valence_video=[]

objet_image=[]
bouton_image=[]
note_image=[]

## Putting all in the frame of the interface 
##Use of Tkinter
fenetre=tk.Tk()

sizex = 750
sizey = 720
posx  = 100
posy  = 100
fenetre.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

frame=tk.Frame(fenetre,relief='groove')
frame.place(x=10,y=8)
canvas=tk.Canvas(frame)
newframe=tk.Frame(canvas)
myscrollbar=tk.Scrollbar(frame,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=newframe,anchor='nw')
frame.bind("<Configure>",myfunction)
newframe.config(background="azure",highlightbackground="azure")
frame.config(background="azure",highlightbackground="azure")
canvas.config(background="azure",highlightbackground="azure")


boutons()

#Define the Menu of the interface 
menubar = tk.Menu(fenetre)
menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Fini",command=sortie)
menu1.add_command(label="Recommencer",command=reset)
menubar.add_cascade(label="Menu",menu=menu1)
fenetre.config(menu=menubar,background="azure")


fenetre.mainloop()
    

