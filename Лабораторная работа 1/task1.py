numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
inccorect = numbers[4]
correct = 0
numbers[4]=correct
sum = sum (numbers)
total = len (numbers)
average = sum / total
numbers[4]=average

print("Измененный список:", numbers)
