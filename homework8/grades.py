filename = "grades.csv"
mode = "r"
contents = "" 

#read each line strip \n and split by comma 

with open(filename, mode) as f:
    lines = [line.strip("\n").split(",") for line in f.readlines()]
    print(lines)

# calculate average for each student

with open(filename, mode) as f:
    for line in f:
        parts = line.strip().split(",")
        name = parts[0]
        scores = list(map(int, parts[1:]))
        average = sum(scores) / len(scores)
        print(f"{name}: Average score = {average:.2f}")

#new file average.csv , pass/fail 

filename = "average.csv"
mode = "a"
with open(filename, mode) as f:
    for line in lines:
        name = line[0]
        scores = list(map(int, line[1:]))
        status = "Pass" if average >= 50 else "Fail"
        f.write(f"{name},{average:.2f},{status}\n")
