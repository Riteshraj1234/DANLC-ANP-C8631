"""
8. Exception Handling in List Operations
   - Write a function `safe_list_access` that takes a list and an index as arguments and returns the element at that index. Use exception handling to manage:
     - Index out of range.
     - Any other error (provide a generic error message).
        - Test the function with various lists and indices, including valid, negative, and out-of-range indices.
"""
def safe_list_access(input_list, index):
    try:
        return input_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")
    except Exception as e:
        print(f"Error: {e}")

# Test cases
def test_safe_list_access():
    # Test case 1: Valid index
    lst = [100, 200, 300, 400, 900]
    index = 2
    result = safe_list_access(lst, index)
    print(f"Value at index {index}: {result}")
    index = -1
    result = safe_list_access(lst, index)
    print(f"Value at index {index}: {result}")

    # Test case 3: Out of range index
    index = 10
    result = safe_list_access(lst, index)
    print(f"Value at index {index}: {result}")

    # Test case 4: Empty list
    empty_list = []
    index = 0
    result = safe_list_access(empty_list, index)
    print(f"Value at index {index}: {result}")

if __name__ == "__main__":
    test_safe_list_access()
