#include <iostream>

using namespace std;

class Node
{   public:
    int val;
    Node *next;
    Node (int val)
    {
        this->val=val;
        next=NULL;
    }
};

int main()
{
    Node *n1=new Node(10);

    Node *n2=new Node(20);
    n1->next=n2;
    Node *n3=new Node(30);
    n2->next=n3;
    Node *n4=new Node(40);
    n3->next=n4;
    /**Node *n5= new Node(50);
    n4->next=n5;**/
    Node *temp=n1;
    Node *temp1=n1;
   while(temp1!= NULL && temp1->next != NULL)
   {
       temp=temp->next;
       temp1=temp1->next;
       temp1=temp1->next;
   }
   cout<<temp->val<<endl;

    
}

