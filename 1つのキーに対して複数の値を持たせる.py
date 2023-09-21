from collections import defaultdict

s_l = ['s1','s2','s3']
cols_l = [[1,2,3],[4,5,6],[7,8,9]]
file_l = ['f1', 'f2', 'f3']

 リストの長さを取得
num_elements = len(s_l)

tmp_d = defaultdict(list)

for i in range(num_elements):
    s = s_l[i]
    c = cols_l[i]
    f = file_l[i]
    tmp_d[s] = {'cols': c, 'file': f}

if __name__ == '__main__':
    print(tmp_d)
    print(tmp_d['s1']['cols'])
    print(tmp_d['s1']['file'])