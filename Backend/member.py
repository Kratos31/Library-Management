import mysql.connector as i

from datetime import datetime  #imported datetime function to convert strings into datetime objects

log=i.connect(host="localhost",user="root",password="root",database="library")

def viewmemb():

    c=log.cursor()
    c.execute("select * from member")
    result= c.fetchall()
    for row in result:
        print(row)
        print("\n")

def memberadd():
    mi=input("Enter member id given by admin:")
    
    n=input("Enter your name:")
    print("Enter the date in sequence of MM-DD-YYYY")
    d=(input("Enter the date:"))


    dat=datetime.strptime(d, '%m-%d-%Y')  #strptime function in python converts string into datetime objects
    
    
    phno=int(input("Enter your phone no.:"))

    ader=input("Enter your address:")

    wr=input("Enter if you are a student or staff:")
    
    data=(mi,n,dat,phno,ader,wr)
    print(data)
    sql=("insert into member values (%s,%s,%s,%s,%s,%s)")
    c=log.cursor()
    c.execute(sql,data)
    log.commit()

    print("Member added successfully")

def removemem():
    bc=input("Enter the Member ID:")
    try:
      B=(bc,)
      sq=("delete from issue where Mem_ID=%s")
      c=log.cursor()
      c.execute(sq,B)
      log.commit()
      print("Successfully Deleted the Entry.")
    except:
        print("Either issue number is incorrect or there is no book issued by the given Issue ID")
    deleteissue()