#Chpt. 3/4 Quiz
my_list = [1, 3.0, ["a", "b", ["A", "B", "C"], "d"], "John"]
print(my_list[2][2][0])



#Chpt. 3/4 Quiz 
my_list = [1, 3.0, ["a","b", ["A", "B", "C"], "d"], "John"]
for x in my_list:
    if isinstance (x, list):
        for m in x:
            if isinstance (m, list):
                print(m, end="")

#my_dict = [1.0, 2,[1],3, -4, 5]
#for x in my_dict: 
    #if isinstance (x, str):
        #print(x, end="")

while message != "quit": 
    message = input("What is your favorite topping? ")
    message += ("I'll add that to your order!")
    if message == "quit": 
        break
    else:
        print(message)
