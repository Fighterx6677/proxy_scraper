import requests
import colorama
import os
import time

colorama.init()
os.system('cls')

print("""

 \u001b[34m.██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗  ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
 \u001b[34m.██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 \u001b[34m.██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░  ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
 \u001b[34m.██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░  ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
 \u001b[34m.██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░  ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
 \u001b[34m.╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
""")
print("""
\u001b[31m.[1] socks4
\u001b[31m.[2] socks5
\u001b[31m.[3] http
\u001b[31m.[4] Exit
""")
choice = int(input("[?]: "))
if choice == 1:
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    print("\u001b[32m." + r.text)
    choice = input("Save Proxies?(yes,no): ")
    while(choice!="yes" and choice!="no"):
        print("\u001b[31m.Wrong Option, Type Yes Or No")
        time.sleep(1)
        choice = input("Save Proxies?(yes,no): ")
    else:
        if(choice=="yes"):
            file = open('./results//socks4.txt', "w")
            file.write(r.text)
            file.close()
            print("\u001b[32m.saved")
            time.sleep(3)
            os.system('cls')
        else:
            print("Ok")
            time.sleep(5)
if choice == 2:
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    print(r.text)
    choice = input("You Wanna Save The proxies?(yes,no): ")
    while(choice!="yes" and choice!="no"):
        print("Wrong Option, Please Consider Telling Yes or No")
        time.sleep(1)
        choice = input("You Wanna Save The proxies?(yes,no): ")
    else:
        if(choice=="yes"):
            file = open('./results//socks5.txt',"w")
            file.write(r.text)
            file.close()
            print("SAVED")
            time.sleep(3)
        else:
            print("alright")
            time.sleep(10)
            os.system('cls')

if choice == 3:
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    print(r.text)
    choice = input("Wanna Save Proxies?(yes,no): ")
    while(choice!="yes" and choice!="no"):
        print("Wrong Option Type Yes or No")
        time.sleep(1)
        choice = input("Wanna Save Proxies?(yes,no): ")
    else:
        if(choice=="yes"):
            file = open('./results//http.txt', "w")
            file.write(r.text)
            file.close()
            print("saved kiddo")
        else:
            print("K")
            time.sleep(10)
            os.system('cls')

if choice == 4:
    x = 4



