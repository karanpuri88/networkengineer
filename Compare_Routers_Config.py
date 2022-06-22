# This script can be use to compare config and generate script

import difflib


first_file = ("/Users/karpuri/Downloads/compare_file_new1.txt")
second_file = ("/Users/karpuri/Downloads/compare_file_new2.txt")

first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()


difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
difference_report = open("/Users/karpuri/Downloads/diff_report_1.html", "w")
difference_report.write(difference)
difference_report.close()