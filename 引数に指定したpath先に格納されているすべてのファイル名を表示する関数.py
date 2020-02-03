iimport sys,os
import glob
import pandas as pd


def disp_file_name(path):
    '''
    関数内容
    ・引数に指定したpath先に格納されているすべてのファイル名を表示する関数
    Input
    ・Path：名前を表示したいファイルが格納されているパス
    関数使用方法
    display_file_name(r'L:\Work\20018\Data\*.*')
    '''

    file_path_list = sorted(glob.glob(path))
    
    file_name_list = [os.path.basename(file) for file in file_path_list]
    
    return file_name_list
    
 