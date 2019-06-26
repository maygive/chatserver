import socket ##use send tcp
import zlib#resize file give small
from tkinter import * #gui
import tkinter 
from tkinter import ttk
from datetime import datetime #put global time 
import tzlocal  # $ pip install tzlocal put global time thai
import os #system
from tkinter import messagebox
import http.server 
import socketserver 
from tkinter.filedialog import askopenfilename #gui choose file
from ftplib import FTP #ftp protocal
global s # variable global
r=["","",""] # keep r[0]=create socket r[1]=server ip r[2]=port server ip
def sys_ip_port(v,p,ser_ip,ser_port):
    
    try:
        host = str(v.get())
        port = int(p.get())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        s.bind((host,port)) #contect server
        r[0]=s
        r[1]=str(ser_ip.get())
        r[2]=str(ser_port.get())
        open_login()
        main.withdraw()
    except:
        messagebox.showerror("Error", "insert Ip Port again!!")
    
main = Tk()
main.title("chat server")
main.geometry("450x150+500+350")
L1 = Label(main, text="client ip")
L1.place(bordermode=OUTSIDE,height = 30,width =60,x=0,y=30 )
v = StringVar(main, value=str(socket.gethostbyname(socket.gethostname())))
E1 = Entry(main, bd =5, textvariable=v)
E1.place(bordermode=OUTSIDE,height = 30,width =100,x=70,y=30)
L1 = Label(main, text="client port")
L1.place(bordermode=OUTSIDE,height = 30,width =60,x=190,y=30 )
p = StringVar()
E1 = Entry(main, bd =5, textvariable=p)
E1.place(bordermode=OUTSIDE,height = 30,width =100,x=260,y=30)



ok = Button(main, text ="OK" ,cursor="hand1",command=lambda:sys_ip_port(v,p,ser_ip,ser_port))
ok.place(bordermode=OUTSIDE,height = 30,width =60,x=380,y=28)
L2 = Label(main, text="server ip")
L2.place(bordermode=OUTSIDE,height = 30,width =60,x=0,y=90 )

ser_ip = StringVar(main, value=str(socket.gethostbyname(socket.gethostname())))
E2 = Entry(main, bd =5, textvariable=ser_ip)
E2.place(bordermode=OUTSIDE,height = 30,width =100,x=70,y=90)
L3 = Label(main, text="server port")
L3.place(bordermode=OUTSIDE,height = 30,width =60,x=190,y=90 )
ser_port = StringVar(main, value=str(5500))
E3 = Entry(main, bd =5, textvariable=ser_port)
E3.place(bordermode=OUTSIDE,height = 30,width =100,x=260,y=90)
x=["","","","",""]
to_user=[""]
label_room=[""]
def open_login ():
    s=r[0]
    print(r[1]+":"+r[2])
    server = (r[1],int(r[2]))
    message = "select user,password from account"
    s.sendto(message.encode('utf-8'), server)#client send to server by encode in order to byte
      
    data, addr = s.recvfrom(1024) #determine recived data <1024 , if send over ,it will send 2 data of series
    print(addr[0],addr[1])#addr[0]=server ip ,addr[1]=server port 
    uncmpstr = zlib.decompress(data) 
    data=uncmpstr.decode("utf-8")
    print(data)##recived user:pass from server
    account = list(data.split("\n")) ##user:pass
    if("" in account):
        account.remove("")
    my_window = Toplevel()
    my_window.title("Login chat")
    my_window.geometry("300x500+600+150")
    password = StringVar()
    lo1 = Label(my_window, text="Login")
    lo1.place(bordermode=OUTSIDE,height = 30,width =60,x=100,y=50)

    regis = tkinter.Button(my_window, text ="Register" ,cursor="hand1",command=lambda: register(my_window,account,s,server))
    regis.place(bordermode=OUTSIDE,height = 30,width =60,x=160,y=400)

    lo = Label(my_window, text="Username")
    lo.place(bordermode=OUTSIDE,height = 30,width =60,x=20,y=150)

    user=Text(my_window, height=7, width=35)
    user.place(bordermode=OUTSIDE,height = 20,width =140,x=100,y=150)

    passw = Label(my_window, text="Password")
    passw.place(bordermode=OUTSIDE,height = 30,width =60,x=20,y=200)

    passEntry = Entry(my_window, textvariable=password, show='*')
    passEntry.place(bordermode=OUTSIDE,height = 20,width =140,x=100,y=200)
    login = tkinter.Button(my_window, text ="Login" ,cursor="hand1",command=lambda: sys_login(my_window,account,user,password,s,addr[0],addr[1],server))
    login.place(bordermode=OUTSIDE,height = 30,width =60,x=80,y=400)

