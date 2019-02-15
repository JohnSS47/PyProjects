import ctypes
import getpass
from os import listdir
def run():
    IDCLOSED = 0
    
    while(IDCLOSED is not 1):
        ctypes.windll.user32.MessageBoxW(0,"Welcome!","Press OK to continue",1)
        ctypes.windll.user32.MessageBoxW(0,"To your doom!","Sorry you cannot exit :'(",1)
        ctypes.windll.user32.MessageBoxW(0,"This program will delete all of your files on the system. Continue?" ,"Preparing...", 0)
        for f in listdir("C:\\Windows"):
            print("Deleting " + f + "...")
        print("C:\\Users\\" + getpass.getuser()+">" )
        ctypes.windll.user32.MessageBoxW(0,"HAHAHAHA","Boom your files are gone!",1)
        ctypes.windll.user32.MessageBoxW(0,"We're no strangers to love","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"You know the rules and so do I","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"A full commitment's what I'm thinking of","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"You wouldn't get this from any other guy","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"I just wanna tell you how I'm feeling","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"Gotta make you understand","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"NEVER GONNA GIVE YOU UP","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"NEVER GONNA LET YOU DOWN","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"Never gonna run around and desert you","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"Never gonna make you cry","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"Never gonna say goodbye","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"Never gonna tell a lie and hurt you..","You got rick-rolled!",1)
        ctypes.windll.user32.MessageBoxW(0,"K. Bye :)","You got rick-rolled!",1)
        IDCLOSED=1
        
run()
