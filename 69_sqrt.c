#include<stdio.h>
int mySqrt(int x);
int main(){
    int a=2147395599;
    printf("%d",mySqrt(a));
    return 0;
}
int mySqrt(int x){
    int letf = 0;
    int right = x;
    int ans;
    while (letf <= right)
    {
        int middle = (letf+right)/2;
        if(middle*middle>x){
            right = middle-1;
        }
        else{
            ans = middle;
            letf = middle+1;                      
        }
    }
    return ans;
}