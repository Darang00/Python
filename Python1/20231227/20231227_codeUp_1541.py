#1541
def test(x):
    if x<0:
        return "negative"
    
    elif x == 0:
        return "zero"

    else:
        return "positive"

x = int(input())
print(test(x))
        
    
