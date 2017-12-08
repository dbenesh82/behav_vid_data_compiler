# -*- coding: utf-8 -*-
"""
This script takes the copepod behavior data, which is in separate .txt files in
different folders, and combines them into a single master file
"""

# import modules used in compiler_functions
import pandas as pd
from pathlib import Path

# current working dir, ideally where compiler files are
cwd = Path.cwd()
# check if it is correct
if len(list(cwd.glob("*compiler_functions.py"))) == 1:
    # if compiler functions py found, import them
    from compiler_functions import extract_cop_name_day, quality_check_df, create_master_df
    # then switch cwd path to raw_data folder
    cwd = cwd / "raw_data"
    if cwd.exists():
        print("Changed to 'raw_data' folder")
    else:
        print("Could not change to correct folder")
else:
    print("Check working directory")




# now loop through the directories in the raw_data folder
# in each create a pandas data frame, and combine them together
dirs = [x for x in cwd.iterdir() if x.is_dir()] # get all the directories in folder
# loop through the directories
for d in dirs:
    f1 = list(d.glob("*.txt"))        # list txt files in folder
    # if first folder, start master_df, else add new data to master_df
    try:
        master_df
    except NameError:
        master_df = create_master_df(f1)
    else:
        master_df = pd.concat([master_df, create_master_df(f1)])


# write to file       
master_df.to_csv("wrangled_data/behav_combined_out.csv")
