# PCBS Project : Une plateforme d'évaluation de stimuli émotionnels 

   L'émotion est traditionnellement définie comme épisode de changements interdépendants et synchronisés d'une composante physiologique, cognitive et comportementale, en réponse à un événement signficatif pour l’organisme; selon la définition de Sander et R. Scherer, 2009. On peut caractérisée une émotion par sa valence (plutôt positive ou négative) et son intensité (amplitude des activations physiologiques, niveau de significativité pour le sujet). Afin d'évaluer la réponse émotionnelle en psychologie expérimentale, les sujets sont la plupart du temps confrontés à des stimuli visuels tels que des photographies (visages, paysages, animaux) ou des séquences filmiques. Par ailleurs, certaines composantes d'une réaction émotionnelle peut aussi être inclue comme facteur de variations sur une mesure comportementale. 
L'activation émotionnelle est une donnée psychophysiologique soumise à une variabilité intra-individuelle très conséquente. Ainsi, utiliser des stimuli émotionnels requiert de confronter ses sujets à des photographies ou vidéos suffisamment stimulantes pour qu'une réaction émerge, tout en gardant l'idée que le matériel expérimental est soumis à l'avis un comité d'éthique. Les stimuli doivent donc faire l'objet d'un pré-test afin de vérifier qu'ils sont suffisamment efficients pour être utilisés dans l'expérience future. 

Mon programme consiste donc en une plateforme de présentation successive de séquences filmiques, dotées chacune d'une échelle de valence et d'intensité, directement manipulables par le sujet. Il peut décider du lancement de la vidéo, et peut bouger le curseur sur l'échelle le long de valeurs discrètes allant de 1 à 10. Initialement, mon programme était une proposition de support pour le pré-test de l'étude de mon laboratoire de stage (Cognition Humaine & artificielle, Université Paris 10). Cette étude s'intéresse notamment contact social non-verbal (contact oeil-oeil, prononciation régulière du prénom de la personne au cours du dialogue, toucher social) comme facteur de variation comportementale. Elle teste l'hypothèse selon laquelle l'augmentation d'un tel contact influence la cohérence entre une mesure auto-rapportée de la réaction émotionnelle et la réponse électrodermale. On appelle cette cohérence la précision intéroceptive, et se mesure par des tests sur des corrélations. 


# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:27:33 2019

@author: Flora
"""

# importing libraries 

import tkinter as tk
from xlwt import Workbook 
import glob
from os import startfile
import sys, os
from pathlib import Path
import tkinter.tix as tktix

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
    
def boutons() :
    
    for i in range(len(videos)) :

    
        objet_video.append(tk.Frame(master=newframe,background="azure"))
        objet_video[i].grid(row=i,column=0,columnspan=2)
        
        bouton_video.append(tk.Button(objet_video[i],command=video(videos[i]).jouer_video,text="Vidéo "+str(i+1),bg='LightSkyBlue1',font=("Constantia",12,'bold')))
        bouton_video[i].grid(padx=5,pady=5,row=i,column=0)

        valence_video.append(tk.Scale(objet_video[i],from_=0, to=1,orient='horizontal',resolution=1,label="Négatif             Positif",background="azure",highlightbackground="azure",font=("Constantia",10,'italic')))
        valence_video[i].grid(padx=15,pady=15,ipady=15,ipadx=15,row=i,column=1)
        
        note_video.append(tk.Scale(objet_video[i],from_=0, to=20,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_video[i].grid(padx=5,pady=5,row=i,column=2)


  
    
    for i in range(len(images)) :
        
    
        objet_image.append(tk.Frame(master=newframe,background="azure"))
        objet_image[i].grid(row=i,column=2,columnspan=2)
        
        bouton_image.append(tk.Button(objet_image[i],command=image(images[i]).montrer_image,text="Image "+str(i+1),bg='SteelBlue1',font=("Constantia",12,'bold')))
        bouton_image[i].grid(padx=5,pady=5,row=i,column=2)
        
        note_image.append(tk.Scale(objet_image[i],from_=0, to=10,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_image[i].grid(padx=5,pady=5,row=i,column=3)

```python
path = Path("Project").parent.absolute()
path=str(path)

images=glob.glob(path+"/*.jpg")
videos=glob.glob(path+"/*.mp4")

objet_video=[]
bouton_video=[]
note_video=[]
valence_video=[]

objet_image=[]
bouton_image=[]
note_image=[]

    
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
```

```javascript
boutons()


menubar = tk.Menu(fenetre)
menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Fini",command=sortie)
menu1.add_command(label="Recommencer",command=reset)
menubar.add_cascade(label="Menu",menu=menu1)
fenetre.config(menu=menubar,background="azure")


fenetre.mainloop()
```




