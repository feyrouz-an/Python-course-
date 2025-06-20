#sum of the first N numbers
try:
    total = 0
    while True:
        N = input("Enter a number (or 'quit' to finish): ")
        if N.lower() == 'quit':
            break
        if int(N) < 0:
            print("Negative numbers are not allowed, please try again.")
            continue
        total += int(N)
    print(f"The total is: {total}")
except Exception as e:
    print(f"An error occurred: {e}")
