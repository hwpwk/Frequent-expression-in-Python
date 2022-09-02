def complement_null_values(cate_list):
    """
    データフレームの値がリストで格納されている場合にリストを除外して値を文字列にする
    """
    try:
        return ','.join(map(str, cate_list))
    # リスト内に「nan」が含まれている場合があるので
    except:
        return cate_list