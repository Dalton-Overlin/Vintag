class ver:
    sion="2.1" # Version number of program. # ver.sion
"""
##############################
    Vintag.
##############################
    Coded by: Dalton Overlin
##########################################################
    Last Code Revision Date: Jul. 9th, 2020
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
import os, sys, threading, random
def ravage():
    try:
        os._exit(0)
    except:
        print('Kraken Error!')
        sys.exit("Kraken Error!")
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
            ravage()
    else:
        print('Exiting, Goodbye:)')
        ravage()
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
class image:
    imageA="""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"""
    imageB="""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"""
    imageC="""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"""
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
    numb=None
ex.numb=tkinter.Tk()
ex.numb.withdraw()
if "nt" in ex.thisOS: ex.v = "\\"
else: ex.v = "/"
class maxx:
    div=' ' # This can be anything like ' ', ' - ', etc.  maxx.div
def rep(hexa):
    return hexa.replace("/", "_Forward-Slash_").replace("\\", "_Back-Slash_").replace(":", "_Colon_").replace("*", "_Star_").replace("?", "_Question_Mark_").replace("\"", "_Quote-Mark_").replace("'", "_Up_Mark_").replace("<", "_Left-Arrow_").replace(">", "_Right-Arrow_").replace("|", "_Bar_").replace(" ", "_Space_")
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
        victor=rep(temp+t)
        holder.append(victor)
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
class wait:
    root=None
    temp=None
def waiting(folderPath):
    wait.root=None
    wait.temp=folderPath
    wait.root = Toplevel(ex.numb)#tkinter.Tk()
    root=wait.root
    def doMe():
        return
    root.protocol('WM_DELETE_WINDOW', doMe)
    w = 230
    h = 100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background=ex.forestgreen)
    root.title("Scanning...")
    background_image=tkinter.PhotoImage(data = image.imageC)
    a = tkinter.Button(root,text ="", anchor='c',bg=ex.forestgreen,image=background_image,fg=ex.white,font=('Helvetica', 16, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=100, width=230,relx=0.5, rely=0.0, anchor=N)
    background_image2=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image2)
    def gumbo():
        masterLoop(wait.temp)
    root.after(1,gumbo)
    root.mainloop()
class hudu:
    yep=True
def masterLoop(folderPath):
    if hudu.yep:
        hudu.yep=False
        waiting(folderPath)
        return
    else:
        hudu.yep=True
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
            wait.root.destroy()
            mainCat("No Files.")
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
            wait.root.destroy()
            mainCat('No mp3s')
    except:
        wait.root.destroy()
        mainCat('Error 3')
    clock=0
    dat.path=folderPath
    dat.clock,dat.albums,dat.data=clock,albums,data
    #wait.root.destroy()
    root = Toplevel(ex.numb)#tkinter.Tk()
    root.withdraw()
    def doMe():
        try:
            root.destroy()
        except:
            print('Neuro exception')
        mainCat('Exited Early!')
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
        rooty = Toplevel(ex.numb)#tkinter.Tk()
        def doMe4():
            root.destroy()
            rooty.destroy()
            mainCat('Exited Early!')
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
        background_timage2=tkinter.PhotoImage(data = ex.vall)
        rooty.iconphoto(False, background_timage2)
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
                    mainCat('All Done!')
                    return
            else:
                if dat.mergetta:
                    root.destroy()
                    mainCat('All Done!')
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
        rt = Toplevel(ex.numb)#tkinter.Tk()
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
        background_image32=tkinter.PhotoImage(data = ex.vall)
        rt.iconphoto(False, background_image32)
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
    wait.root.destroy()
    root.deiconify()
    root.mainloop()
ex.vall=image.imageB
def mainCat(indo):
    if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
    if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox.jpg')
    root = Toplevel(ex.numb)#tkinter.Tk()
    def doDis():
        root.destroy()
        try:
            ex.numb.destroy()
        except:
            pass
        ravage()
    root.protocol('WM_DELETE_WINDOW', doDis)
    w = 270
    h = 152
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='black')
    if indo == None:
        indo=ex.fold
    root.title(indo)
    def sorter():
        file = browse_button()
        if os.path.isdir(file):
            root.destroy()
            egg=masterLoop(file)
        else:
            root.title('Select a Path...')
            return
    background_image=tkinter.PhotoImage(data = image.imageA)
    a = tkinter.Button(root,image=background_image,text ="",command=sorter, anchor='c',bg='black',fg='black',font=('Helvetica', 16, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=67, width=270,relx=0.5, rely=0.0, anchor=N)
    red = tkinter.Text(root,font=('Helvetica', 14),bg='#fff800',fg='black',insertbackground='black')
    red.pack()
    red.place(bordermode=OUTSIDE, height=25, width=270,relx=0.5, rely=0.435, anchor=N)
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
            df=df.replace('\n','').replace('\t','').replace('\\',ex.v).replace('/',ex.v).replace('"',"").replace("'","").strip()
            if os.path.isdir(df):
                root.destroy()
                egg=masterLoop(df)
            else:
                root.title('Invalid Path!')
                return
    ab3 = tkinter.Button(root,text ="Open Selector",command=sorter, anchor='c',bg="#006100",fg="#fff800",font=('Helvetica', 14, 'bold'),activebackground='#fff800',activeforeground='#006100')
    ab3.pack()
    ab3.place(bordermode=OUTSIDE, height=30, width=270,relx=0.5, rely=0.8, anchor=S)
    ab = tkinter.Button(root,text ="Start",command=credula, anchor='c',bg="#006100",fg="#fff800",font=('Helvetica', 14, 'bold'),activebackground='#fff800',activeforeground='#006100')
    ab.pack()
    ab.place(bordermode=OUTSIDE, height=30, width=135,relx=0.248, rely=1.0, anchor=S)
    ac = tkinter.Button(root,text ="Exit",command=doDis, anchor='c',bg="#006100",fg="#fff800",font=('Helvetica', 14, 'bold'),activebackground='#fff800',activeforeground='#006100')
    ac.pack()
    ac.place(bordermode=OUTSIDE, height=30, width=135,relx=0.748, rely=1.0, anchor=S)
    background_image2=tkinter.PhotoImage(data = image.imageB)
    root.iconphoto(False, background_image2)
    root.mainloop()
def callera():
    mainCat('Vintag '+ver.sion)
ex.numb.after(1,callera)
ex.numb.mainloop()
