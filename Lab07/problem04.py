try:
    with open("sample.txt", "w") as file:
        file.write("Hello Python\n")

    with open("sample.txt", "a") as file:
        file.write("Welcome to AIUB Python Lab.\n")

    with open("sample.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)