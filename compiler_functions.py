# -*- coding: utf-8 -*-
"""
Functions used in compiler.py
"""
import pandas as pd
from pathlib import Path

# function to extract copepod id and day from file name
def extract_cop_name_day(fpath):
    # takes in file path to txt file, returns copepod name and day as tuple
    fname = Path(fpath).stem # get the file name without suffix
    fnamel = fname.split("_") # split file name by underscores
    if len(fnamel) == 3: # should break into 3 parts, if so get name and day
        day = int(fnamel[2])
        cop_name = "_".join(fnamel[0:2])
        print(fname, "OK")
    else:
        print(fname, "Non-standard file name")
    return(fname, cop_name, day) # return tuple


# function to quality check data frame imported from txt file
def quality_check_df(pd_df):
    '''
    Take a pandas data frame, read from txt file, and make sure it fits
    expectations for these files. Flags files that deviate from
    expectations, and returns the adjusted df.
    '''
    # get number of rows, columns in df 
    n_row, n_col = pd_df.shape
    
    # check if number of columns is expected
    if n_col == 8:
        ok_col_num = 0
    else:
        ok_col_num = 1
    
    # check if number of rows is expected
    if n_row == 62:
        ok_row_num = 0
    else:
        ok_row_num = 1
    
    # check if col names are as expected
    colnames = [' ', 'Track n°', 'Slice n°', 'X', 'Y',
            'Distance', 'Velocity', 'Pixel Value'] # expected column names
    if sum(colnames != pd_df.columns) == 0: 
        ok_col_names = 0
    else:
        ok_col_names = 1
        # if mismatches occur, replace names with expectations
        # this is necessary for binding rows of mulitple dfs
        pd_df.columns = colnames
    
    # not all variables needed, remove a few
    pd_df = pd_df[['Slice n°', 'X', 'Y', 'Distance', 'Pixel Value']]
    
    # add QC variables
    pd_df = pd_df.assign(ok_col_num = ok_col_num, 
                   ok_row_num = ok_row_num, 
                   ok_col_names = ok_col_names)
    return(pd_df)
    
  

# function to create master data frame from all txt files in a folder
def create_master_df(file_list):
    # takes in a file list and then loops through it to combine into single df
    for f in file_list:
        
        # read file into pandas data frame
        df = pd.read_table(f, encoding = 'latin-1')
        df = quality_check_df(df) # qc file
        
        fname, cop_name, day = extract_cop_name_day(f) # add cop name, day
        df = df.assign(fname = fname, cop_name = cop_name, day = day)
        
        # check if this is first dataframe      
        try:
            master_df
        except NameError:
            master_df = df # no master, create it from first df
        else:
            master_df = pd.concat([master_df, df]) # combine two data frames
    
    return(master_df)
