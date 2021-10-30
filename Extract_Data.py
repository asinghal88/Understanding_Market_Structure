# -*- coding: utf-8 -*-
"""
Spyder Editor

Extract Data from the zip files downloaded from the SEC MIDAS: Code adapted from 
Stackoverflow for extracting data from the zip files and appending the data
"""

import glob
import pandas as pd
from zipfile import ZipFile
import os
#Zip_Data is the location set for all the zip files downloaded from the SEC MIDAS site	
#Joining the system path and the zip path
system_path = os.getcwd()
zip_files_path =  'Zip_Data'
path = os.path.join(system_path,zip_files_path)
print(path)
#load all zip files in folder
all_files = glob.glob(path+"/*.zip")

final_df = pd.DataFrame()
i = 0
#Appending all the quarters data from 2012Q1 to 2021Q2
for filename in all_files:
    print(i)
    zip_file = ZipFile(filename)
    dfs = list({text_file.filename: pd.read_csv(zip_file.open(text_file.filename))
        for text_file in zip_file.infolist()
        if text_file.filename.endswith('.csv')}.values())[0]
    final_df = final_df.append(dfs)
    i+=1
final_df["Date"] = final_df["Date"].astype("int")
final_df.to_csv("Processed_Data.csv")