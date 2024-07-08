import nmap
import os 
import time
scanner = nmap.PortScanner()

print(r"""
$$\    $$\ $$\   $$\ $$\       $$\   $$\        $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$ |   $$ |$$ |  $$ |$$ |      $$$\  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\ 
$$ |   $$ |$$ |  $$ |$$ |      $$$$\ $$ |      $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |
\$$\  $$  |$$ |  $$ |$$ |      $$ $$\$$ |      \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |
 \$$\$$  / $$ |  $$ |$$ |      $$ \$$$$ |       \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$< 
  \$$$  /  $$ |  $$ |$$ |      $$ |\$$$ |      $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |
   \$  /   \$$$$$$  |$$$$$$$$\ $$ | \$$ |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |
    \_/     \______/ \________|\__|  \__|       \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|
""")
print("\033[1;33m ================================================================================================== \033[1;33m")
print('''\033[0;34m Created by: AlexRods9581''')
print('''\033[0;34m Github: https://github.com/AlexRodrigues9581''')
print("\033[1;33m ================================================================================================== \033[1;33m")

def menu():
    
    op = input('1 - Network Scanner & Host Discovery \n2 - Single Host Scanner \n3 - Vulnerability Detector \n4 - Search for the exploits \n5 - Exit\n \nPlease choose an option:')
    
    
    if op == "1":
        host_discovery()
    
    if op == "2":
        nscanner()
        
    if op == "3":
        vulndetector()
        
    if op == "4":
        exploits()
        
    if op == "5":
        exit 
 
def nscanner():
    print("*************************")
    print("***SINGLE HOST SCANNER***")
    print("*************************")
    
    ip = input("Please enter an IP address to scan:")
    print("I will scan this IP and show you the open ports !")
    print("Please wait...")
    scanner.scan(ip,'1-1024')
    print(scanner.scaninfo())
    print(scanner[ip]['tcp'].keys())


def vulndetector():
    print("********************************")
    print("*****VULNERABILITY DETECTOR*****")
    print("********************************")
    ip = input("Please enter an IP address to scan:")
    print(os.system('nmap -sV --script vuln ' +ip))
    
def host_discovery():
    print("********************************")
    print("********HOSTS DISCOVERY*********")
    print("********************************")
    host = input("Please enter an IP address of a network to scan (with subnet mask(eg. /24)):")
    scanner.scan(host, arguments='-sT')
    for host in scanner.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, scanner[host].hostname()))
     print('State : %s' % scanner[host].state())
     for proto in scanner[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)

         lport = scanner[host][proto].keys()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))
             
def exploits():
    print("I WILL OPEN MSFCONSOLE AND YOU WILL SEARCH FOR THE RIGHT EXPLOITS ! ")
    print("Please wait...")
    time.sleep(5)
    os.system('clear')
    os.system('msfconsole')

if __name__ == "__main__" :
    menu()
    
    
    
    