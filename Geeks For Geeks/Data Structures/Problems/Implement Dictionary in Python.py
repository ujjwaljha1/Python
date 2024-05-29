#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def insert_dict(key, value, Dict):
    Dict[key] = value
    print("Inserted")

# deleting from dictionary and print "Deleted" if key present else "-1"
def del_dict(key, Dict):
    if key in Dict:
        del Dict[key]
        print("Deleted")
    else:
        print("-1")

# print marks of student whose name is key if student name is present in Dict else "-1"
def print_dict(key, Dict):
    if key in Dict:
        print("Marks of {} is {}".format(key, Dict[key]))
    else:
        print("-1") 
    

#{ 
 # Driver Code Starts.
# Driver code
def main():
    for _ in range(int(input())):

        Q = int(input())

        Dict = {}
        for i in range(Q):
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query[1], query[2], Dict)
                
            elif(query[0] == 'd'):
                del_dict(query[1], Dict)
                    
            else:
                print_dict(query[1], Dict) 


if __name__ == '__main__':
    main()
# } Driver Code Ends