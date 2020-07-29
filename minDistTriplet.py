# Question Link : https://app.codesignal.com/challenge/LPAySw9MQXCi7934W
# Level : Hard for beginners
# Solution right below :-

def minDistTriplet(a, b, c):
    minDist = 2**31
    
    x,y,z=a.pop(),b.pop(),c.pop()
    
    while True:
        # 'x' should be max(x,y,z) always 
        # 'a' should always points to list to which 'x' belongs
        # below  if , elif are for above 2 points 
        if y > x and y>= z:
            a,b = b,a
            x,y = y,x
        elif z>x and z>=y:
            c,a = a,c
            x,z = z,x
            
        # small math rule :
        # if x = max(x,y,z) then 2*(x-min(y,z)) === abs(x-y)+abs(y-z)+abs(z-x)
        minDist =min(minDist,x-min(y,z))
        
        if not a:
            # terminate if the pointing set ends
            break
        x=a.pop()
        
    return 2*minDist # 2*(x-min(y,z))
    
print('Min Possible dist :',minDistTriplet([4, 30],[6, 12, 20],[10, 37]))
            
