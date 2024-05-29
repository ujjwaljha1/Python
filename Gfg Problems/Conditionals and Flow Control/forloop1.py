def utility():
    n = int(input())
    # Using range(1, 11) to generate numbers from 1 to 10
    for i in range(1, 11):
        # Print the multiplication result followed by a space
        print(i * n, end=" ")
        
# Driver code to test the function
def main():
    testcases = int(input()) # testcases
    while testcases > 0:
        utility()
        print() # To give a new line after each test case
        testcases -= 1

if __name__ == '__main__':
    main()
