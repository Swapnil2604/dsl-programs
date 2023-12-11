
#include<iostream>
#include<vector>
using namespace std;

class node{
	public:
		int prn;
		string name;
		
		node *next;
		node(){
			next = nullptr;
		}
};
class List{
	node *head;
	public:
		List()
		{
			head = NULL;
		}
		void insertAtBeg(int v,string s)
		{
			node *p = new node();
			p->prn = v;
			p->name=s;
			p->next = head;
			head = p;
		}
		void insertAtEnd(int v,string s)
		
		{
			node *p = new node();
			p->prn = v;
			p->name=s;
			if (head == NULL)
			{
				head = p;
			}
			else
			{
				
				node *ptr = head;
				while (ptr->next != NULL)
				{
					ptr = ptr->next;
				}
				ptr->next = p;
			}
		}
		
		void display()
		{
			int count=0;
			if (head == NULL){
				cout<<"List is empty"<<endl;
			}
			else
			{
				
				node *p = head;
				cout<<"Linked List: \n";
				while (p != NULL){
					cout<<p->prn<<"\t"<<p->name<<"\n";
					count++;
					p = p->next;
				}
			
			}
			cout<<"Number of elemnets in linked list:"<<count;
		}	
		void insertBetween(int v,string s, int pos){
			node *p = new node();
			p->prn = v;
			p->name=s;
			if (pos == 0)
			{
				p->next = head;
				head = p;
			}
			else
			{
				node *ptr = head;
				while(pos>1) 
				{
					ptr = ptr->next;
					--pos;
				}
				p->next = ptr->next;
				ptr->next = p;
			}
		}
		void deleteAtFirst()
		{
			if (head == NULL){
				cout<<"List is Empty"<<endl;
			}
			else
			{
				cout<<"Element Deleted: "<<head->prn<<"\t"<<head->name<<endl;
				node *p = head;
				head = head->next;
				delete(p);
			}
		}
		void deleteAtEnd()
		{
			if (head == NULL){
				cout<<"List is Empty"<<endl;
			}
			else if (head->next == NULL)
			{
			
				cout<<"Element Deleted: "<<head->prn<<"\t"<<head->name<<endl;
				delete(head);
				head = NULL;
			}
			else
			{
				node *p = head;
				
				while (p->next->next != NULL)
				{
					p = p->next;
				}
				
				cout<<"Element Deleted: "<<p->next->prn<<endl;
				delete(p->next);
				p->next = NULL;
			}					
		}
		void deleteInBetween(int pos)
		{
			if (head == NULL)
			{
				
				cout<<"List is Empty"<<endl;
			}
			else
			{
				node *p, *ptr;
				if (pos == 0)
				{
				
					cout<<"Element Deleted: "<<head->prn<<"\t"<<head->name<<endl;
					ptr = head;
					head = head->next;
					delete(ptr);
				}
				else
				{
					
					p = ptr = head;
					while(pos>0)
					{
						--pos;
						p = ptr;
						ptr = ptr->next;
					}
					cout<<"Element Deleted: "<<ptr->prn<<"\t"<<ptr->name<<endl;
					p->next = ptr->next;
					free(ptr);
				}
			}
		}
};

int main()
{
	
	printf("1 to Insert at the beginning");
	printf("\n2 to Insert at the end");
	printf("\n3 to Insert at mid");
	printf("\n4 to Delete from beginning");
	printf("\n5 to Delete from the end");
	printf("\n6 to Delete from mid");
	printf("\n7 to Display");
	printf("\n0 to Exit");
	
	int choice,v,p;
    string nm;
	List ll;
	do 
	{
		cout<<"\nEnter Your Choice: ";
		cin>>choice;
		switch (choice)
		{
			case 1:
				cout<<"Enter Element:  ";
				cin>>v;
				cout<<"Enter name:  ";
				cin>>nm;
				ll.insertAtBeg(v,nm);
				break;
				
			case 2:
				cout<<"Enter Element: ";
				cin>>v;
				cout<<"Enter name:  ";
				cin>>nm;
				ll.insertAtEnd(v,nm);
				break;
				
			case 3:
				cout<<"Enter Element: ";
				cin>>v;
				cout<<"Enter name:  ";
				cin>>nm;
				cout<<"Enter Position ( zero-indexed ): ";
				cin>>p;
				ll.insertBetween(v,nm,p);
				break;
				
			case 4:
				ll.deleteAtFirst();
				break;
				
			case 5:
				ll.deleteAtEnd();
				break;
				
			case 6:
				cout<<"Enter Position ( zero-indexed ): ";
				cin>>p;
				ll.deleteInBetween(p);
				break;
				
			case 7:
				ll.display();
				break;
			
				
				
		}
	} while (choice != 0);
	
}
