import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # ask the user for input type
    input_type = input("Enter input type (F for file or K for keyboard): ").upper()
    if input_type == 'F':
        # ask the user for the filename
        filename = input("Enter filename: ")
        # check if the filename has the letter 'a'
        if 'a' in filename:
            print("Error: Filename contains the letter 'a'.")
            return
        try:
            with open(filename, 'r') as f:
                # read the number of elements
                n = int(f.readline().strip())
                # read the values and split them into an array
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("Error: File not found.")
            return
    elif input_type == 'K':
        # read the number of elements
        n = int(input("Enter number of elements: "))
        # read the values and split them into an array
        parents = list(map(int, input("Enter values: ").strip().split()))
    else:
        print("Error: Invalid input type.")
        return

    # call the function and output its result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(107)  # max depth of recursion
threading.stack_size(227)   # new thread will get stack of such size
threading.Thread(target=main).start()
