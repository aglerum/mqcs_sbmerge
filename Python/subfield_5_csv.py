"""
Created by Jennifer Scholl 9-11-2022
This script takes an input .mrk file and creates an OpenRefine or other tool-ready .csv file to analyze fields
that hold a $5.
"""

import csv
import turtle as t
import os

t.setup(300, 300)
user_input_file = t.textinput("$5 manipulation for analysis", "What is the path of your input file? "
                                                              "ex. /Users/username/general_collection.mrk")

line_ct = 1
new_rec = True

with open(user_input_file, "r", encoding="utf8") as input_file:
    input_rdr = csv.reader(input_file)
    output_file_hldr = user_input_file.replace(".mrk", "2.csv")
    output_file = open(output_file_hldr, "w", encoding="utf8")

    for row in input_rdr:
        print(line_ct)
        x = "".join(row)
        output_file.write(x)
        output_file.write("\n")
        line_ct += 1

    input_file.close()
    output_file.close()
    print("Files closed.")


with open(output_file_hldr, "r", encoding="utf8") as input_file:
    input_rdr = csv.reader(input_file)
    output_file_holder = user_input_file.replace(".mrk", ".csv")
    output_file = open(output_file_holder, "w", encoding="utf8")


    header_added = False

    if not header_added:
        output_file.write("action")
        output_file.write(",")
        output_file.write("iz_mms_id")
        output_file.write(",")
        output_file.write("nz_mms_id")
        output_file.write(",")
        output_file.write("field")
        output_file.write(",")
        output_file.write("full_contents_field")
        output_file.write(",")
        output_file.write("sub_5")
        output_file.write("\n")

    for row in input_rdr:
        x = " ".join(row)
        if new_rec:
            output_file.write("action:")
            output_file.write(",")
            new_rec = False
        if "=001" in x:
            mms_id = x
        if "(EXLNZ-01FALSC_NETWORK)" in x:
            nz_hld = x.replace(r"\\$a(EXLNZ-01FALSC_NETWORK)", "")
            nz = nz_hld
        if "$5" in x:
            output_file.write(str(mms_id))
            output_file.write(",")
            output_file.write(str(nz))
            output_file.write(",")
            fld = x.split(" ")
            output_file.write(fld[0])
            output_file.write(",")
            output_file.write(x)
            output_file.write(",")
            rhs = x.split("$5")
            srtd_rhs = sorted(rhs)
            for i in range(1, len(srtd_rhs)):
                output_file.write(str(srtd_rhs[i]))
                output_file.write(" ")
            sep_sub5 = x.split("$5")
            for i in range(1, len(sep_sub5)):
                output_file.write(str(sep_sub5[i]))
                output_file.write(",")
            # print(sep_sub5)
            output_file.write("\n")
            new_rec = True



    input_file.close()
    if os.path.isfile(output_file_hldr):
        os.remove(output_file_hldr)
    output_file.close()
    print("Files closed.")