def sys_login(my_window,account,user,password,s,host,port,server):
    check=0
    print(account)
    inputValue=user.get("1.0","end-1c")

    inputValue2=password.get()
    Username=[]
    Password=[]
    print("sssssssssssss"+str(inputValue+inputValue2))
    print(str(inputValue2))
    if (inputValue=="" or inputValue2==""):
            messagebox.showwarning("Warning","Have blank!")
            check=1
    else:  
        for i in account:
            Username,Password=i.split(":")
            print(Username,Password)
            if(Username == inputValue and Password == inputValue2):
                print("EE")
                check=1
                my_window.destroy()
                chat(inputValue,s,host,port,server)
##              os.system("cn1.py "+inputValue)
    if (check==0):
        messagebox.showwarning("No member","Please sign in now")
        
    
    #textBox2.insert(END,inputValue+"\n")
    #textBox2.setText(inputValue)
##    textBox2.insert(END,inputValue+"\n")
##    textBox.delete('1.0', END)
##    message=(inputValue)
##    s.sendto(message.encode('utf-8'), server)
def register(my_window,account,s,server):
    my_window.withdraw()
    
    newpassword = StringVar()
    newpassword1 = StringVar()
    top = Tk()
    top.title("Register chat")
    top.geometry("300x500+600+150")

    lo1 = Label(top, text="Username")
    lo1.place(bordermode=OUTSIDE,height = 30,width =60,x=20,y=100)
    user1=Text(top, height=7, width=35)
    user1.place(bordermode=OUTSIDE,height = 20,width =140,x=100,y=100)

    passw1 = Label(top, text="Password")
    passw1.place(bordermode=OUTSIDE,height = 30,width =60,x=20,y=150)
    
    passEntry1 = Entry(top, textvariable=newpassword, show='*')
    passEntry1.place(bordermode=OUTSIDE,height = 20,width =140,x=100,y=150)
    
    passw2 = Label(top, text="Re-Password")
    passw2.place(bordermode=OUTSIDE,height = 30,width =70,x=20,y=200)
    
    passEntry2 = Entry(top, textvariable=newpassword1, show='*')
    passEntry2.place(bordermode=OUTSIDE,height = 20,width =140,x=100,y=200)

    
    login1 = tkinter.Button(top, text ="Back" ,cursor="hand1",command =lambda: backlogin(top,my_window))
    login1.place(bordermode=OUTSIDE,height = 30,width =60,x=80,y=400)
    
    
    regis2 = tkinter.Button(top, text ="Register" ,cursor="hand1",command=lambda: sys_regis(my_window,user1.get("1.0","end-1c"),passEntry1.get(),passEntry2.get(),top,account,s,server))
    regis2.place(bordermode=OUTSIDE,height = 30,width =60,x=160,y=400)

def sys_regis(my_window,user,newpassword1,newpassword,top,account,s,server):
    
    Username=[]
    print(account)
    for i in account:
        Username.append(i.split(":")[0])
    print(Username)
        
    if (newpassword=="" or newpassword1=="" or user==""):
        messagebox.showwarning("Warning","Have blank!")
    elif(newpassword!=newpassword1):
        err_pass()
    elif(newpassword==newpassword1 and user!="" and user not in Username and newpassword!="" and newpassword1!=""):
        message = "INSERT INTO account (user,password,status) VALUES ('%s', '%s', '%s');"%(user,newpassword,"N")
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        uncmpstr = zlib.decompress(data)
        data=uncmpstr.decode("utf-8")
        print(data)
        account.append(user+":"+newpassword)
        popupsu()
        top.withdraw()
        my_window.deiconify()
    else :
        user_used()

def chat(user,s,host,port,server):
    message = 'UPDATE account SET status="Y" WHERE user="{0}"'.format(user)
    s.sendto(message.encode('utf-8'), server)
      
    data, addr = s.recvfrom(1024)
    print(addr[0],addr[1])  
    uncmpstr = zlib.decompress(data)
    data=uncmpstr.decode("utf-8")
    print(data)

    root=Tk()
    
    root.geometry("500x500+550+100")
    root.title(user+"@"+host)
    Label2 = Label(root,text =user,fg="black")
    label_room[0]=Label2
    Label2.place(bordermode=OUTSIDE,x=140,y=10)
    Label1 = Label(root,text = "◆ online",fg="green").place(bordermode=OUTSIDE,height = 30,width =50,x=235,y=10)
    print("xx")
    textBox2=Text(root, height=13, width=35)
    textBox2.place(bordermode=OUTSIDE,height = 280,width =260,x=20,y=40)
