import pandas as pd
import math
import os
import glob
from shutil import copyfile
import sys

section = "3308-204"  # change to desired section name
submissions_folder = "/home/jsmayank/Desktop/submissions_lab4"  # change to folder name containing downloads
lab_num = "4"  # optional

section_csv = "swe"+section+".csv"

data_df = pd.read_csv(section_csv)

file_names = []
for ind in data_df.index:
    curr_row = data_df.loc[ind]
    curr_student = curr_row['Student']
    curr_id = curr_row['ID']
    curr_sis = curr_row['SIS User ID']
    if not math.isnan(curr_sis):
        curr_sis = int(curr_sis)
    curr_name = curr_student.split(",")[0].lower() + curr_student.split(",")[1].lower().lstrip() + "_" + `curr_id` + "_"
    file_names.append(curr_name)

directory_name = section+"_submissions_" + lab_num
cwd = os.path.abspath(os.getcwd())
directory = cwd + '/' + directory_name
if not os.path.isdir(directory):
    os.mkdir(directory,0o777)

failed_files = []
src_pre = submissions_folder + '/'
dest_pre = cwd + '/' + directory_name + '/'
for i in range(len(file_names)):
    curr_file_wildcard = src_pre + file_names[i] + "*"
    curr_files = glob.glob(curr_file_wildcard)
    if len(curr_files) > 0:
        for j in range(len(curr_files)):
            src = curr_files[j]
            dest = dest_pre + curr_files[j].split('/')[-1]
            try:
                copyfile(src,dest)
            except Error:
                failed_files.append(file_names[i])
    else:
        failed_files.append(file_names[i])

failed_file = dest_pre + '/00000failed_file_transfers.txt'
with open(failed_file, 'w') as f:
    for item in failed_files:
        print >> f, item
