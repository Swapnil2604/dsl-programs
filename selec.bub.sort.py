#Write a Python program to store first year percentage of students in array.
#Write function for sorting array of floating point numbers in ascending order using 
#a) Selection Sort 
#b) Bubble sort and display top five scores.


def add_Elements(arr,n):
    
    
    flag=False
    print("Enter Array Elements :")
    for i in range(0,n):
        num=int(input())
        arr.append(num)
    print("Array Elements are:")
    print(arr)
    return arr


def bubble_sort(arr,n):
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print("sorted elements using bubble sort....")
    print(arr)
    
def selection_sort(arr,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("sorted elements using selection sort....")
    print(arr)
    
    


        
        

if __name__=="__main__":
    arr=[]
    n=0
    
    print("1.Insert array elements....")
    print("2.display array elements....")
    print("3.Bubble sort...")
    print("3.Selection sort...")
    while(True):
        print("enter choice:")
        ch=int(input())
        
        if ch==1:
            n=int(input("how many number do you want to add..."))
            arr=add_Elements(arr,n)
        elif ch==2:
            bubble_sort(arr,n)
        elif ch==3:
            selection_sort(arr,n)
        else:
             print("wrong choice...")
             break

