# File Read & Write Challenge 🖋️
def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f_in:
            content = f_in.read()
        
        # Example modification: convert to uppercase
        modified_content = content.upper()
        
        with open(output_file, "w") as f_out:
            f_out.write(modified_content)
        
        print(f" Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f" The file '{input_file}' does not exist.")
    except Exception as e:
        print(f" An error occurred: {e}")


# Example usage
modify_file("input.txt", "output.txt")


# Error Handling Lab 
def read_user_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as f:
            print("\n File content:\n")
            print(f.read())
    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f" Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Example usage
read_user_file()
