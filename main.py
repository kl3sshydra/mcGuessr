import socket, sys
from os import system, environ, getenv
from platform import platform
from colorama import *
from timeout import *
from time import time
init(autoreset=True)


environ['timer'] = "0"


class mc:
    def logo(self):
        print("""
 _  _   ___  ___  _  _  ____  ____  ____  ____ 
( \/ ) / __)/ __)/ )( \(  __)/ ___)/ ___)(  _ \\
/ \/ \( (__( (_ \) \/ ( ) _) \___ \\___ \ )   /
\_)(_/ \___)\___/\____/(____)(____/(____/(__\_)

        · minecraft domain resolver ·
              · by kl3sshydra ·

        """)

    def getprintnotfoundmode(self):
        try:
            return sys.argv[1] == "--print-not-found"
        except:
            return False


    def clearscreen(self):
        if "windows" in platform():
            system("cls")
        else:
            system("clear")

    def printifdomainexists(self,completedomain):
        exists = mc.doesexist(completedomain)
        linecolor = Fore.GREEN
        if exists == "cannot resolve host":
            linecolor = Fore.RED
        if linecolor == Fore.RED:
            if mc.getprintnotfoundmode() == False:
                print(f"{linecolor}{completedomain} -> {exists}"+(" "*20), end="\r")
            else:
                print(f"{linecolor}{completedomain} -> {exists}")
            return 0
        else:
            if mc.getprintnotfoundmode() == False:
                print(f"{linecolor}{completedomain} -> {exists}"+(" "*20))
            else:
                print(f"{linecolor}{completedomain} -> {exists}")
            return 1

    
    def find_sub_and_top(self,sublist,toplist,domain):
        found = 0

        for sTOP in toplist:
            sTOP = sTOP.strip() 
            onlytopleveldomain = f"{domain}.{sTOP}"
            if mc.printifdomainexists(onlytopleveldomain) == 1:
                found += 1

        for sSUB in sublist:
            sSUB = sSUB.strip()
            for sTOP in toplist:
                sTOP = sTOP.strip()
                completedomain = f"{sSUB}.{domain}.{sTOP}"    
                if mc.printifdomainexists(completedomain) == 1:
                    found += 1

        print("all done, found: "+str(found)+(" "*50))
        environ['timer'] = str(int(time()) - int(getenv('timer')))
        print("checking opreation took "+getenv('timer')+" seconds")
                
                

    def doesexist(self,domain):
        try:
            with raise_on_timeout(0.5):
                return socket.gethostbyname(domain)
        except OSError:
            return "cannot resolve host"     
        

    def getwordlist(self,path):
        f = open(path,"r")
        content = f.readlines()
        f.close()
        return content
    
    def main(self):
        mc.clearscreen()
        mc.logo()
        domain = input("insert domain: ")
        environ['timer'] = str(int(time()))
        mc.find_sub_and_top(mc.getwordlist("subdomains.txt"),mc.getwordlist("toplevels.txt"),domain)

mc = mc()
try:
    mc.main()
except KeyboardInterrupt:
    exit()