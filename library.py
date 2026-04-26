books = []
issued_books = []
def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print(book,'is added to the library')
def show_books():
    if len(books) == 0:
        print("No books in the library")
    else:
        print("Books in the library:")
        for book in books:
            print(book)
def issue_book():
    book = input("Enter book name to issue: ")
    if book in books:
        books.remove(book)
        issued_books.append(book)
        print(book,'is issued')
    else:
        print(book,'is not available in the library')
def return_book():                  
    book = input("Enter book name to return: ")
    if book in issued_books:
        issued_books.remove(book)
        books.append(book)
        print(book,'is returned')
    else:
        print(book,'is not issued from the library')

    if book in issued_books:
        issued_books. remove (book)
        book. append (book)
        print(' book is returned')
    else:
        print (book,'is not issued')
        

def library():
    while True:
        print('Menu')
        print('1.Add book')
        print('2.Show books')
        print('3.Issue book')
        print('4.Return book')
        print('5.Exit')

        choice = int(input('Enter your choice'))
        if choice==1:
            add_book()
        elif choice==2:
            issue_book()
        elif choice==4:
            return_book()
        elif choice==5:
            print('Thank You!')
            break
        else:
            print('Invalid choice.Please try again')    
library()
