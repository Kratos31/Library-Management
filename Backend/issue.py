import mysql.connector as i

from datetime import datetime


log=i.connect(host="localhost",user="root",password="root",database="library")


def viewissues():

    c=log.cursor()
    c.execute("select * from issue")
    result= c.fetchall()
    for row in result:
        print(row)
        print("\n")

def issuebook():
    iid=input("Enter issue ID:")
    mmid=input("Enter member ID:")
    bc=input("Enter the book ID:")
    
    B=(bc,)

    c=log.cursor()
    sql=("select B_Avilable from books where B_ID=%s")
    c.execute(sql,B)
    res=c.fetchall()

   
    
    for i  in res[0]:
        if i =='y' or 'Y' or'n' or 'N':
            adate=input("Enter book issue date (MM-DD-YYYY):")
            bdate=input("Enter due date(MM-DD-YYYY):")

            idate=datetime.strptime(adate, '%m-%d-%Y')
            duedate=datetime.strptime(bdate, '%m-%d-%Y')
            
            data=(iid,mmid,bc,idate,duedate)
            sq=("insert into issue values(%s,%s,%s,%s,%s)")
            
            c=log.cursor()
            c.execute(sq,data)
            log.commit()
            print("Book issued successfully!")
            
            
            data=(B)
            sq=("update books set B_Avilable= replace(B_Avilable, 'Y','N') where B_ID=%s")
            c=log.cursor()
            c.execute(sq,data)
            log.commit()
        else:
            print("Either book isnt avilable or code is wrong:")
            issuebook()

def bookupdate():
    bc=input("Enter book id:")
    B=(bc,)
    data=(B)
    sq=("update books set B_Avilable= replace(B_Avilable, 'N','Y') where B_ID=%s")
    c=log.cursor()
    c.execute(sq,data)
    log.commit()

def deleteissue():
    bc=input("Enter the issue ID:")
    try:
      B=(bc,)
      sq=("delete from issue where I_ID=%s")
      c=log.cursor()
      c.execute(sq,B)
      log.commit()
      print("Successfully Deleted the Entry.")
    except:
        print("Either issue number is incorrect or there is no book issued by the given Issue ID")
        deleteissue()


