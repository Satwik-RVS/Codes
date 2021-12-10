#include <stdio.h>
#include <stdlib.h>

int getIntegerValue(int N)
{
    int arr[1001], index = 0;
    int bin = 0, base = 1;
    while(N > 0)
    {
        int x = N%10;
        if(x == 1 || x == 0)
        {
            while(N > 0 && (x == 1 || x == 0))
            {
                bin += x * base;
                base *= 2;
                N = N/10;
                x = N%10;
            }
            x = bin;
        }
        else
        {
            N = N/10;
        }
        arr[index] = x;
        index = index + 1;
    }
    
    int num = 0;
    for(int i=index-1; i>=0; i--)
    {
        num = num*10 + arr[i];
    }
    
    return num;
}

int main()
{
    int N;
    scanf ("%d", &N);
    printf("%d", getIntegerValue(N));
    return 0;
}
