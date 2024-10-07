class Placeholder:
    def fn():
        print("Placeholder")

class InputManager:
    bookEngine = Placeholder()
    borrowerEngine = Placeholder()

    def __init__(self, bookEngine, borrowerEngine):
        self.bookEngine = bookEngine
        self.borrowerEngine = borrowerEngine

    def print_init_message(self):
        print("How to use the CLI Libary:")
            
        print("\nBasics ****************************************************************************************")
        print("Quitting:\t\t\t \"q\"")
        
        print("\nBooks *****************************************************************************************")
        print("Adding books:\t\t\t \"add book, <book name>, <authors (comma separated)>, <ISBN>, <# of pages>\"")
        print("Removing books:\t\t\t \"rm book, <ISBN>\"")
        print("Edit books:\t\t\t \"edit book, <ISBN>, <new name>, <new authors (comma separated)>, <new # of pages>\"")
        
        print("\nQuerying Books ********************************************************************************")
        print("Search for books:\t\t \"search books, <search type (name, author, isbn)>, <query>\"")
        print("List all books (sorted):\t \"list books, <sort type (name, author, isbn, page count)>\"")
        
        print("\nBorrowing *************************************************************************************")
        print("Add Borrower:\t\t\t \"add borrower, <name>, <username>, <phone>\"")
        print("Delete Borrower:\t\t \"rm borrower, <username>\"")
        print("Edit Borrower:\t\t\t \"edit borrower, <username>, <new name>, <new phone>\"")
        print("Checkout:\t\t\t \"checkout book, <isbn>, <borrower username>\"")
        print("Return:\t\t\t\t \"return book, <isbn>\"")
        print("View book's borrower:\t\t \"borrower of, <isbn>\"")
        print("View # of borrower's books:\t \"borrowed by, <username>\"")

        print("\nQuerying Borrowers ****************************************************************************")
        print("Search for borrowers:\t\t \"search borrowers, <search type (name, username)>, <query>\"\n")

    def handle_input(self, input):
        splitInput = input.split(", ")

        if len(splitInput) < 2:
            print("Please provide a valid input.\n")
            return

        command = splitInput[0]

        if "book" in command.lower() or "borrower of" == command.lower():
            self.bookEngine.handle_input(command, args=splitInput[1:])
        elif "borrower" in command.lower() or "borrowed by" == command.lower():
            self.borrowerEngine.handle_input(command, args=splitInput[1:])
        else:
            print("The operation failed.\n")
