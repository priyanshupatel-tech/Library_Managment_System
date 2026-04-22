book=["Data Structure","Python","Java Script"]
def menu():
    print("\n=============== Menu ==============")
    print("1.Add Book","\n2.View Book","\n3.Search Book","\n4.Issue Book","\n5.Return Book","\n6.Exit")
def view_books():
    print(*book,sep=",",end=".")
    return book
def add_book(book):
    addbook=input("Enter your book name =")
    title_addbook=addbook.title()
    book.append(title_addbook)
    print("Book Added Sussesfully!")
    return book
def search_book(book):
    search=input("Enter Search Book name =")
    search_title=search.title()
    for books in book:
        if books==search_title:
            searchfound=1
            break
        else:
            searchfound=0
    if searchfound==1:
        print("Book Available")
    else:
        print("Book Not Available !")
def issue_book(book):
    issue=input("Enter Issue Book Name=")
    issue_title=issue.title()
    for issues in book:
        if issues==issue_title:
            found=0
            break
        else:
            found=1
    if found==0:
        book.remove(issue_title)
        print("Book Issued!")
    else:
        print("Book not Available")
def return_book(book):
    returnbook=input("Enter Return Book Name=")
    book.append(returnbook)
    print("Thanks You for return book ")
    return book





print ("=============Library Managment System===============") 
while True:
    menu()
    choice1=input("Enter Your Choice=")
    choice=choice1.upper()
    if choice=="ADD BOOK" or choice=="1":
        add_book(book)
    elif choice=="VIEW BOOK" or choice=="2":
        view_books()
    elif choice=="SEARCH BOOK" or choice=="3":
        search_book(book)
    elif choice=="ISSUE BOOK" or choice=="4":
        issue_book(book)
    elif choice=="RETURN BOOK" or choice=="5":
        return_book(book)
    elif choice=="EXIT" or choice=="6":
        print("Thank You \nVisit Again")
        break
    else:
        print("Wrong Input!\nPlease Correct Your Input Spelling")