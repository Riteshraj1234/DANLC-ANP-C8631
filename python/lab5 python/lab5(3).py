def print_multiplication_tables(start, end):
    for num in range(start, end + 1):
        print(f"Multiplication Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print()  # Print an empty line after each table


start_range = 2
end_range = 5
print_multiplication_tables(start_range, end_range)



