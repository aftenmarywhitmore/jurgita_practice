#Step 1: write a function to print "hello_USERNAME!" 
#Step 2: USERNAME is the input of the function.
#Step 3: The first line of code has been defined as below:

def hello_name(user_name): 
    print("hello_" + user_name.upper() + "!")
hello_name("username")

#hello_USERNAME!
#hello_username 


def first_odds(): 
    for number in range(1, 101):
        if number % 2 == 1:
            print(number)
first_odds()


#Write a function 
#to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

def is_consecutive(a_list): 
    startNumber = a_list[0]
    for i in a_list: 
        if startNumber != i: 
            return False
        startNumber += 1  
    return True 
list1 = [2,3,4,5]
list2 = [1,2,4,5]
print(is_consecutive(list1))
print(is_consecutive(list2))


def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1,2,3,4,5]
print(is_consecutive(a_list))

friends = ['Aften', 'David', 'Carson', 'Aaron', 'Brian']
message = "I am grateful for my friends" + " " + friends [0] + " " + friends [1] + " " + friends[2] + " " + friends[3] + "."
print(message)