
import mysql.connector as i

log=i.connect(host="localhost",user="root",password="root",database="library")

def viewbook():

    c=log.cursor()
    c.execute("select * from books")
    result= c.fetchall()
    for row in result:
        print(row)
        print("\n")

def addbook():
    bid=input("Enter the book ID:")
    bnm=input("Enter the book name:")
    bauth=input("Enter the name book's author:")
    bpub=input("Enter the book's publisher:")
    bsts=input("If available or not(Y/N):")
    data = (bid,bnm,bauth,bpub,bsts)
    sql='insert into books values(%s,%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Book(s) Added sucessfully")

def deletebook():
    bc=input("Enter the book ID:")
    
    B=(bc,)

    c=log.cursor()
    sql=("select B_Avilable from books where B_ID=%s")
    c.execute(sql,B)
    res=c.fetchall()
    
    if 'Y' and 'y' and 'N' and 'n' in res[0]:
        
        B=(bc,)
        sq=("delete from books where B_ID=%s")
        
        c=log.cursor()
        c.execute(sq,B)
        log.commit()

        print("Successfully Deleted the Entry.")
        
        
    else:
        print("Either book isnt avilable or code is wrong:")
        deletebook()