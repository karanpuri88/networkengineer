# Identify all BGP neighbors using Regex & count number of neighborship Flaps
# !/usr/bin/env python

import netmiko
import re 

IP = input ("Enter IP address of router : ")
user = input ("Enter Username : ")
pas = input("Enter Password : ") 
sec = input ( "Enter Enable password : ")

session = netmiko.ConnectHandler(ip = IP, username = user, password = pas, secret = sec, device_type = "cisco_xe")

output = session.send_command ("sh ip bgp neighbors | in Session")

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ips = pattern.findall(output)

for nbr in ips:
      session.enable()
      logs = session.send_command("sh logg | in %s Down" %(nbr))
      count = (len(logs.split("\n")))
      print("BGP neighbor IP %s flapped %s many times"%(nbr, count))



