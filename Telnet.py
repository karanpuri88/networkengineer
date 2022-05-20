# Telnet to router & execute any Command 

#!/usr/bin/env python

import telnetlib

ip = input("Enter IP address: ")
user = input("Enter Username : ")
passw = input ("Enter Password : ")
sec = input ("Enter Enable password : ")

# Default string is UTF-8 , so convert it into ascii because telnet uses byte strings
username = user.encode("ascii")
password = passw.encode("ascii")
secret = sec.encode("ascii")

# Creating Session to telnet to router Telnet is function inside telnetlib (module.function())
connection = telnetlib.Telnet(ip)

# Read untill username & password in byteString & then write  
connection.read_until(b"Username:")
connection.write( username +b"\n")
connection.read_until(b"Password:")
connection.write(password + b"\n")
connection.write(b"enable" + b"\n")
connection.read_until(b"Password:")
connection.write(secret + b"\n")

# Enter the command to read from router  
com = input("Enter the read command to you want to run : ")
command = com.encode("ascii")
connection.write(command + b"\n")

#Read the output & convert into UTF-8 Format otherwise output would be in bytes ascii format & very clumpsy 
out = connection.read_all()
output = out.decode("utf-8")
print(output)

# Close Telnet session
connection.close()