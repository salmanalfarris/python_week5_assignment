def create_and_write_file():
    try:
        # Creating and writing to the file
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("1913\n")
            file.write("This is the third line with a number: 3689.\n")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    try:
        # Reading the file contents
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Appending to the file
        with open("my_file.txt", 'a') as file:
            file.write("This is an appended line.\n")
            file.write("3151\n")
            file.write("Final appended line with text and number: 6176.\n")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
        create_and_write_file()
        read_file()
        append_to_file()
        read_file()
    except Exception as e:
        print(f"An error occurred in the main function: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()