
def transform(legacy_data):
    new_dict = {}

    for key, value in legacy_data.items():
        #print("key: ", key)
        #print("value: ", value)

        col = key

        for item in value:
            item = item.lower()
            new_dict[item] = [col]

    #sortednames=sorted(new_dict.keys(), key=lambda x:x.lower())
    return new_dict #sortednames