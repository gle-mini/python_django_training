def read_and_print_numbers():
    try:
        with open('numbers.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.replace(',', '\n').strip())
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_and_print_numbers()

