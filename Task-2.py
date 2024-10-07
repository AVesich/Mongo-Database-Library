import Books
import Borrowers
import Input

input_manager = Input.InputManager(Books.BookEngine(), Borrowers.BorrowerEngine())

input_manager.print_init_message()

while True:
    input_str = input()
    if input_str == "q":
        break
    input_manager.handle_input(input_str)

# add book, Book 1, Austin Vesich, Sriram Mohan, 100, 1020