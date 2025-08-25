# File Read & Write Challenge with Error Handling

# Ask the user for the file name
filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (make everything uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "new_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print("🎉 File has been modified and saved as", new_filename)

except FileNotFoundError:
    print("❌ Error: File not found. Please check the name and try again.")
except Exception as e:
    print("⚠️ Error: Something went wrong ->", e)
