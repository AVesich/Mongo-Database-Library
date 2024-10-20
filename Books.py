import pymongo
import Shared
from Shared import client

class BookEngine:
    db = client['library'] # Library db

    def add_book(self, args: list[str]): # name, authors, isbn, # of pages
        arg_count = len(args)
        if arg_count < 4:
            print("Not enough args provided. Minimum 4 args.")
            return
            
        self.db.books.insert_one({
            'name' : args[0],
            'authors' : args[1:arg_count-2],
            'ISBN': args[arg_count-2],
            'num_pages': args[arg_count-1]
        })
        print("Book added!")

    def remove_book(self, args: list[str]): # isbn
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return

        result = self.db.books.delete_one({'ISBN':args[0]})
        print(result.deleted_count)
        print("Book removed!" if (result.deleted_count > 0) else "No book found!")

    def edit_book(self, args: list[str]): # isbn, new name, new authors, new # of pages
        arg_count = len(args)
        if arg_count < 4:
            print("Not enough args provided. Minimum 4 args.")
            return

        result = self.db.books.update_one({ 'ISBN':args[0] },
                                          { '$set': {'name':args[1],
                                                     'authors':args[2:arg_count-1] ,
                                                     'num_pages': args[arg_count-1]}
                                          })

        print("Book updated!" if (result.modified_count > 0) else "No books found to update!")

    def search_books(self, args: list[str]): # search type, query
        arg_count = len(args)
        if arg_count != 2:
            print("Incorrect # of args. 2 must be provided.")
            return

        if args[0].lower() == "name":
            results = self.db.books.find({ 'name' : args[1] })
        elif args[0].lower() == "author":
            results = self.db.books.find({ 'authors' : args[1] })
        elif args[0].lower() == "isbn":
            results = self.db.books.find({ 'ISBN' : args[1] })
        else:
            print("Please enter a valid search type: 'name', 'author', 'isbn'.")
            return
        
        for result in results:
            response = "Name: " + result['name'] + ",   Authors: "
            for author in result['authors'] :
                response += author + ", "
            if len(result['authors']) > 0:
                response = response [0:len(response)-2]
            response += ",   ISBN: " + result['ISBN']
            response += ",   # of pages: " + result['num_pages']
            print(response)

    def list_books(self, args: list[str]): # sort type
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return
        
        if args[0].lower() == "name":
            results = self.db.books.find().sort('name', pymongo.ASCENDING)
        elif args[0].lower() == "author":
            results = self.db.books.find().sort('authors', pymongo.ASCENDING)
        elif args[0].lower() == "isbn":
            results = self.db.books.find().sort('ISBN', pymongo.ASCENDING)
        elif args[0].lower() == "page count":
            results = self.db.books.find().sort('num_pages', pymongo.ASCENDING)
        else:
            print("Please enter a valid search type: 'name', 'author', 'isbn', 'page count'.")
            return
        
        for result in results:
            response = "Name: " + result['name'] + ",   Authors: "
            for author in result['authors'] :
                response += author + ", "
            if len(result['authors']) > 0:
                response = response [0:len(response)-2]
            response += ",   ISBN: " + result['ISBN']
            response += ",   # of pages: " + result['num_pages']
            print(response)

    def checkout_book(self, args: list[str]): # isbn, username
        arg_count = len(args)
        if arg_count != 2:
            print("Incorrect # of args. 2 must be provided.")
            return
        
        print("Book checked out to borrower!")

    def return_book(self, args: list[str]): # isbn
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return
        
        print("Book returned to the library!")

    def check_borrower_of_book(self, args: list[str]): # isbn
        arg_count = len(args)
        if arg_count != 1:
            print("Incorrect # of args. 1 must be provided.")
            return
        
        print("Book not borrowed!")

    possible_commands = {
        "add book" : add_book,
        "rm book" : remove_book,
        "edit book" : edit_book,
        "search books" : search_books,
        "list books" : list_books,
        "checkout book" : checkout_book,
        "return book" : return_book,
        "borrower of" : check_borrower_of_book
    }

    def handle_input(self, command: str, args: list[str]):
        self.possible_commands[command](self, args)
