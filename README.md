# PCBS Project: une plateforme d'évaluation de stimuli émotionnels 

   L'émotion est traditionnellement définie comme épisode de changements physiologiques, cognitifs et comportementaux, interdépendants et synchronisés, en réponse à un événement signficatif pour l’organisme; selon la définition de Sander et Scherer, 2009. On peut caractériser phénoménologiquement une émotion par sa valence (plutôt positive ou négative) et son intensité (amplitude des activations physiologiques, niveau de significativité pour le sujet). Afin d'évaluer la réponse émotionnelle en psychologie expérimentale, les sujets sont la plupart du temps confrontés à des stimuli visuels tels que des photographies (visages, paysages, animaux) ou des séquences filmiques. Par ailleurs, certaines composantes d'une réaction émotionnelle peuvent aussi être inclues comme facteur de variations sur une mesure comportementale. 
L'activation émotionnelle est une donnée psychophysiologique soumise à une variabilité intra-individuelle très conséquente. Ainsi, utiliser des stimuli émotionnels requiert de confronter ses sujets à des photographies ou vidéos suffisamment stimulantes pour qu'une réaction émerge, tout en gardant en tête que le matériel expérimental est soumis à l'avis un comité d'éthique. Les stimuli doivent donc faire l'objet d'un pré-test afin de vérifier qu'ils sont suffisamment efficients pour être utilisés dans l'expérience future. 

Mon programme consiste donc en une plateforme de présentation successive de séquences filmiques, dotées chacune d'une échelle de valence et d'intensité, directement manipulables par le sujet. Il peut décider du lancement de la vidéo, et peut bouger le curseur sur l'échelle le long de valeurs discrètes allant de 1 à 10. Initialement, mon programme était une proposition de support pour le pré-test de l'étude de mon laboratoire de stage (Cognition Humaine & artificielle, Université Paris 10). Cette étude s'intéresse au contact social non-verbal (contact oeil-oeil, toucher social) comme facteur de variation comportementale. Elle teste l'hypothèse selon laquelle l'augmentation d'un tel contact influence la cohérence entre une mesure auto-rapportée de la réaction émotionnelle et la réponse électrodermale. On appelle cette cohérence la précision intéroceptive, et se mesure par des tests sur des corrélations. 

## Structure du programme 
* Importation des packages 
* Définition des objets 
* Output Excel
* Echelles de notations 
* Réponse via les boutons 
* Frame de l'interface 

# importing libraries 
On importe les packages nécessaires : Tkinter pour l'interface, Workbook de xlwt pour l'output Excel, Os pour utiliser les fonctions dépendantes du système d'exploitation (windows), Pathlib pour aller chercher les fichiers. 

```python
import tkinter as tk
from xlwt import Workbook 
import glob
from os import startfile
import sys, os
from pathlib import Path
import tkinter.tix as tktix
```

## Définition des objets 
Le programme peut être utilisé avec des vidéos (format mp4) mais aussi des images (format jpg). Les images ne figurent pas dans ma database mais peuvent toutefois être ajoutées car il y a du code disponible pour. Les objets sont les vidéos (référencées en tant que Self)

```python
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
```

### Output 
On définit la sortie grâce à la fonction Workbook. C'est-à-dire qu'on va recevoir un fichier Excel dans le dossier mère à la fin de la notation avec les chiffres & la valence correspondante. On utilise le path local + ``/Excel.xls`` pour que le programme retrouve le fichier Excel. La plupart des intéractions entre les fichiers & le programme utilisent le path & les fonctions Os, **il faut donc bien tout mettre ensemble dans un dossier sinon plus rien ne va.** 
```python
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
``` 
### Définition de la valence et de l'intensité des stimuli
On utilise une ``forloop`` pour que chaque vidéo puisse faire l'objet d'une note.
```python
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
```
### Putting all together 
* *Boutons*

On va installer les boutons et leur ajouter un design sur l'interface, et les lier au lancement des vidéos, de façon à ce que lorsqu'on appuie sur le bouton, la vidéo se lance. 
```python
def boutons() :
    
    for i in range(len(videos)) :

        objet_video.append(tk.Frame(master=newframe,background="azure"))
        objet_video[i].grid(row=i,column=0,columnspan=2)

        bouton_video.append(tk.Button(objet_video[i],command=video(videos[i]).jouer_video,text="Vidéo "+str(i+1),bg='LightSkyBlue1',font=("Constantia",12,'bold')))
        bouton_video[i].grid(padx=5,pady=5,row=i,column=0)
```
* *Echelle de valence* 
```python
        valence_video.append(tk.Scale(objet_video[i],from_=0, to=1,orient='horizontal',resolution=1,label="Négatif             Positif",background="azure",highlightbackground="azure",font=("Constantia",10,'italic')))
        valence_video[i].grid(padx=15,pady=15,ipady=15,ipadx=15,row=i,column=1)
```
* *Echelle d'intensité* 
```python
        note_video.append(tk.Scale(objet_video[i],from_=0, to=20,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_video[i].grid(padx=5,pady=5,row=i,column=2)
``` 
(On a tenté un petit style dans les teintes bleu azur, cela va bien avec les vidéos de plage : on voyage !) 

