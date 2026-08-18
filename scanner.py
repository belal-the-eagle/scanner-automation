C = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'end': '\033[0m'  }
import pyfiglet
from colorama import Fore, Style
import subprocess
from alive_progress import alive_bar
import time
def t():
    with alive_bar(100) as bar:
           for i in range(100):
               time.sleep(0.05)
               bar()
def ban():
    banner=pyfiglet.figlet_format("SCANNER AUTOMATION")
    print(f"{C['cyan']}{banner}{C['end']}")
ban()
def whois():
    domain = input("Enter Target Domain💬 :")
    t()
    subprocess.run(["whois", domain])
def nmap():
    ip = input("Enter Target IP - Domain💬 :")
    t()
    subprocess.run(["nmap",ip])
def checktool():
    subprocess.run(["pkg","install","nmap"])
    subprocess.run(["pkg","install","whois"]) 
x=True
while x ==True:
      print(f"{C['bold']}     Scanner Automation  📜{C['end']}")
      print(f"{C['yellow']}1) nmap scanner 🧠")
      print(f"2) whois scanner 🧠") 
      print(f"3) installing requirements ⚒️{C['end']}")
      print("***************************")
      print(f"{C['green']}0) Exit tool 👋{C['end']}")
      choose=input(f"{C['red']} fosciety@root {C['end']}")
      if choose=="1":
         nmap()
         ban()
      elif choose=="0":
           print(f"{C['bold']}exiting ....{C['end']}")
           x =False
      elif choose=="2":
           whois()
           ban()
      elif choose=="3":
           checktool()
           print (f"{C['green']}requirements installed{C['end']}")
           ban()
      else:
          ban()
