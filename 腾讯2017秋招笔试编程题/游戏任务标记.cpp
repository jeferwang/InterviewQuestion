/*
腾讯笔试题 
*/

#include <iostream>

using namespace std;

int main(){
	int ID1,ID2;//输入的两个任务ID
	while(cin>>ID1>>ID2){
		// 检查输入是否符合条件 
		if(ID1<1||ID1>1024 || ID2<1|| ID2>1024){
			cout<<-1<<endl;
			continue;
		}
		// 创建32个unsigned int 
		unsigned int tag[32];
		
		int index=0;
		index=(ID1-1)/32;//计算出来存储数字的位置 
		
		int temp=0;
		temp=(ID1-1)%32;//计算出来所在的下标
		
		tag[index]|=(1<<temp);//标记第一个任务为已完成状态 
		
		index=(ID2-1)/32;
		temp=(ID2-1)%32;
		
		if((1<<temp)&tag[index]){
			cout<<1<<endl;
		} else{
			cout<<0<<endl;
		}
		
	}
	return 0;
	
} 