##    Label2 = Label(root,text = "",fg="blue").pack()
    textBox=Text(root, height=7, width=35)   #pim message in textbox
    textBox.place(bordermode=OUTSIDE,height = 30,width =260,x=20,y=360)
    buttonCommit=Button(root, height=1, width=10, text="Send", 
                        command=lambda: showchat(user,to_user[0],textBox,textBox2,s,server))
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.place(bordermode=OUTSIDE,height = 30,width =50,x=100,y=410)

    button_file=Button(root, height=1, width=1, text="Browse", 
                        command=lambda: showfile())
    button_file.place(bordermode=OUTSIDE,height = 20,width =50,x=230,y=340)

    x[0]=root
    x[1]=s
    x[2]=user
    x[3]=textBox2
    x[4]=server #(serverip,serverport)
    setListBox()
    setTextBox()
def placeFile(filename):
    ftp = FTP(str(r[1]))
    ftp.login(user='bewwy', passwd = 'bewwy')
    ftp.cwd('FTP') ##take file in folder FTP
    data = str(list(filename.split("/"))[-1])#filename
    print(data)
    ftp.storbinary('STOR '+data, open(filename, 'rb'))##open file client to server folder name FTP
    ftp.quit()

    
    
def grabFile(filename):#ftp default port22
    ftp = FTP(str(r[1]))
    ftp.login(user='bewwy', passwd = 'bewwy')
    ftp.cwd('FTP')
    data = str(list(filename.split("/"))[-1])
    
    print(data)
    
    ftp.retrbinary("RETR " + data, open(data, 'wb').write)

    ftp.quit()
        
def showfile():
    
    print("")
    s=x[1]
    user=x[2]
    tuser = to_user[0]
    server = x[4]
    
    send=Toplevel()
    #send.geometry("500x500+550+100")
    #ok = Button(send, text ="OK" ,cursor="hand1",command=lambda:send.destroy())
    #ok.place(bordermode=OUTSIDE,height = 30,width =60,x=380,y=28)


    #host=socket.gethostbyname(socket.gethostname())
    send.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)## address file/namefile
    placeFile(filename)##sent file
    data = str(list(filename.split("/"))[-1]) #namefile
    
    #host=socket.gethostbyname(socket.gethostname())
    #port=50000
##    datasend=str(host)+","+str(port)+","+data
    print(data)
    if(tuser!=""):
        date,timez=time()
        message = "INSERT INTO server (user,to_user, message, date, time) VALUES ('%s', '%s', '%s', DATE('%s'), TIME('%s'));"%(user,tuser,"SENDFILE=>"+data,date,timez)
        print(message)
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
         
        uncmpstr = zlib.decompress(data)
        data=uncmpstr.decode("utf-8")
        print(data)


chack=[""]
   
def setTextBox():
    root=x[0]
    s=x[1]
    user=x[2]
    textBox2=x[3]
    server=x[4]
    tuser = to_user[0]
    oldfile=chack[0]
    message = 'select user,message from server where ((user = "{0}" and to_user = "{1}") or (user = "{2}" and to_user = "{3}"))'.format(user,tuser,tuser,user)
    s.sendto(message.encode('utf-8'), server)
    root.after(1000,setTextBox)
  
    data, addr = s.recvfrom(1024)
      
    uncmpstr = zlib.decompress(data)
    data=uncmpstr.decode("utf-8")
##    SENDFILE
    try:
        mess = str(list(data.split("\n"))[-2])
        print("xxxxxxxxxxxxxx"+mess)
        nameuser = str(list(mess.split(":"))[0])
        namefile  =str(list(str(list(mess.split(":"))[1]).split("=>"))[1])
        if(nameuser.upper() == tuser.upper() and oldfile!=namefile):##check user-send == to_user and is not oldfile
            chack[0]=namefile
            print(nameuser,namefile)
            MsgBox = messagebox.askquestion ('File accept','Are you sure you accept file',icon = 'warning')
            if MsgBox == 'yes':
               
               grabFile(namefile)##recived file
         
    except:
        pass
        
    
