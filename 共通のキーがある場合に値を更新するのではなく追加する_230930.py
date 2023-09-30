my_dict = {'キー1': '値1', 'キー2': '値2'}

# 新しいキーと値を持つ辞書 dict2
dict2 = {'キー1': '新値1', 'キー2': '新値2'}

# 既存のキーに値がある場合は値をリストに追加
for key, new_value in dict2.items():
    if key in my_dict:
        current_value = my_dict[key]
        if isinstance(current_value, list):
            current_value.append(new_value)
        else:
            my_dict[key] = [current_value, new_value]
    else:
        my_dict[key] = new_value
