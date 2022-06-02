# Perform QFP trace
# !/usr/bin/env python

from ipaddress import ip_address
import netmiko
import os

ipaddr = input("Enter Router IP address : ")
user = input ("Enter Username : ")
passwd = input ("Enter Password : ")
sec = input ("Enter Secret : ")

def create_capture_folder():
        os.chdir("/Users/karpuri/Documents/Devnet/Learning Py/")
        try :
            os.mkdir("Captures")
        except OSError as err:
            if err.errno == 17:
                os.chdir("/Users/karpuri/Documents/Devnet/Learning Py/Captures")

def send_debugs():
    interf = input ("Enter Input or Outgoing interface : ")
    session.send_command("debug platform condition interface %s ipv4 access-list TAC both "%(interf))
    session.send_command("debug platform packet-trace packet 1024 fi cir")
    session.send_command("debug platform packet-trace copy packet both l2 s 256")

def qfp_capture():
    src_ip = input ("Enter source IP : ")
    dst_ip = input ("Enter destination IP : ")       
    session.enable()
    acl = ["ip access-list extended TAC","10 permit ip host %s host %s" %(src_ip, dst_ip), "20 permit ip host %s host %s" %(dst_ip,src_ip)]
    session.send_config_set(acl)
    session.send_command("end")
    print("Debug ACL TAC configured")
    send_debugs()

session = netmiko.ConnectHandler(ip = ipaddr , username = user, password = passwd, secret = sec, device_type = "cisco_xe")
qfp_capture()
start = int (input ("debugs enabled press 1 & hit enter to start : "))
if start == 1:
    session.send_command("debug platform condition start")
    print ("Capture started & ask user to recreate the issue")
    stop = int (input ("debugs enabled press 0 & hit enter to stop : "))
    print("Capturing logs be paitent it may take few minutes based on number of packets captured")
    if stop == 0:
        session.send_command("debug platform condition stop")
else : 
    session.disconnect()

session.send_command("term len 0")
current_time = session.send_command("sh clock")
summary = session.send_command("show platform packet-trace summary")
decode_all = session.send_command("show platform packet-trace packet all decode", read_timeout=120)
session.send_command("clear platform condition all")
session.send_config_set("no ip access-list extended TAC")
session.send_command("end")
create_capture_folder()
hostname = session.find_prompt()
hostname = hostname.replace("#","")
with open (hostname+".txt", "w") as file :
    file.write(current_time)
with open (hostname+".txt", "a") as file :
    file.write("\n""SUMMARY" "\n" "========""\n")
with open (hostname+".txt","a") as file:
    file.write(summary)
with open (hostname+".txt","a") as file :
    file.write("DECODE ALL" "\n" "===========""\n")
with open (hostname+".txt","a") as file :
    file.write(decode_all)
session.disconnect()

print ("Coded by Karan Puri")