Nb : Des lignes sont aussi implémentées pour les images: 
```python
    for i in range(len(images)) :
        
        objet_image.append(tk.Frame(master=newframe,background="azure"))
        objet_image[i].grid(row=i,column=2,columnspan=2)
        
        bouton_image.append(tk.Button(objet_image[i],command=image(images[i]).montrer_image,text="Image "+str(i+1),bg='SteelBlue1',font=("Constantia",12,'bold')))
        bouton_image[i].grid(padx=5,pady=5,row=i,column=2)
        
        note_image.append(tk.Scale(objet_image[i],from_=0, to=10,orient='horizontal',background="azure",highlightbackground="azure",resolution=1,label="Note",font=("Constantia",12,'italic')))
        note_image[i].grid(padx=5,pady=5,row=i,column=3)
``` 
### Réponse
Lier la notation réponse à chaque vidéo.
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
```
### Frame de l'interface 
On crée la fenêtre qui sera le hub pour tout le matériel. 
```python
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
``` 
Cette fonction permet d'ajouter une scrollbar sur l'interface au cas où on ait beaucoup de vidéos. Elle a fait l'objet de moult nuits blanches. 
```python
mybar=tk.Scrollbar(frame,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
``` 
On dispose le matériel sur l'interface
```python
canvas.pack(side="left")
canvas.create_window((0,0),window=newframe,anchor='nw')
frame.bind("<Configure>",myfunction)
newframe.config(background="azure",highlightbackground="azure")
frame.config(background="azure",highlightbackground="azure")
canvas.config(background="azure",highlightbackground="azure")

boutons()
```
Petit plus : on ajoute un Menu afin que le sujet puisse prévenir quand il a fini, ou encore recommencer si cela lui a tellement plu qu'il veut le refaire. 
``` python
menubar = tk.Menu(fenetre)
menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Fini",command=sortie)
menu1.add_command(label="Recommencer",command=reset)
menubar.add_cascade(label="Menu",menu=menu1)
fenetre.config(menu=menubar,background="azure")
```
Enfin, on envoie le tout : 
```python
fenetre.mainloop()
```

## Quelques notes sur le programme 
La totalité du programme (je l'ai appelé "EmoRater") est dans le fichier main_EmoRater.py. Les vidéos utilisées sont dans le fichier Vidéos & uploadées séparémment. La base de données que nous utilisons dans l'expérience d'origine n'est pas disponible en libre usage, c'est pourquoi j'ai mis à disposition des petites vidéos libre-accès trouvées sur internet, qui présentent principalement des animaux ou des séquences dénuées d'intérêt particulier (cependant à titre personnel, j'en trouve certaines plutôt amusantes).

J'ajoute que je suis bien consciente que ce programme n'est pas du grand art de programmeur. Un milliard d'éléments auraient pu être améliorés, en termes de display, d'ergonomie (également au niveau du post sur github), de fonctionnalités, etc. Ce programme ne fourmille pas non plus de pertinence en termes d'analyse des fonctions cognitives, toutefois il ne faut pas oublier la dimension pratique des expériences (surtout en psychologie) et le pré-test des stimuli est une étape non-négligeable si on veut monter en validité expérimentale. 

Etant de background psychologie, je me suis surtout intéressée au langage R durant ce semestre, python n'étant pas ma priorité. Je voulais d'abord tenter une Balloon Analogue Risk Task (Lejuez & al., 2002) mais il va de soi que ce n'était pas de mon niveau. 
Ce que j'aurais pu faire, cependant, c'est extraire l'output des notations sur l'Excel et coder une micro-analyse des indices de tendance centrale et de dispersion sur R. Cela aurait été intéressant et aurait complété le programme, mais je n'ai pas eu le temps. 

Crucialement : Ce programme n'a pas été utilisé pour le pré-test, mon superviseur a préféré utiliser un bon vieux E-prime 3.0 (et on le comprend !) 

## Retour sur la pédagogie du cours PCBS
L'intention est là, pour sûr. On a vraiment besoin d'apprendre le code et on en est tous conscients. Cependant, il y a un problème dans la disposition de l'enseignement. Il serait peut être bien d'essayer un vrai cours, c'est-à-dire, une intéraction entre le groupe et le professeur, la résolution d'exercices ensemble, un apprentissage pas à pas où tout le monde intéragit, et si c'est possible, un rendu de projet final adapté au niveau de chacun. Il est, selon moi, important de diviser la classe en groupes de niveau comme le cours Datacamp. 
Etant débutante, j'ai plus appris en Datacamp qu'en PCBS, je pense que les projets établis pour PCBS reposent à 95% sur les connaissances préalables et la recherche en autonomie sur internet et à 5% sur les cours. Cependant, tout ce que je dis là ne met en aucun cas en cause les intervenants pour cet UE, qui ont su être toujours disponible pour aider et répondre aux questions. 

## Référence  
Sander, D., & Scherer, K. R. (2014). Traité de psychologie des émotions. Paris : Dunod.




