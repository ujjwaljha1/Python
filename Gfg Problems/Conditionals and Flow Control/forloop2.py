def utility():
    # The line below takes input. Don't change it!
    s = input().strip()
    
    # Loop through the string with step of 2 to get characters at even indices
    for i in range(0, len(s), 2):
        print(s[i], end="")  # Printing character and separating characters by nothing

# Driver code to test the function
def main():
    testcases = int(input())  # Number of test cases
    while testcases > 0:
        utility()
        print()  # Separating test case outputs by newlines
        testcases -= 1

if __name__ == '__main__':
    main()
