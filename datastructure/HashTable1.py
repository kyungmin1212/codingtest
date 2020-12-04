# 충돌이 일어나지 않는 HashTable 의 경우
hash_table=[0 for x in range(8)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data,value):
    key=get_key(data)
    hash_address=hash_function(key)
    hash_table[hash_address]=value

def read_data(data):
    key=get_key(data)
    hash_address=hash_function(key)
    return hash_table[hash_address]

save_data('Dave','01072656656')
save_data('trump','01051461653')
print(read_data('Dave'))
print(hash_table)