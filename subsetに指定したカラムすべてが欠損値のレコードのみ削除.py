import pandas as pd
# ag�J�����Ast�J�����̂ǂ��炩�������l�ɂȂ��Ă��郌�R�[�h���폜
df = df.dropna(subset=['ag', 'st'])

# ag�J�����Ast�J�����̂ǂ���������l�ɂȂ��Ă��郌�R�[�h���폜
df = df.dropna(subset=['ag', 'st'], how='all')