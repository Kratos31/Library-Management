from Backend.book import *
from Backend.issue import *
from Backend.member import *


def main():
    print("1. Enter Book menu(1)")
    print("2. Enter Library-member menu(2)")
    print("3. Enter Book-issue menu(3)")
    print("4. Exit(4)")

    res=input("Enter your response here:")


    if res == '1' :
        bookm()
    elif res=='2' :
        memmen()
    elif res== '3' :
        ishmen()
    elif res=='4':
        exit()
    else:
        print("Invalid input")
        main()



def bookm():
    print("To view books(1):")
    print("To add book(2):")
    print("To Delete Book(3)")
    
    
    an=input("Enter your response here:")

    if an=='1':
        print("The book details are in order of (Book ID, Book name, Book Author,Book publisher,Avilable(yes/no))")
        viewbook()
        main()
    elif an=='2':
        print("--------------------You are in Add Book menu--------------------")
        addbook()
        main()
    elif an=='3':
        print("Delete a Book Entry(3)")
        deletebook()
        main()
    else:
        print("Invalid input")
        main()

def ishmen():
    print("View issue database(1):")
    print("Issue a book(2)")
    
    an=input("Enter your response here:")

    if an=='1':
        print("The Issue details are in order of (Issue ID,Member ID,book code,Issue date,Due date)")
        viewissues()
        main()
    elif an=='2':
        print("--------------------You are in Create Issue menu--------------------")
        issuebook()
        main()
    
    else:
        print("Invalid input")
        main()

def memmen():
    print("View Library Members(1):")
    print("Add a Member(2)")
    an=input("Enter your response here:")

    if an=='1':
        print("The Member details are in order of: \n-----------------(Member ID,Member name,DOB,Address,Status)------------------- \n")
        viewmemb()
        main()
    elif an=='2':
        print("--------------------You are in Add Member menu--------------------")
        memberadd()
        main()
    else:
        print("Invalid input")
        main()


    
main()