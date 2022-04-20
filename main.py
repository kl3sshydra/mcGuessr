import socket
import sys
from os import system, environ, getenv
from platform import platform
from colorama import *
import ctypes
from time import time
import threading
init(autoreset=True)


environ['timer'] = "0"
environ['onlyunique'] = "false"


class mc:
    foundlist = list()
    totalchecks = list()

    def logo(self):
        print("""
 _  _   ___  ___  _  _  ____  ____  ____  ____ 
( \/ ) / __)/ __)/ )( \(  __)/ ___)/ ___)(  _ \\
/ \/ \( (__( (_ \) \/ ( ) _) \___ \\___ \ )   /
\_)(_/ \___)\___/\____/(____)(____/(____/(__\_)

        · minecraft domain resolver ·
              · by kl3sshydra ·

        """)

    def getpossibleparameters(self):
        try:
            if sys.argv[1] == "--unique":
                environ['onlyunique'] = "true"
        except:
            pass
        try:
            if sys.argv[1] == "-h":
                print(f"""Usage: 
python3 {sys.argv[0]} -> shows both unique and already-found ips
python3 {sys.argv[0]} --unique -> shows only unique ips
                """)
                return "quit"
        except:
            pass

    def setconsoletitle(self,text):
        if "windows" in platform().lower():
            ctypes.windll.kernel32.SetConsoleTitleA(text)
        else:
            sys.stdout.write(f"\x1b]2;{text}\x07")

    def clearscreen(self):
        if "windows" in platform().lower():
            system("cls")
        else:
            system("clear")

    def printifdomainexists(self,completedomain):
        exists = mc.doesexist(completedomain)
        mc.totalchecks.append(exists)
        alreadyfound = ""
        if exists not in mc.foundlist:
            mc.foundlist.append(exists)
        else:
            alreadyfound = Fore.YELLOW+Style.DIM

        linecolor = Fore.GREEN+Style.BRIGHT
        if exists == "cannot resolve host":
            linecolor = Fore.RED
            alreadyfound = Fore.RED

        
        if linecolor == Fore.RED:
            return 0
        else:
            if alreadyfound == Fore.YELLOW+Style.DIM:
                if getenv('onlyunique') == "false":
                    print(f"{Style.RESET_ALL}{linecolor}{alreadyfound}{completedomain} -> {exists}")        
            else:
                print(f"{Style.RESET_ALL}{linecolor}{alreadyfound}{completedomain} -> {exists}")
            return 1

    def nosubdomaincheck(self,domain,toplist):
        found = 0
        for sTOP in toplist:
            sTOP = sTOP.strip() 
            onlytopleveldomain = f"{domain}.{sTOP}"
            if mc.printifdomainexists(onlytopleveldomain) == 1:
                found +=1
        return found
    
    def find_sub_and_top(self,sub,toplist,domain):
        found = 0
        
        for sTOP in toplist:
            sTOP = sTOP.strip()
            completedomain = f"{sub}.{domain}.{sTOP}"    
            if mc.printifdomainexists(completedomain) == 1:
                found += 1

        print("all done, found: "+str(found)+(" "*50))
        print("unique ips found: "+str(len(mc.foundlist)-1))
        print("total checks: "+str(len(mc.totalchecks)-1))
        environ['timer'] = str(int(time()) - int(getenv('timer')))
        print("checking opreation took "+getenv('timer')+" seconds")
                
                

    def doesexist(self,domain):
        mc.setconsoletitle(f"mcGuessr - checking '{domain}'")
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return "cannot resolve host"     
        

    def getwordlist(self,path):
        f = open(path,"r")
        content = f.readlines()
        f.close()
        return content

    
    def findtopwithsub(self,sub,toplist,domain):
        mc.find_sub_and_top(sub,toplist,domain)
    
    def main(self):
        mc.clearscreen()
        if mc.getpossibleparameters() == "quit":
            sys.exit()
        mc.logo()
        mc.setconsoletitle("Started mcGuessr by kl3sshydra")
        domain = input("insert domain: ")
        environ['timer'] = str(int(time()))

        wrdlist = input("insert sub domain list: ")
        if wrdlist == "":
            wrdlist = "subdomains.txt"
        tplist = input("insert top-level domain list: ")
        if tplist == "":
            tplist = "toplevels.txt"
        toplist = mc.getwordlist(tplist)
        try:
            threadsnumber = int(input("insert thread number: "))
        except:
            threadsnumber = 20
        threading.Thread(target=mc.nosubdomaincheck, args=(domain,toplist,)).start()
        linenumber = 0
        for x in open(wrdlist,'r').readlines():
            linenumber += 1
        linesperthread = int(linenumber/threadsnumber)
        fp = open(wrdlist)
        linecounter = 0
        for i, line in enumerate(fp):
            line = line.strip()
            linecounter += 1
            if linecounter > linesperthread:
                linecounter = 0
            else:
                threading.Thread(target=mc.findtopwithsub, args=(line,toplist,domain,)).start()


mc = mc()
try:
    mc.main()
except KeyboardInterrupt:
    exit()