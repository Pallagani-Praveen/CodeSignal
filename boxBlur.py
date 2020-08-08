# Question Link : https://app.codesignal.com/challenge/LNukgzSzfY88RzNjF
# Level : Easy
# Solution is right below:-

def boxBlur(image):
    def helper(image,i,j):
        r_one = image[i-1][j-1]+image[i-1][j]+image[i-1][j+1]
        r_two = image[i][j-1]+image[i][j]+image[i][j+1]
        r_three = image[i+1][j-1]+image[i+1][j]+image[i+1][j+1]
        return (r_one+r_two+r_three)//9
        
    row,col = len(image),len(image[0])
    res = [ [ 0 for j in range(col-2)] for i in range(row-2)] 
    for i in range(1,row-1):
        for j in range(1,col-1):
            val = helper(image,i,j)
            res[i-1][j-1] = val
    return res
    
print('Result : ',boxBlur([[1,1,1], [1,7,1], [1,1,1]]))
