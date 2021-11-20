from tkinter import *;
from gtts import gTTS;
from playsound import playsound;
from tkinter import ttk;
import mysql.connector;
from PIL import Image,ImageTk;
from tkinter import messagebox

def loginf():
    global uname;
    global passw;
    global main_frame;
    main_frame = Tk();
    main_frame.geometry("700x330");
    main_frame.title("Login Form");
    m = Menu(main_frame);
    m1 = Menu(m,tearoff = 0);
    m.add_cascade(label = "File",menu = m1);
    m1.add_command(label = "Register",command = regf);
    main_frame.config(menu = m);
    Label(main_frame,text = "Admin Login",justify = "center",font = ("helvetica",35,"bold"),fg = "Red",bg = "pink",width = 300).pack();
    
    bg = Image.open("login.jpg").resize((700,330));
    img = ImageTk.PhotoImage(bg,master = main_frame);
    lbl = Label(main_frame,image = img).pack(pady = 0.5);
    username_label = Label(main_frame,text = "UserName - ",font = ("helvetica",20,"bold"),bg = "white",fg = "Green").place(x = 40,y =90);
    password_label = Label(main_frame,text = "Password - ",font = ("helvetica",20,"bold"),bg = "white",fg = "Green").place(x = 40,y =140);
    uname = Entry(main_frame,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    uname.place(x = 275,y = 100);
    passw = Entry(main_frame,width = 50,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    passw.place(x = 275,y = 150);
    loginButt = Button(main_frame,text = "Login",font = ("helvetica",15,"bold"),command = CredentialCheck,fg = "Green",bg = "White",width = 10).place(x = 130,y = 214);
    clearButt = Button(main_frame,text = "Clear",font = ("helvetica",15,"bold"),command = Clear_F1,fg = "Green",bg = "White",width = 10).place(x = 278 ,y = 214);
    exitButt =  Button(main_frame, text = "Exit",font = ("helvetica",15,"bold"),fg = "Green",bg = "White",command =main_frame.destroy,width = 10).place(x = 425,y = 214);
    main_frame.mainloop();

def CredentialCheck():
    userna = uname.get();
    pas = passw.get();
    if userna == "" or pas == "":
        messagebox.showinfo("Alert","Please Fill the Username and Password");
    else:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "texttospeech");
        mycur=mydb.cursor()
        sql = ("select * from cred_check where USERNAME =%s and PASSWORD =%s ");
        val = (userna,pas);
        mycur.execute(sql, val);
        result = mycur.fetchall()
        if result:
            messagebox.showinfo("","Welcome Text to speech Interface 🎉 ");
            main_frame.destroy();
            mainf();
            
        else:
            messagebox.showinfo("","Sorry Try Again 😔 ");

def Clear_F1():
   uname.delete(0, END);
   passw.delete(0,END);


def regf():
    global fentry1;
    global lentry2;
    global emailentry3;
    global uentry4;
    global pentry5;
    global cpentry6;
    global rframe;
    rframe =  Tk();
    rframe.title("Registration Form");
    rframe.geometry("700x600");
    Label(rframe,text = "Registration Form",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",width = 300).pack();
    bg = Image.open("new.jpg").resize((700,600));
    img = ImageTk.PhotoImage(bg);
    lbl = Label(main_frame,image = img).pack(pady = 0.5);
    fname = Label(rframe,text = "FirstName",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 160,y =90);
    lname = Label(rframe,text = "LastName",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 400,y =90);
    fentry1 =Entry(rframe,width = 20,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    fentry1.place(x = 144,y = 140);
    lentry2 =Entry(rframe,width = 20,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    lentry2.place(x = 387,y = 140);
    Email = Label(rframe,text = "Email ID",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 160,y =180);
    emailentry3 = Entry(rframe,width = 51,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    emailentry3.place(x = 140,y = 230);
    uname = Label(rframe,text = "Username",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 160,y =270);
    uentry4 = Entry(rframe,width = 51,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    uentry4.place(x = 140,y = 310);
    p = Label(rframe,text = "Password",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 160,y =350);
    pentry5 = Entry(rframe,width = 51,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    pentry5.place(x = 140,y = 390);
    cp = Label(rframe,text = "Confirm Password",font = ("Ink Free",20,"bold"),bg = "white",fg = "green").place(x = 160,y =430);
    cpentry6 = Entry(rframe,width = 51,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    cpentry6.place(x = 140,y = 470);
    registerButt = Button(rframe,text = "Register",font = ("helvetica",15),fg = "green",bg = "white",width = 10,command = Register).place(x = 60,y = 520);
    clearButt = Button(rframe,text = "Clear",font = ("helvetica",15),fg = "green",bg = "white",width = 10,command = ClearRegForm).place(x = 205 ,y = 520);
    backButt = Button(rframe,text = "Back",font = ("helvetica",15),fg = "green",bg = "white",width = 10,command =  backRegForm).place(x = 350 ,y = 520);
    exitButt =  Button(rframe, text = "Exit",font = ("helvetica",15),fg = "green",bg = "white",command = rframe.destroy,width = 10).place(x = 495,y = 520);
    rframe.mainloop();





def backRegForm():
    rframe.destroy();
    loginf();

    
def regtologmenu():
    main_frame.destroy();
    regf();


def  ClearRegForm():
    fentry1.delete(0,END);
    lentry2.delete(0,END);
    emailentry3.delete(0,END);
    uentry4.delete(0,END);
    pentry5.delete(0,END);
    cpentry6.delete(0,END);

def Register():
    fn = fentry1.get();
    ln = lentry2.get();
    ei = emailentry3.get();
    un = uentry4.get();
    p = pentry5.get();
    cp = cpentry6.get();

    if p != cp:
        messagebox.showinfo("","Password doesn't match");
        
    else:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "texttospeech");
        mycur = mydb.cursor();
        mycur.execute("CREATE TABLE IF NOT EXISTS cred_check(First_Name varchar(40),Last_Name varchar(30),Email_ID varchar(40),UserName varchar(40),Password varchar(46))");
        val= [(fn,ln,ei,un,cp)];
        sql="INSERT INTO cred_check(First_Name,Last_Name,Email_ID,UserName,Password)VALUES (%s,%s,%s,%s,%s)";
        mycur.executemany(sql,val);
        mydb.commit();
        messagebox.showinfo("","You have been successfully Registered , Thank you ");
        ClearRegForm()


def mainf():
    root = Tk();
    root.geometry("350x300") ;
    
    root.title("DataFlair - TEXT TO SPEECH");
    bg = Image.open("text.jpeg").resize((350,300));
    img = ImageTk.PhotoImage(bg);
    lbl = Label(root,image = img).place(x = 0,y = 0);
    Label(root, text = "Text To Speech", font = "helvetica 25 bold",fg = "red",bg = "black").pack(pady = 10);
    Msg = StringVar();
    Label(root,text ="Enter Text", font = 'helvetica 20 bold',fg = "green",bg = "black").pack(pady = 10);
    entry_field = Entry(root, textvariable = Msg ,width ='20',font = "helvetica 20 bold");
    entry_field.place(x=20,y=130);
    def Text_to_speech():
        Message = entry_field.get();
        speech = gTTS(text = Message);
        speech.save('DataFlair.mp3');
        playsound('DataFlair.mp3');
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "texttospeech");
        mycur = mydb.cursor();
        mycur.execute("insert into search_hist(Searched_text) values('"+Message+"')");
        mydb.commit();
    def Exit():
        root.destroy();
    def Reset():
        Msg.set("");
    Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4',fg = "green").place(x=25,y=200);
    Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, fg = "green").place(x=120 , y = 200);
    Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset,fg = "green").place(x=215 , y = 200);
    root.mainloop();


loginf();
