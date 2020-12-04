"""

배열(Array): 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
장점 : 빠른 접근 가능(인덱스 번호로 접근)
단점 : 데이터 추가/삭제의 어려움 (미리 최대길이를 지정해놓기 때문이다.)

"""

# 1차원 배열
data_list = [1,2,3,4,5]
print(data_list[1])

# 2차원 배열
data_list = [[1,2,3],[4,5,6],[7,8,9]]
print(data_list[1][1])
print(data_list[0][1])

# 다음 dataset 리스트에서 전체 이름 안에 M은 몇번 나왔는지 빈도수 출력하기
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

m_count=0
for data in dataset:
    for index in range(len(data)):
        if data[index]=="m":
            m_count+=1
print(m_count)

m_count=0
for data in dataset:
    m_count+=data.count("m")
print(m_count)