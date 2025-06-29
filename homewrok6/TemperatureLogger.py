temps = []

while True:
    entry = input("Enter a temperature (or 'q' to quit): ").strip()
    if entry.lower() == 'q':
        break
    try:
        temp = float(entry)
        temps.append(temp)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

if temps:
    print(f"Number of readings: {len(temps)}")
    print(f"Highest value: {max(temps)}")
    print(f"Lowest value: {min(temps)}")
    print(f"Average: {sum(temps)/len(temps):.1f}")
else:
    print("No temperature readings were entered.")

