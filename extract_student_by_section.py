import pandas as pd

downloaded_csv = "swe.csv"

section_desired = "3308-204"

data_df =  pd.read_csv(downloaded_csv)

df_new = pd.DataFrame(columns=data_df.columns)
for ind in data_df.index:
    row = data_df.loc[ind]
    curr_sec = row['Section']
    if isinstance(curr_sec, str) and section_desired in curr_sec:
        df_new = df_new.append(row, ignore_index=True)

print df_new.shape
filename = "swe"+section_desired+".csv"
df_new.to_csv(filename,index=False)
