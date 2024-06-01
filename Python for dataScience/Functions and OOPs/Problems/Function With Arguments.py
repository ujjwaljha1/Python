#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

#Write the complete argumentFunction below.
#The function should take two arguments a and b
#The function should have only one statement
#print(a+b)



def argumentFunction(a, b):
    print(a + b)


#Write the complete argumentFunction above.
#The function should take two arguments a and b
#The function should have only one statement
#print(a+b)

#{ 
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        a=int(input())
        b=int(input())
        argumentFunction(a,b)
        t-=1

if __name__ == "__main__": 
    main()
# } Driver Code Ends