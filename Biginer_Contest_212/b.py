x = list(map(int, list(input())))
if len(set(x)) == 1: 
    exit(print("Weak"))
for i in range(3):
    if (x[i] + 1) % 10 != x[i + 1] % 10: exit(print("Strong"))
print("Weak")

'''
set([1,2,3,4,5])                                # set([1,2,3,4,5]) 
set([1,1,2,2,3,3])                              # set([1,2,3])
set({'dog':'inu', 'cat':'neko', 'bird':'tori'}) # set(['dog', 'cat', 'bird'])
'''