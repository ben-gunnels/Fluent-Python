def merge_dicts(dct1: dict, dct2: dict):
    return dct1 | dct2

io_mappings_1 = { "led1": 12, "right_motor": 14, "left_motor": 16 }
io_mappings_2 = { "led1": 13, "led2": 10, "infrared": 21}

merged_io_map = merge_dicts(io_mappings_1, io_mappings_2)

# Notice what value "led1" points to in the merged mapping. Is this the behavior that was intended?
print(merged_io_map)