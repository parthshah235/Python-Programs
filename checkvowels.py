num = int(raw_input())
 
for _ in range(num):
    string = raw_input()
    string = string.lower()
    c = 0
    for i in "aeiou":
        c = c + string.count(i)
        
    print c
