import os
from server import Server

while True:
    try:
        # Wait for user input
        user_input = input("Enter command: ").strip()

        # Check for various commands
        if user_input.lower() == "hello":
            print("Hello there!")

        elif user_input.lower() == "help":
            print("Here are the available commands: hello, help, clear, ls, cd")

        elif user_input.lower() == "clear":
            # Clear the terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')

        elif user_input.lower() == "start teacher":
            italianTeacher = Server(maxTokensPrompt=40, maxTokensResponse=40)
            italianTeacher.startConversation()
        
        elif user_input.lower() == "exit":
            print("Exiting terminal...")
            break

        else:
            print("Invalid command. Type 'help' to see the available commands.")

    except KeyboardInterrupt:
        # Handle Ctrl+C interrupt
        print("\nKeyboardInterrupt. Type 'exit' to quit.")
    except Exception as e:
        print(f"Error: {e}")