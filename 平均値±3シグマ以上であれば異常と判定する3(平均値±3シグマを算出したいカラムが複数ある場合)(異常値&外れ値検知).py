def add_range_judge_outlier_col_to_dataframe2(df, col, weight):
    '''
    �֐����e
    �E���ϒl�ƕW���΍����g�p���ĊO��l���o�p�͈̔͂̉����l�Ə���l��ǉ������f�[�^�t���[�����쐬����֐�
    Input
    �Edf:�f�[�^�t���[��
    �Ecol:�O��l������������J����
    �Eweight:�W���΍��ɂ�����d��
    �֐��g�p���@
�@�@�@ norm_col_list = norm_df.columns[norm_df.columns.str.endswith('_���K��_���O�l��������')].tolist()
    �@ norm_df_list =\
    �@[add_range_judge_outlier_col_to_dataframe(norm_df[[col]], col, 1) for col in norm_col_list]
    �@ norm_df = pd.concat([norm_df]+norm_df_list, axis=1)
      #�J���������d������̂ŏd�����Ă���J���������폜
      norm_df = norm_df.loc[:,~norm_df.columns.duplicated()]
    '''
    name = str(col)
    
    df[name + '_lower_limit'] = np.mean(df[col],axis=0) - np.std(df[col],ddof=0,axis=0)*weight
    
    df[name + '_upper_limit'] = np.mean(df[col],axis=0) + np.std(df[col],ddof=0,axis=0)*weight
    
    return df

#���ϒl�ƕW���΍����g�p���ĊO��l���o�p�͈̔͂̉����l�Ə���l��ǉ��������J�����𒊏o
norm_col_list = norm_df.columns[norm_df.columns.str.endswith('_���K��_���O�l��������')].tolist()

# �O��l�𔻒肵�����J�������������邽�߂������񃊃X�g����\�L���g���f�[�^�t���[�������X�g�Ɋi�[
norm_df_list =[add_range_judge_outlier_col_to_dataframe2(norm_df[[col]], col, 1) for col in norm_col_list]

# ���ɘA��
norm_df = pd.concat([norm_df]+norm_df_list, axis=1)

#�J���������d������̂ŏd�����Ă���J���������폜
norm_df = norm_df.loc[:,~norm_df.columns.duplicated()]

