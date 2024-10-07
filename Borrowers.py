class BorrowerEngine:
    def handle_input(self, command: str, args: list[str]):
        print("Command: " + command)
        for arg in args:
            print("Args: " + arg + "\n")