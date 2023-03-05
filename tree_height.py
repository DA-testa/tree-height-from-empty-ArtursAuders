import sys
import threading


def compute_height(n, parents):
    # Create an array to store the height of each node
    heights = [0] * n

    # Find the height of each node by traversing the tree bottom-up
    # Iterate through each node and compute its height
    for node in range(n):
        # Check if the node height has already been computed
        if heights[node] != 0:
            continue

        # If the node has no parent, its height is 1
        if parents[node] == -1:
            heights[node] = 1
        else:
            # Otherwise, compute the parent's height and add 1
            parent_height = compute_height(parents[node], parents)
            heights[node] = parent_height + 1

    # Return the maximum height
    return max(heights)



def main():
# Ask user for input method
    input_method = input("Enter input method (K for keyboard or F for file): ")
    
    # Check if input method is valid
    while input_method.upper() not in ['K', 'F']:
        input_method = input("Invalid input method. Enter K or F: ")

    # Get input from keyboard
    if input_method.upper() == 'K':
        # Input number of nodes
        n = int(input("Enter number of nodes: "))

        # Input parents array
        parents = list(map(int, input("Enter parents array: ").split()))

    # Get input from file
    else:
        # Ask user for file name
        file_name = input("Enter file name (without 'a' in name): ")

        # Check if file name is valid
        while 'a' in file_name or file_name.upper() == 'README':
            file_name = input("Invalid file name. Enter another name: ")

        # Try to read file and get input
        try:
            with open('folder/' + file_name, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))

        # Catch file not found error
        except FileNotFoundError:
            print("File not found.")
            return

    # Compute and print tree height
    print("Tree height:", compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
