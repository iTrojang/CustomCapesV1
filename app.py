from multiprocessing import Process
from flask import *
import os
from sys import platform
from flask import send_file,request as flask_request
from tkinter import filedialog
from dns.resolver import resolve as dns_resolve
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

optifine_ip: str = str(dns_resolve('s.optifine.net', 'A')[0])

app = Flask(__name__)

@app.route("/capes/<username>.png")
def cape(username):
	if os.path.isfile(f"capes/{username}.png"):
		return send_file(f"capes/{username}.png", mimetype='image/gif')
	else: return redirect(f"http://{optifine_ip}/capes/{username}.png")

@app.route("/disable_custom_capes")
def stop_listening():
    func = flask_request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."

def opendir():
    name = entry.get()
    filename = filedialog.askopenfile()
    filename = str(filename.name)
    os.rename(filename,'capes/' + name + '.png')

window_path = r'C:\Windows\System32\drivers\etc\hosts'
linux_path = r'/etc/hosts'
hosts_path = window_path if platform == 'win32' else linux_path

def start_backend(): #wtf is this name lmao
    if str(dns_resolve('s.optifine.net')[0]) != '127.0.0.1': # Don't write multiple times
        with open(hosts_path, "a") as f:
            f.write("127.0.0.1 s.optifine.net\n")  # Redirecting optifine cape server to localhost
    app.run(host='127.0.0.1',port=80)

def pause():
    start_button['text'] = 'Start'
    start_button['command'] = start
    remove_button['state'] = 'normal'
    backend_server.terminate()

def start():
    global backend_server
    start_button['text'] = 'Pause'
    start_button['command'] = pause
    remove_button['state'] = 'disabled'
    backend_server = Process(target=start_backend)
    backend_server.start()
    
def remove_overwrite():
  with open(hosts_path, "r") as f:
      file = str(f.read())
      new_file = file.replace('127.0.0.1 s.optifine.net\n', '') # Remove all records
      with open(hosts_path, "w") as fi:
        fi.write(new_file)
        fi.close()
  remove_button['state'] = 'disabled'

start_button = Button(root,text='Start',font=('Minecraft',16),command=start,bg='#696969')
start_button.grid(row=0,column=2)
remove_button = Button(root,text='Remove',font=('Minecraft',16),command=remove_overwrite,bg='#696969')
remove_button.grid(row=1,column=2)
opencape = Button(root,text='Choose Cape File',font=('Minecraft',16),command=opendir,bg='#696969')
opencape.grid(row=0,column=3)
root.mainloop()
