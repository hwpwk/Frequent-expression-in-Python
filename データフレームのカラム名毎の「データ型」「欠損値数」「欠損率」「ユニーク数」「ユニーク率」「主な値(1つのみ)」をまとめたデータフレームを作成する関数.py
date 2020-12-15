def col_data_in_dataframe1(df):
    '''
    �֐����e
    �E�f�[�^�t���[���̃J���������́u�f�[�^�^�v�u�����l���v�u�������v�u���j�[�N���v�u���j�[�N���v�u��Ȓl�v���܂Ƃ߂��f�[�^�t���[�����쐬����֐�
     ����Ȓl��1�̂�
    Input
    �Edf�F�f�[�^�t���[��
    �֐��g�p���@
    �Ecol_data_in_dataframe2(df)
    '''
    import itertools
    
    col_list = df.columns.tolist()
    null_num_list = df.isnull().sum().tolist()
    data_type_list = df.dtypes.tolist()
    col_unique_num_list = df.nunique().tolist()
    null_num_per_list = [str(round(num/df.shape[0],2)*100)+'%' for num in null_num_list]
    unique_num_per_list = [str(round(num/df.shape[0],2)*100)+'%' for num in col_unique_num_list]
    main_values_list = [df[col].value_counts().reset_index()['index'].tolist()[:1] for col in df.columns.tolist()]
    # ���X�g���̃��X�g������
    main_values_list = list(itertools.chain.from_iterable(main_values_list))

    summary_df = pd.DataFrame({
        '�J������':col_list,
        '�f�[�^�^':data_type_list,    
        '�����l��':null_num_list,
        '������':null_num_per_list,
        '���j�[�N��':col_unique_num_list,
        '���j�[�N��':unique_num_per_list,
        '��Ȓl':main_values_list
    })

    return summary_df