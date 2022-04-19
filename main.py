import socket
from os import system
from platform import platform
from colorama import *
init(autoreset=True)

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


    def clearscreen(self):
        if "windows" in platform():
            system("cls")
        else:
            system("clear")

    
    def find_sub_and_top(self,sublist,toplist,domain):
        for sSUB in sublist:
            sSUB = sSUB.strip()
            for sTOP in toplist:
                sTOP = sTOP.strip()
                completedomain = f"{sSUB}.{domain}.{sTOP}"
                exists = mc.doesexist(completedomain)
                linecolor = Fore.GREEN
                if exists == "cannot resolve host":
                    linecolor = Fore.RED
                print(f"{linecolor}{completedomain} -> {exists}")

    def doesexist(self,domain):
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
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
        mc.find_sub_and_top(mc.getwordlist("subdomains.txt"),mc.getwordlist("toplevels.txt"),domain)

mc = mc()
try:
    mc.main()
except Exception as e:
    print("ERROR: "+str(e))