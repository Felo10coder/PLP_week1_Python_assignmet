# file_read_write.py

# Open the file in read mode
with open("input.txt", "r") as infile:
    content = infile.read()

# modification: make everything uppercase
modified_content = content.upper()

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified version written to output.txt")


# error_handling_lab.py

filename = input("Enter the filename you want to read (input.txt or output.txt): ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You don’t have permission to read '{filename}'.")


