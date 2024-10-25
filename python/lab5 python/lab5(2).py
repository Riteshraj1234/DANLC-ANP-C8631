def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    return sum == n

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end+1):
    if is_armstrong(num):
        print(num)