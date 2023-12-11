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

def fib_search(pb):
    name=input("Enter name to search:")
    
    l = len(pb)
    elim = -1
    f2 = 0    #Two finbonacci numbers before fn
    f1 = 1    #One finonacci numbers before fn
    fn = f1+f2
    flag=0

    while fn<=l:
        f1, f2 = fn, f1
        fn = f1+f2

    while fn>1:
       
        curr = min(elim+f2,l-1)  
        print(curr,"	",f1,"	",f2,"	",fn)
        if pb[curr][0] == name:
            flag=1
            print(name,"is present at location",curr)
            print(pb[curr][0],"   ",pb[curr][1])
            break
        
        elif pb[curr][0] > name:   
            fn = f2
            f1 = f1 - f2
            f2 = f2 - f1
           
        else:  
            fn = f1
            f1 = f2
            f2 = fn - f1   
            elim = curr   
           
        
    if flag==0:
        print("name is not in the list...")



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
            fib_search(pb)
       
        else:
             print("wrong choice...")
             break
