# User function Template for python3

def utility():
    # The line below takes input. Don't change it!
    x = int(input())
    
    # Complete the code below
    while x >= 0:
        # Print the number followed by a space
        print(x, end=" ")
        # Decrement x
        x -= 1

# Driver Code
def main():
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while testcases > 0:
        utility()
        print()  # This gives a new line
        testcases -= 1

if __name__ == '__main__':
    main()
