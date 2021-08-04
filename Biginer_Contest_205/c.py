'''
A,B,C が入力されて、
A^C とB^Cの大小関係を考える．
Cが偶数か奇数かで判断するのが大事！
'''
a,b,c =map(int,input().split())
if c%2 ==0:
    print('='if abs(a)==abs(b) else '<' if abs(a)<abs(b) else '>')
else:
    print('='if a==b else '<'if a<b else'>')

