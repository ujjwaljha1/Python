#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
def sequence(numbers):
    # Extracting the common difference from the given sequence
    diff = numbers[1] - numbers[0]
    
    # Extending the sequence by calculating the next three numbers
    next_three = [numbers[-1] + diff * (i + 1) for i in range(3)]
    
    # Returning the whole sequence as a tuple
    return numbers + tuple(next_three)
 
    # code here to return tuple containing whole sequences

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers =tuple([int(x) for x in input().strip().split()])
        
        ans = sequence(numbers)
        
        if type(ans) != tuple:
            print('your ans is not tuple')
        else:
            print(*ans)

# } Driver Code Ends