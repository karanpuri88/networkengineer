# Take backup of multiple devices which includes SDWAN & NON SDWAN Routers

#!/usr/bin/env python

import netmiko
import os

def create_backup_folder():
        os.chdir("/Users/karpuri/Documents/Devnet/Learning Py/")
        try :
            os.mkdir("backups")
        except OSError as err:
            if err.errno == 17:
                # print("Dir already exist moving on")
                os.chdir("/Users/karpuri/Documents/Devnet/Learning Py/backups")

def backup_sdwan():
    hostname = session.find_prompt()
    hostname = hostname.replace("#","")
    command0 = session.send_command("sh clock")
    command1 = session.send_command("sh runn")
    command2 = session.send_command("sh sdwan run")
    session.disconnect()
    create_backup_folder()
    with open(hostname +".txt", "w") as file:
        file.write("It is SDWAN Router\n==================\n")
    with open(hostname +".txt", "a") as file:
        file.write(command0)
    with open(hostname +".txt", "a") as file:
        file.write("\n!\nPRINTING SHOW RUN\n==================\n!\n")
    with open(hostname +".txt", "a") as file:
        file.write(command1)
    with open(hostname +".txt", "a") as file:
        file.write("\n!\nPRINTING SHOW SDWAN RUN\n=======================\n!\n")
    with open(hostname+ ".txt", "a") as file:
        file.write(command2)

def backup_non_sdwan():
    session.enable()
    hostname = session.find_prompt()
    hostname = hostname.replace("#","")
    command0 = session.send_command("sh clock")
    command1 = session.send_command("sh runn")
    session.disconnect()
    create_backup_folder()
    with open(hostname +".txt", "w") as file:
        file.write("It is NON-SDWAN Router\n======================\n\n")
    with open(hostname +".txt", "a") as file:
        file.write(command0)
    with open(hostname +".txt", "a") as file:
        file.write("\n\n!\nPRINTING SHOW RUN\n==================\n!\n")
    with open(hostname +".txt", "a") as file:
        file.write(command1)

user = input ("Enter Username : ")
passw = input ("Enter Password : ")
sec = input("Enter enable password : ")
with open("/Users/karpuri/Documents/Devnet/Learning Py/Device_List.txt","r")  as file:
    for IPs in file:
        session = netmiko.ConnectHandler (ip = IPs, username = user, password = passw, secret = sec, device_type = "cisco_xe")
        operating_mode = session.send_command("sh ver | in mode")
        if operating_mode == "Router operating mode: Controller-Managed" :
            hostname = session.find_prompt()
            hostname = hostname.replace("#","")
            print(hostname, "is SDWAN Router")
            backup_sdwan()
            print("Back up of" , hostname, "taken")
        else :
            session.enable()
            hostname = session.find_prompt()
            hostname = hostname.replace("#","")
            print(hostname, "is Non-SDWAN Router")
            backup_non_sdwan()
            print("Back up of" , hostname, "taken")

print("Thank you for taking backups , coded by Karan Puri")
