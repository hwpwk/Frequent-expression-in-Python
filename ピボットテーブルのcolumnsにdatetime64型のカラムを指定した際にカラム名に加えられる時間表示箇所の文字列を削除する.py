import pandas as pd
# �����f�[�^�ɕύX
pivot_df =df.pivot_table(index=['����ȖڃR�[�h','����Ȗږ�'], columns='���Z��', values='���z���v', aggfunc='sum')
# ��datetime64�^�̃J�������Ɏw�肷��ƃJ���������u2017-06-30 00:00:00�v�ɂȂ��Ă��܂�

# ���Z���̎��ԕ\������(2017-06-30 00:00:00�́u00:00:00�v)�̕�������폜
pivot_df = pivot_df.rename(columns = lambda x: str(x).split()[0])