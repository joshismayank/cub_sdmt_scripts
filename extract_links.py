import pandas as pd
from os import listdir
from os.path import isfile, join

folder_name = "/home/jsmayank/3308-205_submissions_4"  # change it to name of folder which contains files
url_substring = "github.com"  # change this to common part between all submissions

file_names = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]
non_operated_files = []
flag = False

data = []
for item in file_names:
    if item.split(".")[-1] == "txt":
        curr_id = item.split("_")[1]
        curr_item = folder_name + "/" + item
        with open(curr_item) as f:
            content = f.readlines()
            for line in content:
                if url_substring in line:
                    urls = line.split(" ")
                    for url in urls:
                        if url_substring in url:
                            curr_data = []
                            curr_data.append(curr_id)
                            curr_data.append(url)
                            data.append(curr_data)
                            flag = True
            if not flag:
                non_operated_files.append(item)
            flag = False
    else:
        non_operated_files.append(item)

file_name = folder_name + "_links.csv"
data_df = pd.DataFrame(data, columns=['ID','links'])
data_df.to_csv(file_name,index=False)

print "did not extract link from: "
for item in non_operated_files:
    print item
