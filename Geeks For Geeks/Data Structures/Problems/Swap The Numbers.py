#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def utility(self, a, b):
        # Swap the values of a and b
        temp = a
        a = b
        b = temp
        
        print(a, b)


#{ 
 # Driver Code Starts.


    

def main():
    t=int(input())
    while(t>0):
        a = int(input())
        b = int(input())
        oj = Solution();
        oj.utility(a, b)
        
        t-=1

if __name__ == "__main__": 
    main()
# } Driver Code Ends