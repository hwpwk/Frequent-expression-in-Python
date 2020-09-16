import xlrd

book_list = [xlrd.open_workbook(path).nsheets for path in files]