'''
What is a List?
A list is an ordered, mutable (changeable) collection of items. This means:

Ordered: The items in a list have a defined order, and that order will not change unless you explicitly modify it. You can access items by their index.

Mutable: You can change, add, or remove items from a list after it has been created.

Collection: A list can hold multiple items.

Heterogeneous: List items do not all have to be of the same data type. You can have integers, strings, floats, other lists, and even custom objects all in the same list.
'''

empty_list = []
print(f"List is: {empty_list}")

# Integer List
list1 = [1,2,4,5,6]
print(f"Integer List: {list1[3]}")

#String list
list2 = ["ritesh","bittu","sachin","yogesh"]
print(f"String list:{list2} ")
print(f"list: {list2[2]}")

#Mix list
mixList = ["ritesh",19,80.12,True,"indigo",[1,2]]
print(f"Mix List: {mixList}")

#Negative indexing
number = [1,2,3,4,5]
print(f"element: {number[-2]}")


#slicing list

numbers = [0,1,2,3,4,5,6,7,8,9]

print(f"Slice from index 2 to 5 (exclusive): {numbers[2:6]}")   # Output: [2, 3, 4, 5]
print(f"Slice from beginning to index 4 (exclusive): {numbers[:5]}") # Output: [0, 1, 2, 3, 4]
print(f"Slice from index 5 to end: {numbers[5:]}")    # Output: [5, 6, 7, 8, 9]
print(f"Copy of the whole list: {numbers[:]}")        # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Every second item: {numbers[::2]}")         # Output: [0, 2, 4, 6, 8]
print(f"Reverse the list: {numbers[::-1]}")         # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#Operations

fruits = ["Apple","Banana","Cherry"]

#changing item
fruits[1] = "Orange"
print(f"after changing: {fruits}")

#adding item
fruits.append("Grapes")
print(f"after append: {fruits}")

#insert item
fruits.insert(2,"Mango")
print(f"after insert: {fruits}")

#extend item
more_fruits = ["kiwi","pineapple"]
fruits.extend(more_fruits)
print(f"after extend: {fruits}")

#removing item
    #specified item
fruits.remove("Apple")
print(f"after removing: {fruits}")

    #removing using index
fruits.pop(1)
print(f"after removing: {fruits}")

#delete at item at specified index or a slice

myNumber = [10,20,30,40,50]
del myNumber[1] # delete 20
print(f"After deleting index: {myNumber}")

del myNumber[1:3]
print(f"After deleting index: {myNumber}")

#clear list
myNumber.clear()
print(f"After clear: {myNumber}")


#Common methods in list
my_list = [1,2,9,6,2,3,8,2,5,4]

print(f"Length: {len(my_list)}")    #length
print(f"Count: {my_list.count(2)}")  #count the number
print(f"Index of 9: {my_list.index(9)}")  #Index of element in the list

my_list.sort() #Ascending order
print(f"List: {my_list}")

my_list.sort(reverse=True) #Descending order
print(f"List: {my_list}")

#reverse
list3 = ["a","b","c"]
list3.reverse()
print(f"List: {list3}")

My_list = ["apple", "banana", "cherry", "date"]
for i in range(0,4):
    print(f"List item {i}: {My_list[i]}")


print("Using enumerate(): ")
for index, item in enumerate(My_list):
        print(f"Index: {index}: {item}")


