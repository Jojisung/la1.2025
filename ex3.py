numbers = list(range(1,101))
rows = 4
per_row = len(numbers) // rows  

for i in range(rows):
    start = i * per_row
    
    if i == rows - 1:
        end = len(numbers)
    else:
        end = (i + 1) * per_row
    print(*numbers[start:end])