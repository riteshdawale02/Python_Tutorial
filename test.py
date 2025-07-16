# def my_function(*kids):
#   i = int(input("Enter the index: "))
#   print("The youngest child is " + kids[i])

# my_function("Emil", "Tobias", "Linus")


# my_function("Ritesh","Aditya","Samu")
# my_function("Ritesh","Aditya","Samu","Harish")




# def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# my_function(child1 = "Ritesh", child2 ="Aditya", child3 = "Samu")





def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
