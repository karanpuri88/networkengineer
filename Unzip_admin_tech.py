# Coded by Karan Puri
# Untar SDWAN Admin Tech .tar.gz 

import tarfile
import os
import re
import shutil


#  Admin Tech Input
print("Enter the full path of Admin Tech")
admintech = input()
admin_tech_name = os.path.basename(admintech)

# Check if it is valid Tar gz or not
if  bool(re.findall(".gz$" , admin_tech_name)) == True:
    print ("Admin Tech Verified")
else :
    print ("Not a tar.gz file")

# We need to create 2 Folders , one is same name as case number & other one is same name as Admin Tech name 
parent_path = os.path.dirname(admintech)
os.chdir(parent_path)
print ("Enter Case number")
case_number = input ()
try:
    os.mkdir(case_number)
    print ( "Folder", case_number, "Created" )
except OSError as err:
    if err.errno == 17:
        print("Dir already exist moving on")
shutil.move(admintech, case_number)
os.chdir(case_number)

#If already created in case of multiple Admin Techs downloaded from Case , create a exeption handling 
folder_creation = admin_tech_name.split(".tar.gz")
folder_name = folder_creation[0]
print ("Admin tech Folder inside" , case_number, "created" )

# Untar the Admin Tech inside the folder 
my_tar = tarfile.open(admin_tech_name)
my_tar.extractall(folder_name) 
my_tar.close()
print ("Admin tech extracted")
new_path = (os.getcwd())

# Untar all files inside Admin Tech

for root, dirs, files in os.walk(new_path):
    for allfiles in files:
        if bool(re.findall("vdebug_", allfiles)) == True:
            os.chdir(root)
            vdebug_folder_creation = allfiles.split(".tar.gz")
            vdebug_folder = vdebug_folder_creation[0]
            os.mkdir(vdebug_folder)
            shutil.move(allfiles, vdebug_folder)
            os.chdir(vdebug_folder)
            command = "tar -xvf " + allfiles
            os.system (command) 
            print (allfiles, " file extracted")
        elif bool(re.findall(".gz$", allfiles)) == True:
            gzfiles = os.path.join(root, allfiles)
            command = "gunzip " + gzfiles
            os.system (command)
            print (gzfiles ," file successfully unzipped")

