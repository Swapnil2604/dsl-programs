#Write a Python program to maintain club members, sort on roll numbers in ascending order.
#Write function “Ternary_Search” to search whether particular student is member of club or not.
#Ternary search is modified binary search that divides array into 3 halves instead of two. 
def add_data(pb):
    roll=int(input("Enter roll number"))
    name=input("Enter name..")
    
    flag=False
    for i in range(len(pb)):
        if roll < pb[i][0]:
            pb.insert(i, (roll, name))
            flag = True
            break
    if not flag:
        pb.append((roll,name))
        
    return pb

def display(pb):
    
    for c in pb:
        print(c)

def Ternary_Search(pb):
    roll_no=int(input("Enter roll no search:"))
    length=len(pb)
    l=0
    r=length-1
    flag=0
    while(l<=r):
        
        # Calculate mid1 and mid2
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        # Check if the element is present at the mid1 or mid2 positions
        if roll_no==pb[mid1][0]:
            print("roll number=",roll_no,"and  name is:",pb[mid1][1])
            print(pb[mid1][1], "is member of club....")
            flag=1
            break
        elif roll_no==pb[mid2][0]:
            print("roll number=",roll_no,"and  name is:",pb[mid2][1])
            print(pb[mid2][1], "is member of club....")
            flag=1
            break
            
        # If x is in the left one-third
        elif  roll_no< pb[mid1][0]:
            r=mid1-1
            flag=0
            
        # If x is in the right one-third
        elif roll_no > pb[mid2][0]:
            l=mid2+1
            flag=0
        # If x is in the middle one-third
        else:
            l=mid1+1
            r-=mid2-1
            flag=0

    
    if flag==0:
        print("Roll number",roll_no,"is not in club....add the name")
        add_data(pb)
        display(pb)

    
        

if __name__=="__main__":
    pb=[]
    print("1.Insert roll number and name....")
    print("2.display roll number and name....")
    print("3.Search name...")
    while(True):
        print("enter choice:")
        ch=int(input())
        
        if ch==1:
            pb=add_data(pb)
            
        elif ch==2:
            display(pb)
        elif ch==3:
            Ternary_Search(pb)
        
        else:
             print("wrong choice...")
             break


