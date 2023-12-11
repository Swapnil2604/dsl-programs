
#include<iostream>
using namespace std;
#include<string>
#define max 50
char stk[max];
class stack
{
	int top=-1;
	public:
		
	void push(string ch)
	{
		if(top==max-1)
		{
			cout<<"Stack is full.....\n";
		}
		else
		{
			for (int i=0;i<ch.length();i++)
			{
				top++;
				stk[top]=ch[top];
			}
			
		}
	}
	
	string pop(string str)
	{
		string rev="";
		cout<<stk;
		if(top==-1)
			cout<<"Stack is Empty....";
		else
		{
			for(int i=top;i>=0;i--)
			{
				cout<<stk[top];
				rev=rev+stk[top];
				top--;
			}
			
		}
		cout<<"\n Top is:"<<top;
		return rev;
	}

};

int main()

{
	
	string str,rev,str1;
	int c;
	stack s1;
	do
	{
		cout<<"\n\n Select from Menu...........";
		cout<<"\n1.  Print Original String followed by reversed String using Stack.....";
		cout<<"\n2: To check given string is Palindrome or not.....";
		cout<<"\n3: Press 0 to Exit......";
		cout<<"\nEnter your choice:";
		cin>>c;
		switch(c)
		{
			case 1:
				cout<<"\nEnter String:";
				cin>>str;
				cout<<"\nString is: ";
				s1.push(str);
				rev=s1.pop(str);
				break;
			case 2:
				cout<<"\nOriginal String:"<<str;
				cout<<"\nReversed String :"<<rev;
				if(str==rev)
				{
					cout<<"\nString  "<<str<<" is Palindrome......";
				}
				else
					cout<<"\nString  "<<str<<" is not Palindrome......";
				break;
			
		
		}
	
	}while(c!=0);
}
