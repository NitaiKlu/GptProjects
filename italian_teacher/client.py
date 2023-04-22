"""
This file contains the implementation of the client of the Italian teacher.
The client is basically a terminal capable of activating the different apps of the server.
The available commands: hello, help, clear, start, exit
Any keyboard interrupt will return to the main terminal of the client. 
"""
import os
from server import Server

# possible apps to run:

def runApp(choiceOfApp):
    if choiceOfApp == '1':
        italianDialouge()
    if choiceOfApp == '2':
        unseen()
    else:
        print("Not a legal choice. \n")

def italianDialouge():
    italianTeacher = Server(mode="conversation")
    italianTeacher.startConversation()

def unseen():
    italianTeacher = Server(mode="unseen", maxTokensResponse=300)
    italianTeacher.startUnseen()

while True:
    try:
        # Wait for user input
        user_input = input("Enter command: ").strip()

        # Check for various commands
        if user_input.lower() == "hello":
            print("Hello there!")

        elif user_input.lower() == "help":
            print("Here are the available commands: hello, help, clear, start, exit")

        elif user_input.lower() == "clear":
            # Clear the terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif user_input.lower() == "start":
            while True:
                # Show the user all of the options to start with:
                print("Choose which kind of conversation you want to have:\n")
                print("1. italian dialogue")
                print("2. unseen mode\n")
                choice = input("Your choice:")
                if choice != "exit":
                    runApp(choice)
                else:
                    break

        elif user_input.lower() == "clean":
            print("Deleting all mp3 files...")
            # Get the current working directory
            dir_path = os.getcwd()
            # Loop through all files in the directory
            for filename in os.listdir(dir_path):
                # Check if the file ends with '.mp3'
                if filename.endswith('.mp3'):
                    # Construct the full path to the file
                    file_path = os.path.join(dir_path, filename)
                    # Delete the file
                    os.remove(file_path)

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

