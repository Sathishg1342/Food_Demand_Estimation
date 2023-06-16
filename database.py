import sqlite3
conn=sqlite3.connect('feedback.db',check_same_thread=False)
c=conn.cursor()
'''c.execute("""CREATE TABLE feedback (
                name text,
                email text,
                message text
                ) """)
res=c.fetchone()'''
'''c.execute("insert into feedback values('abcd','abcd@gmail.com','hai')")'''
def insert_into_db(name,email,message):
    l=len([i for i in c.execute("""select * from feedback""")])
    try:
        c.execute('insert into feedback values(:name,:email,:message)',{'name':name,'email':email,'message':message})
        if (l+1==len([i for i in c.execute("""select * from feedback""")])):
            conn.commit()
            return 1
        else:insert_into_db(name,email,message)
    except:return 0
#insert_into_db('acd','acd@gmail.com','hai')
#c.execute('delete from feedback where email="abcd@gmail.com"')
def delete_from_db(email):
    #for i in c.execute("""select * from feedback"""): print(i)
    l = len([i for i in c.execute("""select * from feedback""")])
    c.execute('delete from feedback where email=:email',{'email':email})
    if (l-1==len([i for i in c.execute("""select * from feedback""")])):
        conn.commit()
        return 1
    else:delete_from_db(email)
#delete_from_db('abcd@gmail.com')
#c.execute('delete from feedback')
conn.commit()
for i in c.execute("""select * from feedback"""): print(i)
