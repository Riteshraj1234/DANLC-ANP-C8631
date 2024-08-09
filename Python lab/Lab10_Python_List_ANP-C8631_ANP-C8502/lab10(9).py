# Given two lists `a = [1, 2, 3]` and `b = [4, 5, 6]`,
# write code to merge them into a single list and then flatten a list of lists `c = [[1, 2], [3, 4], [5, 6]]`
# into a single list.
a = [1, 2, 3]
print(f"A = {a}")
b = [4, 5, 6]
print(f"B = {b}")
c = a + b
print(F"Merge list = {c}")
list_of_lists = [c[i:i + 2] for i in range(0, len(c), 2)]
print("List of lists:", list_of_lists)


