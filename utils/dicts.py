def get_val(collection, key, default='git'):
    key_collection = collection.keys()
    if key in key_collection:
        return collection[key]
    else:
        return default
