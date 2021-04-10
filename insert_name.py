import mysql.connector as pysql



def insert_values_captains(data):
    
    for j in data:
        db=pysql.connect(host='localhost',user='root',passwd='2234841',database='election')
        cur=db.cursor()
        a=f'insert into captains values(%s,%s)'
        cur.execute(a,(j["Id"],j["name"]))
        db.commit()

def insert_values_vicecaptains(data):
    
    for j in data:
        db=pysql.connect(host='localhost',user='root',passwd='2234841',database='election')
        cur=db.cursor()
        a=f'insert into vicecaptains values(%s,%s)'
        cur.execute(a,(j["Id"],j["name"]))
        db.commit()



print('CAPTAINS : 1')
print('VICE CAPTAINS : 2')
who=int(input('Enter position: '))

n=int(input('enter no of candidates: '))
dataD={}
data=[]
for i in range(n):
    dataD['Id']=int(input('enter id'))
    dataD['name']=input('enter name')
    data.append(dataD)
    dataD={}
print(data)

if who ==1:
    insert_values_captains(data)
elif who == 2:
    insert_values_vicecaptains(data)


    