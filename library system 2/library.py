from book import Book
import os
import pickle #will help in writing and reading whole object in .pkl file

#For O(1) lookups we will make different files for each book and file name would be same as title of book
#Taking title as primary key means it will be unique. No two books can have same title


#Using pickle for serialization and deserialization
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
        enter_borrower= input("Enter Borrower Name: ").title()
        enter_available = True if enter_borrower=="None" else False

        file_name = f"./{enter_title.replace(' ', '_')}.pkl"

        if os.path.exists(file_name):
            print(f"{enter_title} book already exists in records")
        else:
            book_record = Book(enter_title, enter_author,enter_content, enter_borrower, enter_available)
            #will create a new file if not exists and stores whole object after serializing it
            with open(file_name, "wb") as f:
                pickle.dump(book_record, f)
            
            print(f"{enter_title} Record Added\n")

    #delete record     
    def delete_record(self):
        print("\n Deleting Record-----\n")
        enter_title = input("Enter Title of Book You want to Delete Record Of: ")
        
        file_name = f"./{enter_title.replace(" ", "_").lower().title()}.pkl"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{enter_title} Record Deleted\n")
        else:
            print("No such record exists.")

    #fetch record
    def fetch_record(self)->str:
        print("\n-----Fetching Record-----\n")
        enter_title = input("Enter Title of Book You want to Fetch Record Of: ")
        file_name = f"./{enter_title.replace(" ", "_").lower().title()}.pkl"
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                loaded_book = pickle.load(f) #the whole book object is retrieved and we can easily return it no need to create a new book object
            return str(loaded_book)
        return "No such record exists."
    
    #edit record
    def edit_record(self):
        print('\n-----Editing Record-----\n')
        enter_title = input("Enter Book Title: ").title()
        enter_author = input("Enter Author Name: ").title()
        enter_content = input("Update Content: ")
        enter_borrower= input("Update Borrower Name(if book returned put None): ").title()
        enter_available = True if enter_borrower == "None" else False

        file_name = f"./{enter_title.replace(' ', '_').lower().title()}.pkl"

        if os.path.exists(file_name):
            book_record = Book(enter_title,enter_author,enter_content, enter_borrower, enter_available)
            #will create a new file if not exists
            with open(file_name,'wb') as f:
                pickle.dump(book_record,f)
            print(f'{enter_title} Record Edited\n')
        else:
            print("No such record exists.")

    def show_titles(self):
        print("\n-----Showing Records-----\n")
        folder_path="./"
        print(f'{self.__name} has following books \n')
        for file in os.listdir(folder_path):
            if file.endswith(".pkl"):
                print("Book Title:", file.replace("_"," ").removesuffix(".pkl"))

    def borrow_book(self):
        print("\n-----Lending Book-----\n")
        enter_title = input("Enter Book Title: ").title()
        enter_borrower = input("Enter Borrower Name: ").title()
        
        file_name = f'./{enter_title.replace(" ", "_")}.pkl'

        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                book_data = pickle.load(f)
            
            if(book_data.is_available):
                book_record= Book(book_data.title,book_data.author,book_data.content,enter_borrower, False)
                with open(file_name, 'wb') as f:
                    pickle.dump(book_record,f)

                print(f'{book_record.title} borrowed by {book_record.borrower}')
            else:
                print("Book is already borrowed by someone else.")
        else:
            print("No such record exists.")

    def return_book(self):
        print("\n-----Return of Book-----\n")
        enter_title = input("Enter book Title: ").title()
        enter_borrower_name = input("Enter Borrower Name: ").title()
          
        file_name = f'./{enter_title.replace(" ",("_"))}.pkl'
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                book_data = pickle.load(f)
            
            if book_data.title == enter_title and book_data.borrower==enter_borrower_name:
                book = Book( book_data.title,book_data.author,book_data.content,"None",True)
                with open(file_name, 'wb') as f:
                    pickle.dump(book,f)
                    
            else:
                print("No such record exists.")
        else:
            print("No such record exists.")

                
            