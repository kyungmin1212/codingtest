# 충돌이 있는경우 (Linear Probing 기법 : 폐쇄해쉬 or Close Hashing 기법 중 하나 )(선형적으로 내려가면서 찾는다고 생각)
hash_table=[0 for i in range(8)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data,value):
    key=get_key(data)
    hash_address=hash_function(key)
    if hash_table[hash_address]!=0:
        for i in range(hash_address,len(hash_table)):
            if hash_table[i][0]==key:
                hash_table[i][1]=value
                return
            elif hash_table[i]==0:
                hash_table[i]=[key,value]
                return
    else:
        hash_table[hash_address]=[key,value]

def read_data(data):
    key = get_key(data)
    hash_address = hash_function(key)
    if hash_table[hash_address]!=0:
        for i in range(hash_address,len(hash_table)):
            if hash_table[i][0]==key:
                return hash_table[i]
            else:
                return None
    else:
        return None

save_data("Dd","123")
save_data("asdf","223")

save_data("poio","9950")
print(hash_table)
print(read_data("poio"))
# 원래같으면 hashtable 을 만들때 보통 저장해야할 데이터보다 더큰 테이블 공간을 마련해두기때문에 가능하다.