##    try:
##        html = str(list(data.split("\n"))[-2])
##        text=""
##        user = user.upper()
##        tuser = tuser.upper()
##        name=""
##        for i in html:
##            text+=i
##
##            if(text.upper()==user or text.upper() ==tuser):
##                name=text
##                text=""
##        print("name : "+name)       
##      
##        
##        
##    ##    print(name,html)
##    ##    print("qwqeweqe"+str(list(html.split(":"))[0]))
##        if(name.upper()==tuser.upper() and text[1:][0:5].upper() == "http:".upper() and html.upper() !=chack[0].upper()):
##            print("Download",html,chack[0])
##            chack[0]=html
##            
####        if(html.upper() ==chack[0].upper()):
####            chack[0]=""
##    except:
##        pass
    textBox2.delete('1.0', END)
    textBox2.insert(END,data)
    textBox2.see(END)
    
def setListBox():
    root=x[0]
    s=x[1]
    user=x[2]
    server=x[4]
    l=Listbox(root,width=30,height=21,selectmode=SINGLE,selectbackground="blue")
    
##    l.insert(1,"REE")
##    l.insert(2,"gGG")
    
       
    message = 'select user,password from account where status="Y"'
    s.sendto(message.encode('utf-8'), server)
    root.after(1000,setListBox)
      
   
  
    data, addr = s.recvfrom(1024)
      
    uncmpstr = zlib.decompress(data)
    data=uncmpstr.decode("utf-8")
   
    account = list(data.split("\n"))
    if("" in account):
        account.remove("")
   
    User=[]
    for i in account:
        Username,Password=i.split(":")
        print(Username,Password)
        User.append(Username)
   
    for i in range(len(User)):
        if(User[i]!=user):
            l.insert(i+1,User[i])
   
    l.bind('<<ListboxSelect>>',onselect)
    
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    l.place(bordermode=OUTSIDE,x=300,y=40)
    

   
    
def showchat(user,to_user,textBox,textBox2,s,server):
    print(to_user)
    inputValue=textBox.get("1.0","end-1c") #chat big
    print(inputValue)
    inputValue2=textBox2.get("1.0","end-1c")
    print(inputValue2)
    #textBox2.insert(END,inputValue+"\n")
    #textBox2.setText(inputValue)
   
    textBox.delete('1.0', END)
    message=(inputValue)
    if(message.upper()!="SELECT * FROM SERVER" and message.upper()!="DELETE FROM SERVER" and to_user!=""):
        date,timez=time() 
        message = "INSERT INTO server (user,to_user, message, date, time) VALUES ('%s', '%s', '%s', DATE('%s'), TIME('%s'));"%(user,to_user,message,date,timez)
    s.sendto(message.encode('utf-8'), server)

    data, addr = s.recvfrom(1024)
    uncmpstr = zlib.decompress(data)
    data=uncmpstr.decode("utf-8")
    print(data)

def time(): #return date time
    local_timezone = tzlocal.get_localzone()
    aware_dt = datetime.now(local_timezone)
    x=list(str(aware_dt).split())
    return str(x[0]),str(x[1][:8])




    

def checkmsg(s):
    
    data, addr = s.recvfrom(1024)
    data=data.decode("utf-8")
    print("["+addr[0]+"]" ,"Send : ",data )
def onselect(evt):
    try:
    # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
       
        to_user[0] = value
        label_room[0]["text"] = "Room : "+value
        print ('You selected item %d: "%s"' % (index, value))
    except:
        print("select error")

def on_closing():
    root=x[0]
    s=x[1]
    user=x[2]
    server=x[4]
    print("xx")
    message = 'UPDATE account SET status="N" WHERE user="{0}"'.format(user)
    s.sendto(message.encode('utf-8'), server)
      
    data, addr = s.recvfrom(1024)
    print(addr[0],addr[1])  
    uncmpstr = zlib.decompress(data)
    data=uncmpstr.decode("utf-8")
    print(data)
    root.after(1500, lambda: root.destroy()) 
    root.withdraw()

    
def err_pass():
    messagebox.showerror("Error", "Error diferrent!")
def popupsu():
    messagebox.showinfo("Password", "Success")
def user_used():
    messagebox.showerror("User", "User is used!")

    
def backlogin(top,my_window):
    top.withdraw()
    my_window.deiconify()

##class StoppableRPCServer(SimpleXMLRPCServer.SimpleXMLRPCServer):
##    def serve_forever(self):
##            while not self.stopped:
##                self.handle_request()
##
##    def not_forever(self):
##        # Called from another function when a custom header is detected
##        self.stopped = True
##        self.server_close()
main.mainloop()
