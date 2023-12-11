#Write a Python program to store names and mobile numbers
#of your friends in sorted order on names.
#Search your friend from list using binary search (recursive and nonrecursive).
#Insert friend if not present in phoneboo


def add_data(pb):
    name=input("Enter name..")
    number=int(input("Enter mobile number"))
    flag=False
    for i in range(len(pb)):
        if name < pb[i][0]:
            pb.insert(i, (name, number))
            flag = True
            break
    if not flag:
        pb.append((name,number))
        
    return pb

def display(pb):
    
    for c in pb:
        print(c)

def bin_search(pb):
    name=input("Enter name to search:")
    length=len(pb)
    l=0
    r=length-1
    flag=0
    while(l<=r):
        mid=(l+r)//2
        if(name==pb[mid][0]):
            print("name=",name,"and mob number is:",pb[mid][1])
            flag=1
            break
        elif name<pb[mid][0]:
            r=mid-1
            flag=0
        else:
            l=mid+1
            flag=0
            
    if flag==0:
        print(name,"is not in list....add the name")
        add_data(pb)
        display(pb)

def rec_BinSearch(pb,l,r,name):
    if l>r:
        print("name is not in the list")
        add_data(pb)
        display(pb)
        print("name is added in the list")
    else:
        mid=(l+r)//2
        if(name==pb[mid][0]):
            print("name=",name,"and mob number is:",pb[mid][1])
        elif name<pb[mid][0]:
            rec_BinSearch(pb,l,mid-1,name)
        else:
            rec_BinSearch(pb,mid+1,r,name)
        
        

if __name__=="__main__":
    pb=[]
    print("1.Insert name and mobile number....")
    print("2.display name and mobile number....")
    print("3.Search friend...")
    while(True):
        print("enter choice:")
        ch=int(input())
        
        if ch==1:
            pb=add_data(pb)
            
        elif ch==2:
            display(pb)
        elif ch==3:
            bin_search(pb)
        elif ch==4:
            name=input("Enter name to search:")
            rec_BinSearch(pb,0,len(pb)-1,name)
        else:
             print("wrong choice...")
             break

