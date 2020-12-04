# 충돌이 있는경우 (chaining 기법 : 개방해쉬 or Open Hashing 기법 중 하나 , 추가적인 공간을 확보)(옆으로 chaining 한다고 생각)
hash_table=[0 for x in range(8)]
def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def save_data(data,value):
    key=get_key(data)
    hash_address=hash_function(key)
    if hash_table[hash_address]!=0:
        for i in range(len(hash_table[hash_address])):
            if key==hash_table[hash_address][i][0]:
                hash_table[hash_address][i][1]=value # key 에 해당하는 값이 있는경우 그 key 에 해당하는 데이터를 변경해주는 것이다.
                return  # return 을 만나면 그순간 함수가 끝난다. key 해당하는 값을 찾아 데이터를 업데이트 했으면 더이상 함수를 진행할필요가 없다.
        hash_table[hash_address].append([key,value])
        # for 문을 다 돌았는데도 없다는것은 hash_address가 같은 hash table 에는 같은 key 를 가진것이 없다는 것이므로 그냥 추가해주면된다.
    else:
        hash_table[hash_address]=[[key,value]]
        # [[]] 괄호를 두개를 넣어주는 이유는 값을 여러개를 옆으로 늘리면서 넣어주기 때문이다.

def read_data(data):
    key = get_key(data)
    hash_address = hash_function(key)
    if hash_table[hash_address]==0:
        return None
    else:
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0]==key:
                return hash_table[hash_address][i][1]
        else:
            return None

save_data("Dd",'1212')
save_data("Data","1231")
save_data("Ddf","123124")
save_data("abc","14514")
print(read_data("Dd"))
print(hash_table)
# key 값을 형성할때 hash() 함수를 썻는데 이건 실행할때마다 달라지므로 결과값이 계속 달라진다
# 간단하게 구성을 보여주기 위하여 hash() 로 사용하였다.