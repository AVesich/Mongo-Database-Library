import pymongo
import Shared
from Shared import client

class BorrowerEngine:

    db = client['library'] # Library db

    def add_borrower(self, args: list[str]): # name, username, phone
        arg_count = len(args)
        if arg_count != 3:
            print("Incorrect # of args. 3 must be provided.")
            return
        
        self.db.borrowers.insert_one({
            'name': args[0],
            'username': args[1],
            'phone': args[2]
        })
        print("Borrower added!")

    def remove_borrower(self, args: list[str]): # username
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return
        
        result = self.db.borrowers.delete_one({'username': args[0]})

        print("Borrower removed!" if (result.deleted_count > 0) else "No borrower found!")

    def edit_borrower(self, args: list[str]): # username, new name, new phone
        arg_count = len(args)
        if arg_count != 3:
            print("Incorrect # of args. 3 must be provided.")
            return
        
        self.db.borrowers.update_one({'username': args[0]},
                                     { '$set': {'name': args[1],
                                                'phone': args[2]}
                                     })

        print("Borrower updated!")

    def check_books_borrowed_by(self, args: list[str]): # username
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return
        
        # Check if the borrower exists
        user = self.db.borrowers.find_one({"username":args[0]})
        if user is None:
            print("The borrower " + args[0] + " does not exist.")
            return
        
        booksBorrowedByUser = self.db.books.find({"borrower":args[0]})
        books = []
        for book in booksBorrowedByUser:
            books.append(book)
        
        if len(books) == 0:
            print(args[0] + " has 0 books checked out.")
        else:
            result = args[0] + " currently has checked out "
            for book in books:
                result += book["name"] + " (ISBN " + book["ISBN"] + "), "
            result = result[0:len(result)-2]
            print(result)

    def search_borrowers(self, args: list[str]): # search type, query
        arg_count = len(args)
        if arg_count != 2:
            print("Incorrect # of args. 2 must be provided.")
            return

        if args[0].lower() == "name":
            results = self.db.borrowers.find({ 'name' : args[1] })
        elif args[0].lower() == "username":
            results = self.db.borrowers.find({ 'username' : args[1] })
        else:
            print("Please enter a valid search type: 'name', 'author', 'isbn'.")
            return
        
        for result in results:
            print("Name: " + result['name'] + ",   Username: " + result['username'] + ",   Phone number: " + result['phone'])

    possible_commands = {
        "add borrower" : add_borrower,
        "rm borrower" : remove_borrower,
        "edit borrower" : edit_borrower,
        "borrowed by" : check_books_borrowed_by,
        "search borrowers" : search_borrowers
    }

    def handle_input(self, command: str, args: list[str]):
        self.possible_commands[command](self, args)