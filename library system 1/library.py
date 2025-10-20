from book import Book
import os

#For O(1) lookups we will make different files for each book and file name would be same as title of book
#Taking title as primary key means it will be unique. No two books can have same title
'''
Data Storing Format in File

Title
Author
Content
Borrower
Availability
'''

class Library:

    def __init__(self, name, location):
        self.__name = name
        self.__location = location 
    
    #add record
    def add_book(self):
        print("\n-----Adding New Record-----\n")
        enter_title = input("Enter Book Title: ").title()
        enter_author = input("Enter Author Name: ").title()
        enter_content = input("Enter Content: ")
        enter_available = True

        file_name = f"./{enter_title.replace(' ', '_')}.txt"

        if os.path.exists(file_name):
            print(f"{enter_title} book already exists in records")
        else:
            book_record = Book(enter_title, enter_author,enter_content, "None", enter_available)

            #will create a new file if not exists
            with open(file_name,'+a') as f:
                f.write(f'{book_record.title}\n')
                f.write(f'{book_record.author}\n')
                f.write(f'{book_record.content}\n')
                f.write(f'{book_record.borrower}\n')
                f.write(f'{str(book_record.is_available)}\n')
            
            print(f"{enter_title} Record Added Successfully")
            

    #delete record     
    def delete_record(self):
        print("\n Deleting Record-----\n")
        enter_title = input("Enter Title of Book You want to Delete Record Of: ")
        
        file_name = f"./{enter_title.replace(" ", "_").lower().title()}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"\n{enter_title} Record Deleted")
        else:
            print("No such record exists.")

    #fetch record
    def fetch_record(self)->str:
        print("\n-----Fetching Record-----\n")
        enter_title = input("Enter Title of Book You want to Fetch Record Of: ")
        data = []
        file_name = f"./{enter_title.replace(" ", "_").lower().title()}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                for line in f.readlines():
                    data.append(line.strip())
                is_available = data[4].strip().lower() == "true"
                book = Book(data[0], data[1], data[2], data[3], is_available)
                
            return str(book)
        return "No such record exists."
    
    #edit record
    def edit_record(self):
        print('\n-----Editing Record-----\n')
        enter_title = input("Enter Book Title: ").title()
        enter_content = input("Update Content: ")

        file_name = f"./{enter_title.replace(' ', '_').lower().title()}.txt"
        data = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                for line in f.readlines():
                    data.append(line.strip())
                is_available = data[4].strip().lower() == "true"
                book = Book(data[0], data[1], enter_content, data[3], is_available)

            #will create a new file if not exists
                with open(file_name,'w') as f:
                    f.write(f'{book.title}\n')
                    f.write(f'{book.author}\n')
                    f.write(f'{book.content}\n')
                    f.write(f'{book.borrower}\n')
                    f.write(f'{str(book.is_available)}\n')

            print(f"\n{book.title} Record Edited")
        else:
            print("No such record exists.")

    def show_titles(self):
        print("\n-----Showing Records-----\n")
        folder_path="./"
        print(f'{self.__name} has following books \n')
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                print("Book Title:", file.replace("_"," ").removesuffix(".txt"))

    def borrow_book(self):
        print("\n-----Lending Book-----\n")
        enter_title = input("Enter Book Title: ").title()
        enter_borrower = input("Enter Borrower Name: ").title()
        
        file_name = f'./{enter_title.replace(" ", "_")}.txt'

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                book_data = [lines.strip() for lines in f.readlines()]

            flag = book_data[4].strip().lower() == "true" # as we are getting string from file
            
            if(flag):
                book = Book( book_data[0],book_data[1],book_data[2],enter_borrower, False)
                with open(file_name, 'w') as f:
                    f.write(f"{book.title}\n")
                    f.write(f"{book.author}\n")
                    f.write(f"{book.content}\n")
                    f.write(f"{book.borrower}\n")
                    f.write(f"{book.is_available}\n")

                print(f'\n{book.title} borrowed by {book.borrower}')
            else:
                print("Book is already borrowed by someone else.")
        else:
            print("No such record exists.")

    def return_book(self):
        print("\n-----Return of Book-----\n")
        enter_title = input("Enter book Title: ").title()
        enter_borrower_name = input("Enter Borrower Name: ").title()
          
        file_name = f'./{enter_title.replace(" ",("_"))}.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                book_data = [lines.strip() for lines in f.readlines()]
            
            if book_data[0] == enter_title and book_data[3]==enter_borrower_name:
                book = Book( book_data[0],book_data[1],book_data[2],"None",True)
                with open(file_name, 'w') as f2:
                    f2.write(f"{book.title}\n")
                    f2.write(f"{book.author}\n")
                    f2.write(f"{book.content}\n")
                    f2.write(f"{book.borrower}\n")
                    f2.write(f"{book.is_available}\n")
                    print(f'\n{book.title} returned by {enter_borrower_name}')
            else:
                print("No such record exists.")
        else:
            print("No such record exists.")

                
            