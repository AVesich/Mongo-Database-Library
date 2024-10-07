class BookEngine:
    def handle_input(self, command: str, args: list[str]):
        print("Command: " + command + "\n")
        for arg in args:
            print("Args: " + arg + "\n")