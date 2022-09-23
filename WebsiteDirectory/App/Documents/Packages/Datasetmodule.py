# This will be dataaset module

import os
import pandas as pd


def csvdataset():
    #search_dir = 'C:\\Users\\Dikshit\\Documents\\WebsiteDir\\App\\Documents\\YTDT'
    search_dir = 'C:\\Users\\Dikshit\\Documents\\WebsiteDirectory\\App\\Documents\\YTDT'
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=os.path.getmtime)
    data1 = pd.read_csv(files[-1], index_col=0)
    return data1


def csvname():
    #search_dir = 'C:\\Users\\Dikshit\\Documents\\WebsiteDir\\App\\Documents\\YTDT'
    search_dir = 'C:\\Users\\Dikshit\\Documents\\WebsiteDirectory\\App\\Documents\\YTDT'
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=os.path.getmtime)
    data1 = pd.read_csv(files[-1], index_col=0)
    nametest = files[-1].split('\\')[-1]
    nametest = nametest.split('channel.csv')[0]
    return nametest


def test(something):
   data=something
   return data
