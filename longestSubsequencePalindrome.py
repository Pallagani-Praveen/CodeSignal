# Question Link : https://app.codesignal.com/challenge/eCMYRLHNSS8AJBP7S
# Solution is given Below
def longestSubsequencePalindrome(a):
    d=dict()
    return f(a,0,len(a)-1,d)

def f(a,i,j,d):
    #  recursive dp problem involving memorisation

        if i>j:
            return 0
        if i==j:
            return 1
        k = (i,j)

        if k not in d:
            # a dynamic programming problem
            
            if a[i]==a[j]:
                # start : if end are equal add length 2 and check for middle portion
                d[k] = f(a,i+1,j-1,d) + 2
            else:
                # trying the possible ways and fix the max one
                d[k] = max(f(a,i+1,j,d),f(a,i,j-1,d))

        return d[k]

print('Max Possible Palindrome Length :',longestSubsequencePalindrome([1,2,3,1])) # [1,2,1] or [1,3,3] 

