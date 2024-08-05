#Mangalyaa
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from PIL import ImageTk,Image
import time
import mysql.connector as mc
import datetime as dt

def homescreen():                         #to create a homescreen
    global cur
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/hsresized.png')
    tk.Label(root,image=bg).pack()
    hs= tk.PhotoImage(file="D:/PROJECT/Images/Homescreen.png")
    button = ttk.Button(root,image=hs,compound=tk.LEFT,command=Login)
    date = dt.datetime.now()
    cur=date.day
    button.place(x=350,y=200)
    root.mainloop()
    
def Login():                                #to create a login page
    def next():  
        def signdatabase():
            cobj=mc.connect(host='localhost',user='root',passwd='root',database='mangalyaa')
            curobj=cobj.cursor()
            if cobj.is_connected():
                password=code.get()
                user1=user.get()
                username=user1+password
                r='show tables'
                curobj.execute(r)
                d=curobj.fetchall()
                c=0
                for i in d:
                    if i[0]==username:
                        Introduction()
                        c+=1
                        break
                if c==0:
                    tk.messagebox.showerror('Invalid','Signup first!')
        def  signup():
            global window,frame,pname,pwd,confirm
            windowsignup=tk.Toplevel()
            windowsignup.title('Me time')
            windowsignup.attributes('-fullscreen',True)
            bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/hsresized.png')
            tk.Label(windowsignup,image=bg).pack()
          
            frame=tk.Frame(windowsignup,bg='Mintcream')
            frame.place(x=500,y=200)

            heading=tk.Label(frame,text='CREATE AN ACCOUNT',font=('Georgia',23,'bold'),bg='white',fg='blue')
            heading.grid(row=0,column=0,padx=10,pady=10)

            pname1=tk.Label(frame,text='Pseudo name',font=('Jokerman',23),bg='white',fg='blue')
            pname1.grid(row=2,column=0,sticky='w',padx=25,pady=(10,0))
            pname=tk.Entry(frame,width=30,font=('Microsoft YaHei UI Light',10,'bold'),relief='solid')
            pname.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
        
            pwd=tk.Label(frame,text='Password',font=('Jokerman',23),bg='white',fg='blue')
            pwd.grid(row=4,column=0,sticky='w',padx=25,pady=(10,0))
            pwd=tk.Entry(frame,width=30,font=('Microsoft YaHei UI Light',10,'bold'),relief='solid',show='*')
            pwd.grid(row=5,column=0,sticky='w',padx=25)
        
            confirm1=tk.Label(frame,text='Confirm password',font=('Jokerman',23),bg='white',fg='blue')
            confirm1.grid(row=6,column=0,sticky='w',padx=25)
            confirm=tk.Entry(frame,width=30,font=('Microsoft YaHei UI Light',10,'bold'),relief='solid',show='*')
            confirm.grid(row=7,column=0,sticky='w',padx=25)

            signup=tk.Button(frame,text='Signup',font=('Georgia',10,'bold'),bd=8,bg='lightblue',activeforeground='blue',relief='sunken',command=signin)
            signup.grid(row=12,column=0,padx=26,sticky='w')
            Next=tk.Button(frame,text='Next',font=('Georgia',10,'bold'),bd=8,bg='lightgreen',activeforeground='purple',relief='sunken',command=next)
            Next.grid(row=12,column=1,padx=25,sticky='w')
            windowsignup.mainloop()
            
        def signin():
            if pname.get()=='' or pwd.get()=='' or confirm.get()=='':
                tk.messagebox.showerror('Error', 'All fields are required')
            elif pwd.get()!=confirm.get():
                tk.messagebox.showerror('Error','Password Mismatched')
            else:
                cobj=mc.connect(host='localhost',user='root',port=3306,passwd='root',database='mangalyaa')
                curobj=cobj.cursor()
            if cobj.is_connected():
                #print('Mysql is connected')
                q='create table {}(Entry varchar(50),curdate int(2))'.format(pname.get()+pwd.get(),cur)
                curobj.execute(q)
                tk.messagebox.showinfo('Connected','YOU ARE NOW A USER')
                
            if not cobj.is_connected():
                tk.messagebox.showerror('Error','Database connectivity issue')
    
        def enter(e):
            user.delete(0, 'end')
        def leave(e):
            n=user.get()
            if n=='':
                user.insert(0,'username')   
        global user,code
        screen=tk.Toplevel()
        screen.title('Login')
        screen.attributes('-fullscreen',True) 
        bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/Background.png')
        tk.Label(screen,image=bg).pack()
        frame=tk.Frame(screen,width=350,height=350,bg="white")
        frame.place(x=580,y=200)
        heading=tk.Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        Name=tk.StringVar()
        user=tk.Entry(frame,width=25,fg='black',border=4,bg='white',textvariable=Name,font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        code=tk.Entry(frame,width=25,fg='black',border=4,bg='white',font=('Microsoft YaHei UI Light',11,),show='*')
        code.place(x=30,y=150)
        code.insert(0,'Password')
        tk.Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',command=signdatabase,border=0).place(x=35,y=204)
        label=tk.Label(frame,text="New to Mangalyaa?",fg='black',bg='white',font=('Jokerman',12))
        label.place(x=55,y=270)
        tk.Button(frame,width=6,text='Sign up',border=2,bg='white',cursor='hand2',fg='#57a1f8',command=signup).place(x=215,y=270)
        screen.mainloop()
        
    def clear():
        pname.delete(0,end)
        pwd.delete(0,end)
        confirm.delete(0,end)
        windowsignup.mainloop()
    next()
    
def Introduction():                              #to create an introduction page
    global window,data
    showinfo(title='WELCOME TO MANGALYAA',message='Wait till you login in to the dashboard!')
    window=tk.Toplevel()
    window.title('User profile')
    window.attributes('-fullscreen',True)
    window.wm_attributes('-transparentcolor', '#ab23ff')
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/f5.png')
    tk.Label(window,image=bg).pack()  
    myfunction()
    window.mainloop()
    
def terminate():                                #to destroy the current page onscreen
    root.destroy()
    
def myfunction():                             #to display contents in the introduction page
    global window,data 
    k='This app helps you look into your life with a New perspective            \n\
With Focus mode , we bring to you the peace-time you require                   \n\
to finish your activity with no distractions from this device, for                  \n\
a set amount of time.                                            \n\
This App also provides another feature - To analyse your mood patterns,      \n\
how they change with time in the form of a graph, by asking specific inputs\n\
periodically and making sure that you will stay poised and find your            \n\
\t\t"Inner Peace" in the Long Run.                                                          \n\
\nYour Well-Being is our Priority :)'
    window.wm_attributes('-transparentcolor', '#ab23ff')
    Intro=tk.Label(window,text=k,font=('Jokerman',18))
    Intro.place(x=300,y=225)
    nextb=tk.Button(window,text="Yes I'm in!",command=Dashboard)
    nextb.place(x=800,y=685)
    backb=tk.Button(window,text="I Quit",command=terminate)
    backb.place(x=700,y=685)
    entry=tk.Label(window,text='Welome to Mangalyaa!',font=('Jokerman',21),height=1)
    entry.place(x=550,y=100)
    window.mainloop()
    
def Dashboard():                          #to create a dashboard with the 'Focus' and 'Mood' buttons
    root=tk.Toplevel()
    root.title("Dashboard")
    root.attributes('-fullscreen', True)
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/2022-01-05 (5).png')
    tk.Label(root,image=bg).pack()
    label=tk.Label(root,text="DASHBOARD",font=("Jokerman",28),width=30,bd=30,fg="black")
    b1 = tk.Button (root, text = "FOCUS",font=("Jokerman",18),width=10,bd=30,fg="blue",bg="MintCream",command=focusscreen)
    b2 = tk.Button (root, text = "MOOD",font=("Jokerman",18),width=10,bd=30,fg="blue",bg="MintCream",command=mood)
    b3=tk.Button (root, text = "Quit",font=("Jokerman",12),width=5,bd=10,fg="blue",bg="MintCream",command=terminate)
    label.place(x=350,y=200)
    b1.place(x=350,y=500)
    b2.place(x=850,y=500)
    b3.place(x=900,y=700)
    root.mainloop()
    
def focusscreen():                       #to create a focus screen window
    def  message():
        def destroy():
            ut.destroy()
        ut=tk.Toplevel()
        ut.geometry("350x150+800+200")
        ut.title("message")
        label=tk.Label(ut,text="Are you sure To QUIT?")
        b1=tk.Button(ut,text="yes",command=Dashboard)
        b2=tk.Button(ut,text="no",command=destroy)
        label.pack()
        b1.pack()
        b2.pack()
    def startCountdown():
        try:
            userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            def eliminate():
                uv.destroy()
            uv=tk.Toplevel()
            uv.geometry("350x250+500+200")
            uv.title("message")
            label=tk.Label(uv,text="Invalid Input")
            b1=tk.Button(uv,text="OK",command=eliminate)
            label.pack()
            b1.pack()
        while userinput >-1:
            mins,secs = divmod(userinput,60)
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            ws.update()
            time.sleep(1)
            if (userinput == 0):
                def eliminate():
                    uv.destroy()
                uv=tk.Toplevel()
                uv.geometry("350x250+500+200")
                uv.title("message")
                label=tk.Label(uv,text="CONGRATS! You have done it.")
                b1=tk.Button(uv,text="OK",command=eliminate)
                label.pack()
                b1.pack()
                focusscreen()
            userinput -= 1
    f=("Arial",50)
    ws =tk.Toplevel()
    ws.geometry("400x250+500+200")
    ws.title("FOCUS TIMER")
    ws.attributes('-fullscreen',True)
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/f4.png')
    tk.Label(ws,image=bg).pack()
    label2=tk.Label(ws,text='Enter the time here',font=('Jokerman',20),fg='black',bg='white')
    label=tk.Label(ws,text='FOCUS TIMER',font=('Jokerman',28),width=20,bd=30,fg='black',bg='white')
    label.place(x=550,y=250)
    label2.place(x=680,y=400)
    hour=tk.StringVar()
    minute=tk.StringVar()
    second=tk.StringVar()
    hour.set("00")
    minute.set("00")
    second.set("00")
    hour_tf= tk.Entry(ws,width=5,font=f,textvariable=hour)
    hour_tf.place(x=650,y=450)
    mins_tf= tk.Entry(ws,width=5,font=f,textvariable=minute)
    mins_tf.place(x=750,y=450)
    sec_tf = tk.Entry(ws,width=3,font=f,textvariable=second)
    sec_tf.place(x=850,y=450)
    label2=tk.Label(ws,text='(hh-mm-ss)',font=('Jokerman',26),fg='black',bg='white')
    label2.place(x=700,y=530)
    start_btn = tk.Button(ws,text='START',bd='20',command= startCountdown)
    start_btn.place(x=450,y=600)
    button=tk.Button(ws,text='EXIT',bd='20',command=message)
    button.place(x=1100,y=600)
    ws.mainloop()
    
def mood():                                         #to create the mood select window and allow user to choose the mood
    global curo,flag
    def initial():
        days=0
        c=0
        return c,days
    
    def on_click(text):
        global k,n,flag,curo
        curo=cur+1
        c,days,flag=check()
        k=text
        if k=='Terrible':
            m="I'm sorry you're feeling glum"
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Terrible.jpg')
            fg='blue'
            n=2
        if k=='Angry':
            m='Oh no, hope your day gets better soon :)'
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Anger.png')
            fg='black'
            n=3
        if k=='Sad':
            m='Everyone has Off days.\nTake good care of yourself today'
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/sadness.png')
            fg='grey'
            n=4
        if k=='Okay':
            m="It's okay to feel Okay :))"
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Okayu.jpg')
            fg='yellow'
            n=5
        if k=='Happy':
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Happy3.jpg')
            fg='orange'
            m="Happy that you're having a good day"
            n=6
        if k=='Joyful':
            m='Excellent! Have a great day!'
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Excited.png')
            fg='Red'
            n=7
        if k=='Amazed':
            m="That's the spirit!\nkeep enjoying the day like this"
            I=ImageTk.PhotoImage(file='D:/PROJECT/Images/Amazedbg.png')
            fg='white'
            n=8

        my_w2=tk.Toplevel()    
        my_w2.attributes('-fullscreen',True)
        my_w2.wm_attributes('-transparentcolor', my_w2['bg'])
        Labelimage=tk.Label(my_window,image=I,bd=180).place(x=290,y=130)
        Labelmsg=tk.Label(my_w2,text=m,font=('Jokerman',25),fg=fg,width=45)
        Labelmsg.place(x=250,y=500)
        w.writerow([days+1,n])
        f.flush()
        if flag%6==0:
            my_w3=tk.Toplevel()
            my_w3.geometry('850x200+400+300')
            Labelfin=tk.Label(my_w3,text='Yay, you have successfully completed '+str(c+1)+' week(s),wanna see your "mood" graph?',font='Jokerman',height=1)
            Labelfin.pack()
            submit=tk.Button(my_w3,text='Show',borderwidth=5,command=lambda:shows(days,c))
            submit.pack()
            back=tk.Button(my_w3,text='Back',borderwidth=5,command=Dashboard)
            back.pack()
            my_w3.mainloop()
        else:
            back=tk.Button(my_window,text='Back',borderwidth=5,command=Dashboard)
            back.place(x=600,y=750)
            submit=tk.Button(my_window,text='Show',borderwidth=5,command=lambda:shows(days,c))
            submit.place(x=800,y=750)
            my_w2.mainloop()

    def shows(days,c):                   
        days,c=days,c
        global my_window,backbutton
        style.use('Solarize_Light2')
        f.seek(0)
        r=csv.reader(f)
        x,y=np.loadtxt('Moodgraph.csv',unpack=True,delimiter=',')
        plt.yticks(np.arange(2,9),['Terrible','Angry','Sad','Okay','Happy','Joyful','Amazed!'],size='large',rotation=15)
        plt.scatter(x,y,s=30) #,cmap=plt.cm.get_cmap('inferno'))
        plt.plot(x,y,'--',color='grey',lw=1.5,label='Mood')
        plt.title('Mood Graph')
        plt.xlabel('Days')
        plt.ylabel('Mood')
        plt.legend(loc='lower left',labels='Week'+str(c),fontsize=5)
        plt.show()
        
    def check():
        global flag
        f=open('Moodgraph.csv','a+',newline='')
        f.seek(0)
        r=csv.reader(f)
        for i in r:
            flag+=1
        w=csv.writer(f)
        if f.tell()==0 :
            c,days=initial()
        else:
            c=f.tell()//35
            f.seek(0)
            r=csv.reader(f)
            for i in r:
                days=int(i[0])
        return c,days,flag
    
    my_window=tk.Toplevel()
    my_window.geometry('1800x1800')
    my_window.title('Mood Graph')
    check()
    k=''
    L=[]
    n=0
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/Backgroundmood.png')
    tk.Label(my_window,image=bg).pack()
    tk.Label(my_window,bd=430).place(x=290,y=130)
    Labeltext=tk.Label(my_window,text='How are you feeling today?',font=('Jokerman',20),height=1,padx=280)
    Labeltext.place(x=260,y=160)
    
    date = dt.datetime.now()
    
    label =tk.Label(my_window, text=f"{date:%A, %B %d, %Y}", font='Jokerman',bg='pink',fg='red')
    label.place(x=290,y=130)
    label=tk.Label(my_window,text='Mood Graph',font='Jokerman',relief='solid',bd=3,height=1,fg='black',padx=10)
    label.place(x=650,y=90)
    
    my_window.attributes('-fullscreen',True)
    
    style.use('Solarize_Light2')
    f=open('Moodgraph.csv','a+',newline='')
    w=csv.writer(f)
    b1=tk.Button(my_window, image=terrible,borderwidth=0,activeforeground='black',command=lambda:on_click('Terrible'),cursor='heart')
    b1.place(x=370,y=250)
    b2=tk.Button(my_window, image=angry,borderwidth=0,activeforeground='white',command=lambda:on_click("Angry"),cursor='heart')
    b2.place(x=500,y=650)
    b3=tk.Button(my_window, image=sad,borderwidth=0,activeforeground='white',command=lambda:on_click("Sad"),cursor='heart')
    b3.place(x=370,y=450)
    b4=tk.Button(my_window, image=okay,borderwidth=0,activeforeground='white',command=lambda:on_click("Okay"),cursor='heart')
    b4.place(x=770,y=650)
    b5=tk.Button(my_window, image=happy,borderwidth=0,activeforeground='white',command=lambda:on_click("Happy"),cursor='heart')
    b5.place(x=950,y=450)
    b6=tk.Button(my_window, image=joyful,borderwidth=0,activeforeground='white',command=lambda:on_click("Joyful"),cursor='heart')
    b6.place(x=950,y=250)
    b7=tk.Button(my_window, image=amazed,borderwidth=0,activeforeground='white',command=lambda:on_click("Amazed"),cursor='heart')
    b7.place(x=650,y=200)
    if curo>cur:
        tk.messagebox.showerror('Reflections Taken!','Come back Tomorrow :)')
        Dashboard() 
    my_window.mainloop()

#--main--
    
root = tk.Tk()                                       # to create a root window
root.title('front screen')
root.attributes('-fullscreen',True)
terrible=ImageTk.PhotoImage(file='D:/PROJECT/Images/Terrible.png')
angry=ImageTk.PhotoImage(file='D:/PROJECT/Images/Angry.png')
sad=ImageTk.PhotoImage(file='D:/PROJECT/Images/Sad.png')
okay=ImageTk.PhotoImage(file='D:/PROJECT/Images/Okay.png')
happy=ImageTk.PhotoImage(file='D:/PROJECT/Images/Happy.png')
joyful=ImageTk.PhotoImage(file='D:/PROJECT/Images/Joyful.png')
amazed=ImageTk.PhotoImage(file='D:/PROJECT/Images/Amazed.png')
flag=0
curo=0
homescreen()






