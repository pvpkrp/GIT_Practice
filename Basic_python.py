"""def add(*args):
    return sum(args)
print(add(7,8,1,1,15,67,8))"""

"""def userdetails(**kwargs):
    print(kwargs)
userdetails(name='Pvpkr',no=8,phno=88977,age=24)"""

"""year =int(input("Enter a year"))
if (year%400==0) and (year%100==0):
    print("{} is a leap year".format(year)
elif (year%4 == 0) and (year%100 != 0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))"""
#prime number
"""num=int(input())
flag=False
if num==1:
    print(f"{num} is not a prime number")
elif num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")"""

"""num=int(input("Display the table for :"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)"""

#Fibonacii series by using the recursion

"""num=int(input("fibonacci series of :"))
if num<=1:
    print(num)
else:"""

"""def fib_rec(num):
    if num<=1:
        return num
    else:
        return fib_rec(num-1)+fib_rec(num-2)
print(fib_rec(8))"""

"""def rotate_arr(arr,d):
    n=len(arr)
    if d<0 or d>=n:
        return "Invalid rotation value"
    rotated_arr=[0]*n
    for i in range(n):
        rotated_arr[i]=arr[(i+d)%n]
    return rotated_arr
print(rotate_arr([5,6,7,3,4,5],3))"""

#Rotating the array by using the split and add

"""def split_add(arr,d):
    n=len(arr)
    if d<=0 or d>=n:
        return arr
    #split the array in two parts
    first_part=arr[d:]
    second_part=arr[:d]
    total_string=first_part+second_part
    return total_string
print(split_add([7,8,3,4,5,2,3],4))"""

##sort the words

"""my_str=input("Enter a string")
words=[word.capitalize() for word in my_str.split()]
words.sort()
print("The sorted words are :")
for word in words:
    print(word)"""
##string split and join
"""input_list="Python program to split and join a string"
word_list=input_list.split()
print(word_list)
print(word_list[-4])
sep=" "
join_word=sep.join(word_list)
print(join_word)"""

"""##to know whether the string is binary or not
def binary_str(input_str):
    for i in input_str:
        if i in "01":
            return True
        return False
print(binary_str("99868"))"""

"""##to find duplicates in the string
def duplicate_str(input_str):
    count_char={}
    duplicates=[]
    for i in input_str:
        if i in count_char:
            count_char[i]+=1
        else:
            count_char[i]=1
    for i,count in count_char.items():
        if count>1:
            duplicates.append(i)
    return duplicates
print(duplicate_str("VedaPraneethKumar Reddy"))"""

##unique values in the dictionary
"""def unique_vals(Input_str):
    unique_val=set()
    for i in Input_str.values():
        unique_val.append(i)
        unique_val_list=list(unique_val)
print(unique_vals('a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20))"""

##join with the given values

"""input_to_join_with=input("Enter a string :")
joined_str=",".join(input_to_join_with)
print(joined_str)"""

"""#To count no of charcaters and digits in the given input
sentence=input("Enter the sentence :")
char_count=0
digit_count=0
for char in sentence:
    if char.isalpha():
        char_count+=1
    elif char.isdigit():
        digit_count+=1
print("letters :",char_count)
print("digits are :",digit_count)"""





