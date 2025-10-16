
from library import Library

class Main:
    @staticmethod
    def main()->None:
        '''main function for our library management system'''

        print("***** WELCOME TO LIBRARY MANAGEMENT SYSTEM *****")
        library = Library("PUCIT NC Library", "Lahore")
        guide = """
        1: Add
        2: Read
        3: Delete
        4: Edit
        5: Show Titles
        6: Borrow
        7: Return
        8: Print Guide
        9: Quit
        """

        print(guide)

        while True:
            choice = input("Enter your choice (1-9): ").strip()

            match choice:
                case "1":
                    library.add_book()
                case "2":
                    book = library.fetch_record()
                    print(book)
                case "3":
                    library.delete_record()
                case "4":
                    library.edit_record()
                case "5":
                    library.show_titles()
                case "6":
                    library.borrow_book()
                case "7":
                    library.return_book()
                case "8":
                    print(guide)
                case "9":
                    print("Exiting... Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1-9.")


if __name__ == "__main__":
    Main.main()