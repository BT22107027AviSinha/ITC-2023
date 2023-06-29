s = str(input("Input your string here: "))

def isPalindrome(inp):
    return inp == inp[::-1]

inp = s

ans = isPalindrome(inp)

if ans:
    print("Yes")
else:
    print("No")



