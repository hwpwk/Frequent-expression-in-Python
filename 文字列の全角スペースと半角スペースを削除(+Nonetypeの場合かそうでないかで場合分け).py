import pandas as pd
# ���̑S�p�X�y�[�X�Ɣ��p�X�y�[�X���폜
# �u'NoneType' object has no attribute 'replace'�v�Ƃ����G���[���������Ȃ��悤������if x!=None��ǉ�
# https://support.esri.com/ja/technical-article/000014467
df['_�C��'] = df['��'].map(lambda x: x.replace(' ','').replace('�@','') if x!=None else x)