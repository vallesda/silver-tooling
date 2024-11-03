import sys
from hashlib import sha256

def hash_function(data):
    return sha256(data).hexdigest()

def find_duplicates(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = hash_function(data)

        if hash_code in groups:
            groups[hash_code].append(fn)
        else:
            groups[hash_code] = []
            groups[hash_code].append(fn)
    return groups



if __name__ =="__main__":
    unique_groups = find_duplicates(sys.argv[1:])
    for key, val in unique_groups.items():
        print(val)