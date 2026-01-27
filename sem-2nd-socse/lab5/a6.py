def merge_dictionaries_with_sum(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], (int, float)) and isinstance(value, (int, float)):
                merged_dict[key] += value
            elif isinstance(merged_dict[key], str) and isinstance(value, str):
                merged_dict[key] += value
            elif isinstance(merged_dict[key], list) and isinstance(value, list):
                merged_dict[key].extend(value)
            else:
                print(f"Warning: Overlapping keys with incompatible types ('{key}'). Keeping value from dict1.")
        else:
            merged_dict[key] = value
    return merged_dict
dict1 = {"a": 10, "b": 20, "c": 30, "d": [1,2,3], "e": "hello"}
dict2 = {"b": 5, "c": 15, "d": [4,5,6], "f": 40, "e": " world"}
merged_dict = merge_dictionaries_with_sum(dict1, dict2)
print(merged_dict)
dict3 = {"x": 1, "y": "test"}
dict4 = {"x": "string", "z": 2}
merged_dict2 = merge_dictionaries_with_sum(dict3, dict4)
print(merged_dict2)
dict5 = {"a": 10, "b": 20}
dict6 = {"a": "string", "b": 30}
merged_dict3 = merge_dictionaries_with_sum(dict5, dict6)
print(merged_dict3)
