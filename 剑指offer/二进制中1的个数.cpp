#include <iostream>
using namespace std;
int main(){
	class Solution {
public:
     int NumberOf1(int n) {
        int count=0;
		while (n!=0){
			++count;
			n=n&(n-1);
		}
		return count;
     }
};
Solution s;
cout<<s.NumberOf1(-10);
	return 0;
}
