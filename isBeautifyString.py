# Question Link : https://app.codesignal.com/challenge/t9fu2Pr37mmWPuuEk
# Level : Medium
# Solution is right below :-

def isBeautifulString(inst):
    freqs = [0]*26
    maxchar = 0
    for ch in inst:
        freqs[ord(ch)-ord('a')] += 1
        maxchar = max(maxchar,ord(ch)-ord('a'))
    for i in range(maxchar):
        if freqs[i]<freqs[i+1]:
            return False
    return True
    
print('RESULT :',isBeautifulString('bbbaacdafe'))
