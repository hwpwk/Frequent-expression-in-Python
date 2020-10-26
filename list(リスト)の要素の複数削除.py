del_fs_name_list = ['KK_FS_201403','KK_FS_202012']

# name_listに含まれている要素がdel_fs_name_listに含まれていれば、その要素は抽出しない
fs_name_list2 = [name for name in fs_name_list if name not in del_fs_name_list]