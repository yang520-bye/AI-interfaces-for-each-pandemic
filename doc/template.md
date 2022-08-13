# 异或和 (^)
>数组中所有的数异或起来，得到的结果叫做数组的异或和
- 解法
>相同数异或为0
```markdown
满足交换律
```
c++列举前缀和所有排列
```c++
#include <iostream>
using namespace std ;

int main(){
    int sum[10] = {0} ;
    int a[6] = {0 ,  1 , 2 , 3 , 4 ,5 };
    for(int i = 1 ; i <= 5 ; i ++ )
    {
        sum[i] = sum[i-1] + a[i] ; 
    }
    for(int i = 1 ; i <= 5 ; i ++ )
     for(int j = i ; j <= 5 ; j ++ )
     {
          cout << sum[j] - sum[i-1] << endl; 
     }
    return 0 ;
}
```
3
