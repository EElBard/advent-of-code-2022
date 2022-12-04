maxCalories = 0

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readLines()
    current = 0
    
    for line in lines:
        if line.strip():
            current += line
        else:
            if current > maxCalories:
                maxCalories = current
            current = 0

print(maxCalories)