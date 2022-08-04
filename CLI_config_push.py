
import netmiko
user = input("Enter Username : ")
passw = input("Enter Password : ")
secw = input("Enter Secret Password : ")

with open ("/Users/karpuri/Desktop/device_list.txt","r") as file:
    x = file.readlines()
    # print("Devices in text files are : \n")
    for ip_addr in x:
        # print(ip_addr)
        print("Connecting to device :" , ip_addr)
        session = netmiko.ConnectHandler(ip = ip_addr , username = user, password = passw , secret = secw , device_type = "cisco_xe")
        session.enable()
        output = session.send_config_from_file(config_file="/Users/karpuri/Desktop/test_CLI")
        print(output)
        print("Saving config of " + ip_addr)
        session.save_config()
        session.disconnect()
        # print("Device : %s is configured"%(ip_addr))

       
# with open ("/Users/karpuri/Desktop/test_CLI", "r") as file:
#     syn = file.read()
#     print("\nSyntax to configure :\n\n" , syn )


