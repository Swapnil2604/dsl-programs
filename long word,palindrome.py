str1=input("enter the string:\n")
words1=str1.split()
largest_word=words1[0]
for w in words1:
    if len(w)>len(largest_word):
        largest_word=w
        print("the largest word is:", largest_word)
        
str2=input("enter the string:\n")
words2=str2.split()
word=input("enter the word that frequency you want: ")
count=0;
for w in words2:
    if word==w:
        count+=1
print("the frequency of the occurance is: ", count)

str3=input("enter the word to check whether the word is palindrome or not: ")
a1=[]
a2=[]
for i in str3:
    a1.append(i)
for i in range(len(a1)-1,-1,-1):
    a2.append(a1[i])
    if a1==a2:
        print("entered word is a palindrome")
    else:
        print("Entered word is not a palindrome")
        
str4=input("Enter the string to display first index of each word:\n")
str4=str4.lower()
str4=str4.title()
a=[]
for i in str4:
    a.apppend(i)
    
for i in range(0,len(a)):
    if a[i].isupper():
        print(i)