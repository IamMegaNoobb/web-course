def main():
    with open('output.txt', 'w') as file:
        file.write('Hello, World!\n')
        file.write('This is a test file.\n')
        file.write('Goodbye!\n')
    print("File written successfully.")

if __name__ == "__main__":
    main()