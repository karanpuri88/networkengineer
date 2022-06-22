# This script can be use to compare config and generate script
import difflib

# Takes the input of files 
first_file = input("Enter the Full path of first File : ")
second_file = input("Enter the Full path of Second File : ")

#Open Files & readlines
first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()

#Using Difflib compare &  create html report
difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
difference_report = open("/Users/karpuri/Downloads/diff_report_2.html", "w")
difference_report.write(difference)
difference_report.close()
print("HTML Report is created , please open & view in web browser")