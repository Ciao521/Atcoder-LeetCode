p = int(input()) 
a=0
if  p>=90:
    a="expert"
elif p<90 and p>=70:
    a=90-p
    
elif p<70 and p>=40:
    a=70-p   
else:
    a =40-p
print(a)


