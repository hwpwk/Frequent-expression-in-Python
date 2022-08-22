# zipファイルを解凍し解凍ファイルを指定パスに格納
# https://qiita.com/tohka383/items/b72970b295cbc4baf5ab
# https://qiita.com/zoonaka/items/aa0f4149334848285b69
import zipfile
for path in zip_path_list:
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            info.filename = info.orig_filename.encode('cp437').decode('cp932')
            if os.sep != "/" and os.sep in info.filename:
                info.filename = info.filename.replace(os.sep, "/")
            z.extract(info, path=r'D:\tomori\data\unzip/')