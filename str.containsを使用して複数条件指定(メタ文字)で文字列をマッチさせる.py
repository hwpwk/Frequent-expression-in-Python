import pandas as pd

# �J�������擪���u*�v�A�u���v�̃J�������폜������ȊO�̃J�����𒊏o������
# str.contains���g�p����ꍇ�A�u*�v�A�u���v�̂悤�ȃ��^�����͋L���̑O�Ɂu\�v��������K�v����

all_zaiko_df.columns[~all_zaiko_df.columns.str.contains('\*|\��')]