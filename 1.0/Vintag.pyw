"""
##############################
    Vintag.
##############################
    Coded by: Dalton Overlin
##########################################################
    Last Code Revision Date: May. 12th, 2020
##########################################################
    This program is for sorting a directory full of mp3
    files. It scans the directory you slect to sort and
    then allows you to verify and define genres, the
    album name, artist, and even the year for each album.
    Then everything is sorted into folders based on your
    selections. The program utilizes a GUI
    interface using tkinter to make the program more
    user friendly. This is freeware! FREEWARE!
    So if someone asked you to pay for this program
    then they are a crook and you've been scammed!
    I am releasing this program for use at no cost.
    I will not be giving anyone, any form
    of authorization to sell this program (unmodified) for
    a price. Just be aware of this, this code is open source
    and is Freeware! Don't be tricked into paying for free software.
##########################################################
MIT License
-----------

Copyright (c) 2020 Dalton Overlin https://github.com/Dalton-Overlin/Vintag
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""
def installer(x):
    print(('\n'*2)+'This module: ( '+x+' ) is not installed.\n\nIf you type yes & press enter I will try and install it for you.\nIf not, just press enter and the program will exit.\nNote, here are two commands you can run to install the missing module.\n\n'+'python -m pip install '+x+'pip install '+x)
    c=str(input())
    if 'yes' in c.lower() or 'y' in c.lower():
        vue=os.system('python -m pip install '+str(x))
        if vue==0:
            return
        else:
            print('\n\nThis module: ',str(x),' could not be automatically installed, please install it manually.')
            input()
            exit()
    else:
        print('Exiting, Goodbye:)')
        exit()
import threading
try:
    import os
except:
    installer('os')
    import os
try:
    import random
except:
    installer('random')
    import random
try:
    import string
except:
    installer('string')
    import string
try:
    import tkinter
    from tkinter import *
    from tkinter import filedialog
    from tkinter import PhotoImage
    import tkinter.font as tkFont
    import tkinter as tk
except:
    installer('tkinter')
    import tkinter
    from tkinter import *
    from tkinter import filedialog
    from tkinter import PhotoImage
    import tkinter.font as tkFont
    import tkinter as tk
try:
    import shutil
except:
    installer('shutil')
    import shutil
try:
    import time
except:
    installer('time')
    import time
try:
    import datetime
except:
    installer('datetime')
    import datetime
try:
    import eyed3
except:
    installer('eyed3')
    import eyed3
try:
    import tinytag
    from tinytag import TinyTag
except:
    installer('tinytag')
    import tinytag
    from tinytag import TinyTag
try:
    from PIL import ImageTk, Image
except:
    installer('pillow')
    from PIL import ImageTk, Image
class ex:
    thisOS = os.name
    tide = os.getcwd()
    activebackground="dark green"
    activeforeground="lawn green"
    fg="white"
    v='/'
    fold=None
    darkgreen='chartreuse4' # ex.darkgreen
    white='white' # ex.white
    black='dark green' # ex.black
    green4='green4' # ex.green4
    green3='green3' # ex.green3
    lime='lawn green' # ex.lime
    seagreen='SpringGreen4' # ex.seagreen For the editor window bg.
    forestgreen='forest green' # ex.forestgreen
    vall=None
if "nt" in ex.thisOS: ex.v = "\\"
else: ex.v = "/"
class maxx:
    div=' ' # This can be anything like ' ', ' - ', etc.  maxx.div
def reno(Input):
    if type(Input)!=list:
        print('Input must be list!')
        return None
    else:
        if Input==[]:
            print('Cant send empty list for sorting!')
    newHold=[]
    Input.sort()
    for tv in Input: # This primes the data.
        t=str(tv)
        while t[0]==' ':
            t=t[1:]
        kpop=True
        try:
            if t[:2]=='NA' and t[2:3] in [' ','-','_','+','=','~','.']:
                temp = str(t)
                temp=temp.strip()
                if temp[:2]=='NA':
                    temp=temp[2:]
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
            elif t.replace(' ','')[0] in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
                temp = str(t)
                temp=temp.strip()
                con=0
                for v in temp:
                    if v in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        con+=1
                    else:
                        break
                temp=temp[con:]
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
            else:
                temp = str(t)
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
        except:
            temp = str(t)
            temp=temp.strip()
            newHold.append(maxx.div+temp)
    tim=len(str(len(newHold)))
    if tim==1:
        tim=2
    cova=1
    holder=[]
    for t in newHold:
        temp=str(cova)
        while len(temp) != tim:
            temp='0'+temp
        holder.append(temp+t)
        cova+=1
    return holder
if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
    os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
    os.remove(ex.tide+ex.v+'temp-vox.jpg')
class dirTree:
    A=os.getcwd()
    B=os.getcwd()
def browse_button():
    coo = filedialog.askdirectory(initialdir = dirTree.B)
    if os.path.isdir(coo):
        dirTree.B=str(coo)
    return coo
def browseFile():
    return filedialog.askopenfilename(initialdir = dirTree.A,title = "Select Image File",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
class dat:
    albums=None
    data=None
    clock=None
    path=None
    yaro=True
    canva=None
    koi=False
    merge=[] # dat.merge
    mergetta=False # dat.mergetta
    curMer=[] # dat.curMer=[]
    curMerSize=0 # dat.curMerSize
    merge2=[] # dat.merge
    curMer2=[] # dat.curMer=[]
    curMerSize2=0 # dat.curMerSize
class net:
    popupMenu=None
    popupMenu2=None
    popupMenu3=None
    popupMenu4=None
    tkvar=None
    tkvar2=None
    tkvar3=None
    tkvar4=None
class ram:
    ResizeAlbumCoverSize=480,480
def masterLoop(folderPath):
    dat.albums=None
    dat.data=None
    dat.clock=None
    dat.path=None
    dat.yaro=True
    dat.canva=None
    dat.koi=False
    dat.merge=[] # dat.merge
    dat.mergetta=False # dat.mergetta
    dat.curMer=[] # dat.curMer=[]
    dat.curMerSize=0 # dat.curMerSize
    dat.merge2=[] # dat.merge
    dat.curMer2=[] # dat.curMer=[]
    dat.curMerSize2=0 # dat.curMerSize
    net.popupMenu=None
    net.popupMenu2=None
    net.popupMenu3=None
    net.popupMenu4=None
    net.tkvar=None
    net.tkvar2=None
    net.tkvar3=None
    net.tkvar4=None
    albums=[]
    data=[]
    try:
        raw=os.listdir(folderPath)
        if raw == []:
            return "No Files."
        gold=True
        for t in raw:
            if t[-4:] == '.mp3':
                aussie=eyed3.load(folderPath+ex.v+t)
                alName=aussie.tag.album
                if '\\' in alName or '/' in alName:
                    alName=alName.replace('\\',';').replace('/',';')
                if alName!='':
                    gold = False
                    if alName not in albums:
                        albums.append(alName)
                        data.append([alName,[t]])
                    else:
                        data[albums.index(alName)][-1].append(t)
        if gold:
            return 'No mp3s'
    except:
        return 'Error 3'
    clock=0
    dat.path=folderPath
    dat.clock,dat.albums,dat.data=clock,albums,data
    root = tkinter.Tk()
    def doMe():
        root.destroy()
        ex.fold='Exited Early!'
        return
    root.protocol('WM_DELETE_WINDOW', doMe)
    w = 610
    h = 310
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background=ex.seagreen)
    root.title('Configurator. Tracks: 0')
    dat.canva=tkinter.Canvas(root, bg=ex.green3, height=218, width=218)
    dat.canva.pack()
    dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
    net.tkvar = StringVar(root)
    choices = ['Acapella', 'Acid', 'Acid Jazz', 'Acid Punk', 'Acoustic', 'Alternative', 'Alternative Rock', 'Ambient','ASMR', 'Anime', 'Avantgarde', 'Ballad', 'Bass', 'Beat', 'Bebob', 'Big Band', 'Black Metal', 'Bluegrass', 'Blues', 'Booty Bass', 'BritPop', 'Cabaret', 'Celtic', 'Chamber Music', 'Chanson', 'Chorus', 'Christian Gangsta Rap', 'Christian Rap', 'Christian Rock', 'Classic Rock', 'Classical', 'Club', 'Comedy', 'Contemporary Christian', 'Country', 'Crossover', 'Cult', 'Dance', 'Dance Hall', 'Darkwave', 'Death Metal', 'Disco', 'Dream', 'Drum & Bass', 'Drum Solo', 'Duet', 'Easy Listening', 'Egypt', 'Electronic', 'Ethnic', 'Euro-House', 'Euro-Techno', 'Eurodance', 'Fast Fusion', 'Folk', 'Folk-Rock', 'Folklore', 'Freestyle', 'Funk', 'Fusion', 'Game', 'Gangsta', 'Goa', 'Gospel', 'Gothic', 'Gothic Rock', 'Grunge', 'Hard Rock', 'Hardcore', 'Heavy Metal', 'Hip-Hop', 'House', 'House', 'Humour', 'Indie', 'Industrial', 'Instrumental', 'Instrumental Pop', 'Instrumental Rock', 'JPop', 'Jazz', 'Jazz+Funk', 'Jungle', 'Latin', 'Lo-Fi', 'Meditative', 'Merengue', 'Metal', 'Musical', 'National Folk', 'Native US', 'Negerpunk', 'New Age', 'New Wave', 'Noise', 'Oldies', 'Opera', 'Other', 'Polka', 'Polsk Punk', 'Pop', 'Pop-Folk', 'Pop-Funk', 'Porn Groove', 'Power Ballad', 'Pranks', 'Primus', 'Progressive Rock', 'Psychadelic', 'Psychedelic Rock', 'Punk', 'Punk Rock', 'R&B', 'Rap', 'Rave', 'Reggae', 'Retro', 'Revival', 'Rhythmic Soul', 'Rock','Russian','Rpop','RusPop', 'Rock & Roll', 'Salsa', 'Samba', 'Satire', 'Showtunes', 'Ska', 'Slow Jam', 'Slow Rock', 'Sonata', 'Soul', 'Sound Clip', 'Soundtrack', 'Southern Rock', 'Space', 'Speech', 'Swing', 'Symphonic Rock', 'Symphony', 'Synthpop', 'Tango', 'Techno', 'Techno-Industrial', 'Terror', 'Thrash Metal', 'Top 40', 'Trailer', 'Trance', 'Tribal', 'Trip-Hop', 'Unknown', 'Vocal', 'Vocal']
    net.tkvar.set('Pop')
    net.popupMenu = OptionMenu(root, net.tkvar, *choices)
    net.popupMenu.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
    net.popupMenu.place(bordermode=OUTSIDE, height=30, width=310/3,relx=0.084, rely=0, anchor=N)
    def mergeManager2(chosenAlbum,theRawMergeDataFromStepOne): # Step Two.
        dat.curMer=[]
        net.tkvar2 = StringVar(root)
        choices2 = [] # Will hold the album names.
        for t in theRawMergeDataFromStepOne:
            for th in t[-1]:
                dat.curMer.append(th)
            choices2.append(t[0])
        net.tkvar2.set(chosenAlbum)
        net.popupMenu2 = OptionMenu(root, net.tkvar2, *choices2)
        net.popupMenu2.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu2.place(bordermode=OUTSIDE, height=30, width=200,relx=0.0840*4, rely=0, anchor=N)
        art=[]
        year=[]
        root.title('Vintag. Merger.')
        clue=None
        photor=None
        photon=True
        for kin in theRawMergeDataFromStepOne:
            if str(kin[0])==chosenAlbum:
                for t in kin[-1]:
                    cx=eyed3.load(dat.path+ex.v+t)
                    arty=cx.tag.artist
                    if '\\' in arty or '/' in arty:
                        arty=arty.replace('\\',';').replace('/',';')
                    if arty not in art:
                        art.append(arty)
                    yeary=str(cx.tag.recording_date)[:4]
                    if '\\' in yeary or '/' in yeary:
                        yeary=yeary.replace('\\',';').replace('/',';')
                    if yeary not in year:
                        year.append(yeary)
                    if photon:
                        tag = TinyTag.get(dat.path+ex.v+t,image=True)
                        try:
                            photor=tag.get_image()
                            if photor == '' or photor == None or len(photor) < 10:
                                pass
                            else:
                                photon=False
                        except:
                            pass
            else:
                for t in kin[-1]:
                    cx=eyed3.load(dat.path+ex.v+t)
                    arty=cx.tag.artist
                    if '\\' in arty or '/' in arty:
                        arty=arty.replace('\\',';').replace('/',';')
                    if arty not in art:
                        art.append(arty)
                    yeary=str(cx.tag.recording_date)[:4]
                    if yeary not in year:
                        year.append(yeary)
        if photon:
            dat.canva.destroy()
            dat.canva=tkinter.Canvas(root, bg=ex.green3, height=218, width=218)
            dat.canva.pack()
            dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
            dat.koi=False
        else:
            dat.canva.destroy()
            try:
                grey=open(ex.tide+ex.v+'temp-vox-O.jpg','wb')
                grey.write(photor)
                grey.close()
                im = Image.open(ex.tide+ex.v+'temp-vox-O.jpg')
                size = 480, 480
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(ex.tide+ex.v+'temp-vox.jpg','JPEG')
                image = Image.open(ex.tide+ex.v+'temp-vox.jpg')
                size = 218, 218
                image.thumbnail(size,Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                dat.canva=tkinter.Canvas(root,bg=ex.green3, height=218, width=218)
                dat.canva.pack()
                dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
                label = Label(dat.canva,image=photo)
                label.image = photo
                label.place(bordermode=OUTSIDE,relx=0,rely=0,width=218,height=218)
                dat.koi=True
            except:
                dat.canva=tkinter.Canvas(root, bg=ex.green3, height=218, width=218)
                dat.canva.pack()
                dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
                dat.koi=False
        art.sort()
        art.append('Defaults')
        year.sort()
        if str(datetime.datetime.now().year) not in year:
            year.append(str(datetime.datetime.now().year))
        year.append('Defaults')
        net.tkvar3 = StringVar(root)
        choices3 = art
        net.tkvar3.set(art[0])
        net.popupMenu3 = OptionMenu(root, net.tkvar3, *choices3)
        net.popupMenu3.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu3.place(bordermode=OUTSIDE, height=30, width=200,relx=0.0835*8, rely=0, anchor=N)
        net.tkvar4 = StringVar(root)
        choices4 = year
        net.tkvar4.set(year[0])
        net.popupMenu4 = OptionMenu(root, net.tkvar4, *choices4)
        net.popupMenu4.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu4.place(bordermode=OUTSIDE, height=30, width=(310/3)-3,relx=0.08337*11, rely=0, anchor=N)
        B.config(state=NORMAL)
        B2.config(state=NORMAL)
        B3.config(state=NORMAL)
        B4.config(state=NORMAL)
        a.config(state=NORMAL)
        a1.config(state=NORMAL)
        a2.config(state=NORMAL)
    def mergeManager(kilo,numm): # Step One.
        B.config(state=DISABLED)
        B2.config(state=DISABLED)
        B3.config(state=DISABLED)
        B4.config(state=DISABLED)
        a.config(state=DISABLED)
        a1.config(state=DISABLED)
        a2.config(state=DISABLED)
        af.config(state=DISABLED)
        af2.config(state=DISABLED)
        rooty = tkinter.Tk()
        def doMe4():
            root.destroy()
            rooty.destroy()
            ex.fold='Exited Early!'
            return
        rooty.protocol('WM_DELETE_WINDOW', doMe4)
        w = 400
        h = 60
        ws = rooty.winfo_screenwidth()
        hs = rooty.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        rooty.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rooty.resizable(0, 0)
        rooty.configure(background=ex.forestgreen)
        rooty.title('Select Album Name to Extract Cover From')
        net.tkvar2 = StringVar(rooty)
        class beyroute:
            captain=[]
            typ=0
        beyroute.typ=numm
        choices2 = [] # Will hold the album names.
        for t in kilo:
            choices2.append(str(t[0]))
            beyroute.captain.append(t)
        choices2.sort()
        net.tkvar2.set(choices2[0])
        net.popupMenu2 = OptionMenu(rooty, net.tkvar2, *choices2)
        net.popupMenu2.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime,font=('Helvetica', 11, 'bold'))
        net.popupMenu2.place(bordermode=OUTSIDE, height=30, width=400,relx=0.5, rely=0, anchor=N)
        def gaya():
            heaven=str(net.tkvar2.get())
            net.popupMenu2.destroy()
            rooty.destroy()
            if beyroute.typ==1:
                dat.merge=[]
            else:
                dat.merge2=[]
            mergeManager2(heaven,beyroute.captain)
        Bf = tkinter.Button(rooty,text ="Next",command=gaya, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 11, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        Bf.pack()
        Bf.place(bordermode=OUTSIDE, height=30, width=300,relx=0.5, rely=1, anchor=S)
        rooty.mainloop()
    def Update():
        cobra=False
        if dat.yaro:
            dat.yaro=False
        else:
            net.popupMenu2.destroy()
            net.popupMenu3.destroy()
            net.popupMenu4.destroy()
            if dat.clock==len(dat.albums):
                if dat.merge!=[]:
                    dat.mergetta=True
                    mergeManager(dat.merge,1)
                    #dat.merge=[]
                    return
                elif dat.merge2!=[]:
                    dat.mergetta=True
                    mergeManager(dat.merge2,2)
                    #dat.merge2=[]
                    return
                else:
                    root.destroy()
                    ex.fold='All Done!'
                    return
            else:
                if dat.mergetta:
                    root.destroy()
                    ex.fold='All Done!'
                    return
        net.tkvar2 = StringVar(root)
        choices2 = [dat.albums[dat.clock]] # Will hold the album names.
        net.tkvar2.set(dat.albums[dat.clock])
        net.popupMenu2 = OptionMenu(root, net.tkvar2, *choices2)
        net.popupMenu2.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu2.place(bordermode=OUTSIDE, height=30, width=200,relx=0.0840*4, rely=0, anchor=N)
        art=[]
        year=[]
        root.title('Vintag. Tracks: '+str(len(dat.data[dat.clock][-1]))+'   Album: '+str(dat.data[dat.clock][0]))
        photor=None
        photon=True
        for t in dat.data[dat.clock][-1]:
            cx=eyed3.load(dat.path+ex.v+t)
            arty=cx.tag.artist
            if '\\' in arty or '/' in arty:
                arty=arty.replace('\\',';').replace('/',';')
            if arty not in art:
                art.append(arty)
            yeary=str(cx.tag.recording_date)[:4]
            if '\\' in yeary or '/' in yeary:
                yeary=yeary.replace('\\',';').replace('/',';')
            if yeary not in year:
                year.append(yeary)
            if photon:
                tag = TinyTag.get(dat.path+ex.v+t,image=True)
                try:
                    photor=tag.get_image()
                    if photor == '' or photor == None or len(photor) < 10:
                        pass
                    else:
                        photon=False
                except:
                    pass
        if photon:
            dat.canva.destroy()
            dat.canva=tkinter.Canvas(root, bg=ex.green3, height=218, width=218)
            dat.canva.pack()
            dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
            dat.koi=False
        else:
            dat.canva.destroy()
            try:
                grey=open(ex.tide+ex.v+'temp-vox-O.jpg','wb')
                grey.write(photor)
                grey.close()
                im = Image.open(ex.tide+ex.v+'temp-vox-O.jpg')
                size = ram.ResizeAlbumCoverSize
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(ex.tide+ex.v+'temp-vox.jpg','JPEG')
                image = Image.open(ex.tide+ex.v+'temp-vox.jpg')
                size = 218, 218
                image.thumbnail(size,Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                dat.canva=tkinter.Canvas(root,bg=ex.green3, height=218, width=218)
                dat.canva.pack()
                dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
                label = Label(dat.canva,image=photo)
                label.image = photo
                label.place(bordermode=OUTSIDE,relx=0,rely=0,width=218,height=218)
                dat.koi=True
            except:
                dat.canva=tkinter.Canvas(root, bg=ex.green3, height=218, width=218)
                dat.canva.pack()
                dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
                dat.koi=False
        art.sort()
        art.append('Defaults')
        year.sort()
        if str(datetime.datetime.now().year) not in year:
            year.append(str(datetime.datetime.now().year))
        year.append('Defaults')
        net.tkvar3 = StringVar(root)
        choices3 = art
        net.tkvar3.set(art[0])
        net.popupMenu3 = OptionMenu(root, net.tkvar3, *choices3)
        net.popupMenu3.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu3.place(bordermode=OUTSIDE, height=30, width=200,relx=0.0835*8, rely=0, anchor=N)
        net.tkvar4 = StringVar(root)
        choices4 = year
        net.tkvar4.set(year[0])
        net.popupMenu4 = OptionMenu(root, net.tkvar4, *choices4)
        net.popupMenu4.config(bg=ex.darkgreen,fg=ex.white,activebackground=ex.black,activeforeground=ex.lime)
        net.popupMenu4.place(bordermode=OUTSIDE, height=30, width=(310/3)-3,relx=0.08337*11, rely=0, anchor=N)
        dat.clock+=1
    Update()
    def Next():
        '''   This is the part that will save the data.  '''
        if dat.mergetta: # This is for if in the merge phase.
            tracks= dat.curMer
            tracks.sort()
            newTracks=[]
            lena=len(tracks)
            newTracks=reno(tracks)
        else:
            tracks=dat.data[dat.clock-1][-1]
            tracks.sort()
            newTracks=[]
            lena=len(tracks)
            newTracks=reno(tracks)
        co=0
        for t in tracks: # This should rename the tracks.
            os.rename(dat.path+ex.v+t,dat.path+ex.v+newTracks[co])
            co+=1
        if os.path.isdir(dat.path+ex.v+net.tkvar.get()):
            pass
        else:
            os.mkdir(dat.path+ex.v+net.tkvar.get())
        if os.path.isdir(dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get()):
            pass
        else:
            os.mkdir(dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get())
        if os.path.isdir(dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get()+ex.v+net.tkvar2.get()):
            pass
        else:
            os.mkdir(dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get()+ex.v+net.tkvar2.get())
        for t in newTracks: # Before this folders should be made. This will move em.
            shutil.move(dat.path+ex.v+t,dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get()+ex.v+net.tkvar2.get())
        foldP=dat.path+ex.v+net.tkvar.get()+ex.v+net.tkvar3.get()+ex.v+net.tkvar2.get()+ex.v
        glo=1
        for t in newTracks:
            if os.path.isfile(foldP+t):
                aussie=eyed3.load(foldP+t) # Load File.
                genr=net.tkvar.get() # get genre.
                if genr=="Default":
                    pass
                else:
                    aussie.tag.genre=genr
                    aussie.tag.non_std_genre=genr
                artiste=net.tkvar3.get()
                if artiste=='Defaults':
                    pass
                else:
                    aussie.tag.album_artist=artiste
                    aussie.tag.artist=artiste
                    aussie.tag.composer=artiste
                    aussie.tag.original_artist=artiste
                    aussie.tag.publisher=artiste
                    aussie.tag.copyright=artiste
                yr=net.tkvar4.get()
                if str(yr)=='None':
                    yr='2020'
                if yr=='Defaults':
                    pass
                else:
                    aussie.tag.getBestDate =yr
                    aussie.tag.original_release_date =yr
                    aussie.tag.release_date =yr
                    aussie.tag.tagging_date =yr
                aussie.tag.album=net.tkvar2.get()
                aussie.tag.comments.set(str(net.tkvar2.get()))
                if dat.koi:
                    try:
                        for tc in [yk.description for yk in aussie.tag.images]:
                            aussie.tag.images.remove(tc)
                    except:
                        print('Cola Error')
                    imagedata = open(ex.tide+ex.v+'temp-vox.jpg',"rb").read()
                    aussie.tag.images.set(3,imagedata,"image/jpeg")
                aussie.tag.track_num = glo
                glo+=1
                aussie.tag.save()
        if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
            shutil.move(ex.tide+ex.v+'temp-vox-O.jpg',foldP+'cover.jpg')
        if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
            print('Error 7')
            os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
        if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
            os.remove(ex.tide+ex.v+'temp-vox.jpg')
        Update() # Always at End.
    def editor(thevar,textua):
        theOne=thevar
        tex=str(textua)
        # The above only need edited to work with a new one.
        rt = tkinter.Tk()
        w = 610
        h = 60
        ws = rt.winfo_screenwidth()
        hs = rt.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        rt.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rt.resizable(0, 0)
        rt.configure(background=ex.green4)
        rt.title('Manually Configure '+tex)
        red = tkinter.Text(rt,font=('Helvetica', 15),bg=ex.green4,fg='black',insertbackground='gray17')
        red.pack()
        red.place(bordermode=OUTSIDE, height=30, width=610,relx=0.5, rely=0.0, anchor=N)
        red.insert("1.0", theOne.get())
        temp=theOne.get()
        def saveX():
            df=red.get("1.0", END).replace('\n','').replace('\t','')
            if df=='':
                theOne.set(temp)
            else:
                theOne.set(df)
            rt.destroy()
        B = tkinter.Button(rt,text ="Save",command=saveX, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        B.pack()
        B.place(bordermode=OUTSIDE, height=30, width=80,relx=0.5, rely=1.0, anchor=S)
        def saveY():
            red.delete('1.0', END)
        B2 = tkinter.Button(rt,text ="Clear",command=saveY, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        B2.pack()
        B2.place(bordermode=OUTSIDE, height=30, width=80,relx=0.635, rely=1.0, anchor=S)
        def saveZ():
            con=False
            vin=red.get("1.0", END)
            for t in ['\n','\t']:
                if t in vin:
                    con=True
            if con:
                df=vin.replace('\n','').replace('\t','')
            else:
                df=vin
            for t in ['(',')','[',']','<','>','{','}']:
                if t in df:
                    con=True
                    df=df.split(t)[0]
            if df[-1]==' ':
                con=True
                while df[-1]==' ':
                    df=df[:-1]
            if con:
                red.delete('1.0', END)
                red.insert("1.0", df)
        B3 = tkinter.Button(rt,text ="Clean",command=saveZ, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
        B3.pack()
        B3.place(bordermode=OUTSIDE, height=30, width=80,relx=0.365, rely=1.0, anchor=S)
        rt.mainloop()
    def changeCover():
        nest = browseFile()
        if os.path.isfile(nest):
            pass
        else:
            return
        try:
            im = Image.open(nest)
            rgb_im = im.convert('RGB')
            rgb_im.save(ex.tide+ex.v+'temp-vox-O.jpg','JPEG')
            im = Image.open(ex.tide+ex.v+'temp-vox-O.jpg')
            size = ram.ResizeAlbumCoverSize
            im.thumbnail(size, Image.ANTIALIAS)
            rgb_im = im.convert('RGB')
            rgb_im.save(ex.tide+ex.v+'temp-vox.jpg','JPEG')
            dat.koi=True
        except:
            print('Error 2')
            dat.koi=False
            return
        try:
            dat.canva.destroy()
            image = Image.open(ex.tide+ex.v+'temp-vox.jpg')
            size = 218, 218
            image.thumbnail(size,Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            dat.canva=tkinter.Canvas(root,bg=ex.green3, height=218, width=218)
            dat.canva.pack()
            dat.canva.place(bordermode=OUTSIDE,height=218,width=218,relx=0.5,rely=0.1,anchor=N)
            label = Label(dat.canva,image=photo)
            label.image = photo
            label.place(bordermode=OUTSIDE,relx=0,rely=0,width=218,height=218)
            dat.koi=True
        except:
            print('Error 4')
            dat.koi=False
            return
    def genreE():
        editor(net.tkvar,'Genre')
    B = tkinter.Button(root,text ="Edit Genre",command=genreE, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B.pack()
    B.place(bordermode=OUTSIDE, height=30, width=80,relx=0.0, rely=0.15, anchor=W)
    def albumE():
        editor(net.tkvar2,'Album')
    B2 = tkinter.Button(root,text ="Edit Album",command=albumE, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B2.pack()
    B2.place(bordermode=OUTSIDE, height=30, width=80,relx=0.0, rely=0.25, anchor=W)
    def artistE():
        editor(net.tkvar3,'Artist')
    B3 = tkinter.Button(root,text ="Edit Artist",command=artistE, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B3.pack()
    B3.place(bordermode=OUTSIDE, height=30, width=80,relx=0.0, rely=0.35, anchor=W)
    def yearE():
        editor(net.tkvar4,'Year')
    B4 = tkinter.Button(root,text ="Edit Year",command=yearE, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 10, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    B4.pack()
    B4.place(bordermode=OUTSIDE, height=30, width=80,relx=0.0, rely=0.45, anchor=W)
    a = tkinter.Button(root,text =15*'_'+"Next"+'_'*31,command=Next, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=1, anchor=S)
    def Changa():
        dirTree.A=folderPath
        changeCover()
    a1 = tkinter.Button(root,text =19*' '+"Change Cover",command=Changa, anchor='w',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a1.pack()
    a1.place(bordermode=OUTSIDE, height=30, width=310,relx=0.5, rely=0.903, anchor=S)
    a2 = tkinter.Button(root,text ="Skip",command=Update, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a2.pack()
    a2.place(bordermode=OUTSIDE, height=60, width=150,relx=0.0, rely=1.0, anchor=SW)
    def mage():
        dat.merge.append(dat.data[dat.clock-1])
        dat.curMerSize+=1
        af.config(text='Merge One: '+str(dat.curMerSize))
        Update()
    af = tkinter.Button(root,text ="Merge One: ",command=mage, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    af.pack()
    af.place(bordermode=OUTSIDE, height=30, width=150,relx=1.0, rely=1.0, anchor=SE)
    def mage2():
        dat.merge2.append(dat.data[dat.clock-1])
        dat.curMerSize2+=1
        af2.config(text='Merge Two: '+str(dat.curMerSize2))
        Update()
    af2 = tkinter.Button(root,text ="Merge Two: ",command=mage2, anchor='c',bg=ex.darkgreen,fg=ex.white,font=('Helvetica', 13, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    af2.pack()
    af2.place(bordermode=OUTSIDE, height=30, width=150,relx=1.0, rely=0.903, anchor=SE)
    j = Label(root, text='Embedded Art Size',relief=SUNKEN,anchor='center',fg=ex.white,bg=ex.darkgreen,highlightbackground=ex.darkgreen, highlightcolor=ex.darkgreen, highlightthickness=2,font=('Helvetica', 13,'bold'))
    j.place(bordermode=OUTSIDE, height=25, width=195.5,relx=0.0, rely=0.642, anchor=NW)
    j3 = Label(root, text='Renumbering Style',relief=SUNKEN,anchor='center',fg=ex.white,bg=ex.darkgreen,highlightbackground=ex.darkgreen, highlightcolor=ex.darkgreen, highlightthickness=2,font=('Helvetica', 13,'bold'))
    j3.place(bordermode=OUTSIDE, height=25, width=195.5,relx=0.6768, rely=0.642, anchor=NW)
    choices = ['25x25','50x50','75x75','100x100','125x125','150x150','160x160','175x175','200x200','250x250','300x300','350x350','400x400','480x480','500x500','600x600','700x700','800x800','900x900','1000x1000']
    tkvar = StringVar(root)
    def setter(kilo):
        temp=tkvar.get().split('x')
        ram.ResizeAlbumCoverSize=(int(temp[0]),int(temp[1]))
    popupMenu = OptionMenu(root, tkvar, *choices,command=setter)
    popupMenu.config(relief=SUNKEN,fg=ex.white,bg=ex.darkgreen,highlightbackground=ex.darkgreen, highlightcolor=ex.darkgreen, highlightthickness=2,font=('Helvetica', 13,'bold'))
    popupMenu["menu"].config(bg=ex.darkgreen,font=('Helvetica', 13, 'bold'),fg='white')
    popupMenu.place(bordermode=OUTSIDE, height=25, width=195.5,relx=0.0, rely=0.725, anchor=NW)
    tkvar.set(choices[13])
    choices2 = ['01 - Example.mp3','01-Example.mp3','01- Example.mp3','01 Example.mp3','01Example.mp3','01. Example.mp3','01.Example.mp3','01_Example.mp3','01_ Example.mp3','01:Example.mp3','01 : Example.mp3','01)- Example.mp3','01 ~ Example.mp3','01~ Example.mp3','01~Example.mp3']
    tkvar2 = StringVar(root)
    def setter2(kilo):
        if tkvar2.get()==choices2[0]:
            maxx.div=' - '
        elif tkvar2.get()==choices2[1]:
            maxx.div='-'
        elif tkvar2.get()==choices2[2]:
            maxx.div='- '
        elif tkvar2.get()==choices2[3]:
            maxx.div=' '
        elif tkvar2.get()==choices2[4]:
            maxx.div=''
        elif tkvar2.get()==choices2[5]:
            maxx.div='. '
        elif tkvar2.get()==choices2[6]:
            maxx.div='.'
        elif tkvar2.get()==choices2[7]:
            maxx.div='_'
        elif tkvar2.get()==choices2[8]:
            maxx.div='_ '
        elif tkvar2.get()==choices2[9]:
            maxx.div=':'
        elif tkvar2.get()==choices2[10]:
            maxx.div=' : '
        elif tkvar2.get()==choices2[11]:
            maxx.div=')- '
        elif tkvar2.get()==choices2[12]:
            maxx.div=' ~ '
        elif tkvar2.get()==choices2[13]:
            maxx.div='~ '
        elif tkvar2.get()==choices2[14]:
            maxx.div='~'
        else:
            print('Codfish Error')
    popupMenu2 = OptionMenu(root, tkvar2, *choices2,command=setter2)
    popupMenu2.config(relief=SUNKEN,fg=ex.white,bg=ex.darkgreen,highlightbackground=ex.darkgreen, highlightcolor=ex.darkgreen, highlightthickness=2,font=('Helvetica', 13,'bold'))
    popupMenu2["menu"].config(bg=ex.darkgreen,font=('Helvetica', 13, 'bold'),fg='white')
    popupMenu2.place(bordermode=OUTSIDE, height=25, width=195.5,relx=0.6768, rely=0.725, anchor=NW)
    tkvar2.set(choices2[3])
    background_image2=tkinter.PhotoImage(data = ex.vall)
    root.iconphoto(False, background_image2)
    root.mainloop()
class image:
    imageA="""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"""
    imageB="""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"""
ex.vall=image.imageB
def mainCat(indo):
    if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
    if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox.jpg')
    root = tkinter.Tk()
    w = 270
    h = 230
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background=ex.forestgreen)
    if indo == None:
        indo=ex.fold
    root.title(indo)
    def sorter():
        file = browse_button()
        if os.path.isdir(file):
            root.destroy()
            egg="Completed!"
            egg=masterLoop(file)
            mainCat(egg)
        else:
            root.title('Select a Path...')
            return
    background_image=tkinter.PhotoImage(data = image.imageA)
    a = tkinter.Button(root,image=background_image,text ="",command=sorter, anchor='c',bg=ex.forestgreen,fg=ex.white,font=('Helvetica', 16, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=180, width=270,relx=0.5, rely=0.0, anchor=N)
    red = tkinter.Text(root,font=('Helvetica', 14),bg='darkgreen',fg=ex.activeforeground,insertbackground='lime')
    red.pack()
    red.place(bordermode=OUTSIDE, height=25, width=270,relx=0.5, rely=0.775, anchor=N)
    red.insert("1.0", "Type Path Here or Select it.")
    class clue:
        A=True
    def cringe(kl):
        if clue.A:
            clue.A=False
            red.delete('1.0',END)
    red.bind('<Button-1>',cringe)
    red.bind('<Button-2>',cringe)
    red.bind('<Button-3>',cringe)
    def saveX():
        df=red.get("1.0", END).replace('\n','').replace('\t','')
    def credula():
        if clue.A:
            root.title('Enter a Path!')
            sorter()
            return
        df=red.get("1.0", END).replace('\n','').replace('\t','')
        if df.replace(' ','').replace('\n','').replace('\t','')=='':
            sorter()
        else:
            df=df.replace('\n','').replace('\t','').replace('\\',ex.v).replace('/',ex.v)
            if os.path.isdir(df):
                root.destroy()
                egg="Completed!"
                egg=masterLoop(df)
                mainCat(egg)
            else:
                root.title('Invalid Path!')
                return
    ab = tkinter.Button(root,text ="Start Sorting",command=credula, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
    ab.pack()
    ab.place(bordermode=OUTSIDE, height=27, width=135,relx=0.25, rely=1.0, anchor=S)
    def kala():
        root.destroy()
        exit()
    ac = tkinter.Button(root,text ="Exit",command=kala, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
    ac.pack()
    ac.place(bordermode=OUTSIDE, height=27, width=135,relx=0.75, rely=1.0, anchor=S)
    background_image2=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image2)
    root.mainloop()
mainCat('Vintag 1.0')
