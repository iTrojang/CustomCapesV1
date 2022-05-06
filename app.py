import threading
from flask import *
import os
from flask import send_file
from tkinter import filedialog
from tkinter import *

root = Tk()
root.geometry('900x500')
root.configure(bg='#696969')
root.title(string='CustomCapes By iTrojang#7855')
name = Label(text='Enter Player Name: ',font=('Minecraft',16))
name.configure(bg='#696969')
name.grid(row=0,column=0)
entry = Entry(root,font=('Minecraft',16))
entry.grid(row=0,column=1)


app = Flask(__name__)

@app.route("/capes/<username>.png")
def cape(username):
	if os.path.isfile(f"capes/{username}.png"):
		return send_file(f"capes/{username}.png", mimetype='image/gif')
	return('200')

def opendir():
    name = entry.get()
    filename = filedialog.askopenfile()
    filename = str(filename.name)
    os.rename(filename,'capes/' + name + '.png')

def starty(): #wtf is this name lmao
    with open(r'C:\Windows\System32\drivers\etc\hosts', "a") as f:
        f.write("127.0.0.1 s.optifine.net\n")  # Redirecting optifine cape server to localhost
    app.run(host='127.0.0.1',port=80)

def start():
    threading.Thread(target=starty).start()


start = Button(root,text='Start',font=('Minecraft',16),command=start,bg='#696969').grid(row=0,column=2)
opencape = Button(root,text='Choose Cape File',font=('Minecraft',16),command=opendir,bg='#696969').grid(row=0,column=3)

root.mainloop()
