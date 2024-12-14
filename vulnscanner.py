import nmap
import os 
import time
scanner = nmap.PortScanner()

def menu():
    while True:
        os.system('clear')  

        print("""
$$\    $$\ $$\   $$\ $$\       $$\   $$\        $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$ |   $$ |$$ |  $$ |$$ |      $$$\  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\ 
$$ |   $$ |$$ |  $$ |$$ |      $$$$\ $$ |      $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |
\$$\  $$  |$$ |  $$ |$$ |      $$ $$\$$ |      \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |
 \$$\$$  / $$ |  $$ |$$ |      $$ \$$$$ |       \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$< 
  \$$$  /  $$ |  $$ |$$ |      $$ |\$$$ |      $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |
   \$  /   \$$$$$$  |$$$$$$$$\ $$ | \$$ |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |
    \_/     \______/ \________|\__|  \__|       \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|
        """)
        print("\033[1;33m=====================================================================================================================\033[0m")
        print("\033[0;34m Created by: AlexRods9581\033[0m")
        print("\033[0;34m Github: https://github.com/AlexRodrigues9581\033[0m")
        print("\033[1;33m=====================================================================================================================\033[0m")
        
        op = input('1 - Network Scanner & Host Discovery \n2 - Single Host Port Scanner \n3 - Vulnerability Detector \n4 - Exploit \n5 - Exit\n \nPlease choose an option>')
        
        if op == "1":
            host_discovery()
        
        elif op == "2":
            single_host_scanner()
            
        elif op == "3":
            vulndetector()
            
        elif op == "4":
            os.system('msfconsole')
            
        elif op == "5":
            break
        
        else:
            print("Please select a number between 1 and 5 !")
 
def single_host_scanner():
    print("*************************")
    print("***SINGLE HOST SCANNER***")
    print("*************************")
    
    ip = input("Please enter an IP address to scan:")
    time.sleep(5)
    try:
        scanner.scan(ip, arguments='-sT -T4')

        if ip in scanner.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (ip, scanner[ip].hostname()))
            print('State : %s' % scanner[ip].state())

            for proto in scanner[ip].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)

                lport = list(scanner[ip][proto].keys())
                lport.sort()

                for port in lport:
                    print('Port : %s\tState : %s' % (port, scanner[ip][proto][port]['state']))
        else:
            print(f"Host {ip} is not responding or not found in the scan results.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    back_to_menu()


def vulndetector():
    print("********************************")
    print("*****VULNERABILITY DETECTOR*****")
    print("********************************")
    ip = input("Please enter an IP address to scan:")
    print(os.system('nmap -v --script vuln ' +ip))
    
    back_to_menu()
    
    
def host_discovery():
    print("********************************")
    print("********HOSTS DISCOVERY*********")
    print("********************************")
    host = input("Please enter an IP address of a network to scan (with subnet mask(eg. /24)):")
    scanner.scan(host, arguments='-sT -T4')
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
             
    back_to_menu()
    
            
def back_to_menu():
    while True:
        main_page = input("Go back to the main page? (y/n)> ").lower()
        if main_page in {"y", "yes"}:
            break 
        elif main_page in {"n", "no"}:
            exit

if __name__ == "__main__" :
    menu()
    
    
    
    