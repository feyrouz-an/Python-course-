def even_number(n):
    if n % 2 == 0:
        return True
    else:
        return False

even_numbers = []

while True:
    entry = input("Enter a number (or 'q' to quit): ").strip()
    if entry.lower() == 'q':
        break
    try:
        number = int(entry)
        if even_number(number):
            even_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
print(f"Even numbers entered: {even_numbers}")