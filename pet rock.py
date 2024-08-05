class PetRock:
    def __init__(self, name):
        self.name = name
    
    def sit(self):
        return f"{self.name} is sitting still."

    def stay(self):
        return f"{self.name} stays perfectly still."

    def roll_over(self):
        return f"{self.name} doesn't move, but you imagine it rolling over."

    def respond(self, command):
        command = command.lower()
        if command == "sit":
            return self.sit()
        elif command == "stay":
            return self.stay()
        elif command == "roll over":
            return self.roll_over()
        else:
            return f"{self.name} doesn't understand the command."

# Create a virtual pet rock
rocky = PetRock("Rocky")

# Interactive loop to give commands to the pet rock
while True:
    command = input("Enter a command for your pet rock (sit, stay, roll over) or 'quit' to exit: ")
    if command.lower() == "quit":
        print("Goodbye!")
        break
    print(rocky.respond(command))
