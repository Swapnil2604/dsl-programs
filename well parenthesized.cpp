#include <iostream>
#include <stack>
#include <string>
#define max 50
using namespace std;
char stk[max];
int top=-1;

class Expression
{
	public:
		bool Parenthesized(string exp) 
		{
     		for (char ch : exp) 
	 		{
      			 if (ch == '(' || ch == '[' || ch == '{') 
				{	
           				
            			push(ch);
        		} 
				else if (ch == ')' || ch == ']' || ch == '}') 
				{
            		
            		if (top==-1) 
					{
              			  return false;
            		}

            		
            		char topChar=pop();
            

            		
            		if ((ch == ')' && topChar != '(') ||
                		(ch == ']' && topChar != '[') ||
                		(ch == '}' && topChar != '{')) 
					{
               		 return false;
            		}
       		   }
           }

   		 
   		 return top==-1;
		}	
		
		char pop()
		{
			char c;
			if(top==-1)
				cout<<"\nStack is Empty....";
			else
			{
				c=stk[top];
				top--;
			}
			return c;
		}
			
		void push(char ch)
		{
			if(top==max-1)
				cout<<"\nStack Overflow....";
			else
			{
				top++;
				stk[top]=ch;
			}
		}

		
};

int main() 
{
    string exp;
    Expression e1;

    cout << "Enter an expression: ";
    cin>>exp;

   
    if (e1.Parenthesized(exp))
	 {
        cout << "The expression is well-parenthesized." <<endl;
    } 
	else 
	{
        cout << "The expression is not well-parenthesized." <<endl;
    }

    return 0;
}
