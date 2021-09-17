#include<stdio.h>
int main(){
    int S,T,a,b,c,count=0;
    scanf("%d %d",&S,&T);
    for(a=0;a<=S;a++){
        for(b=0;b<=S-a;b++){
            for(c=0;c<=S-a-b;c++){
                if(a+b+c<=S&&a*b*c<=T) count++;
            }
        }
    }
    printf("%d",count);
    return 0;
}