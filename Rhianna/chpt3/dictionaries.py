#1. Select ALL choices that create a dictionary
#my_dict = {}
#my_dict = dict()
#my_dict = {'key':'value'}

#2. Using the dictionary select the answer that 
    #returns Troy Aikman's team, and the correct datatype of that answer
#my_dict['team'], string

#3.Using the dictionary select the answer that 
    #returns Troy Aikman's awards, and the correct datatype of that answer
#my_dict['awards'], dictionary

#4. Using the dictionary select the answer that 
    #returns 1995, and the correct datatype of that answer
#my_dict["awards"]["probowl"][-2]

#5. Select the answer the corresponds to the correct output
#Troy Aikman has won 3 

#6. Select the answer the corresponds to the correct output
#You will get an error 

#7. Select the answer the corresponds to the correct output
#You will get an error 

#8. Select the answer the corresponds to the correct output
#XXVIII

#9. Select the answer the corresponds to the correct output
#0

#10. Select the answer the corresponds to the correct output (ASK KEVIN)
#team weight superbowls 

#11. Select the answer the corresponds to the correct output
#xxxOldxxxx

#12. Select the answer the corresponds to the correct output 
#54 - TYPE OUT CODE!!!! 

#13. Select the answer the corresponds to the correct output
#1994

#14. Select the answer the corresponds to the correct output
#You will get an error 
#How to append to a list in a dict (appending is for lists)
my_dict = {'age':[54]}

my_dict['age'].append(14)
print(my_dict['age'])

#15. Select the answer the corresponds to the correct output
#14


#16. Select the answer the corresponds to the correct output
#1993
my_dict = {'age':54,
'position':"QB",
'awards': {'probowl': [1991, 1992, 1993, 1994, 1995, 1996]}
}

print(my_dict.get('awards', 'age')['probowl'][len(my_dict['position'])])

#17. Select the answer the corresponds to the correct output
#['XXVII']
#man_or_the_year 

fave_artist= {

    "bands": ["radiohead", "animal collective", "death grips"],
    "solo artist": ["king krule", "arca", "bjork" ],

    "fave albums": {
    
    "dannybrown": ["XXX", "atrocity exhibition"],
    "radiohead": ["in rainbows", "kid A", "ok computer"],
    "animal collective": [" centipede", "feels", "strawberry jam"]
    }
}

#print(fave_artist["rappers"])
#print(fave_artist["rappers"][0])

#for key, value in fave_artist.items():
    #print(key, value)

#for key, value in fave_artist.items():
    #if key == "rappers":
        #print(key, value[0])


for key, value in fave_artist.items():
        if isinstance("radiohead", list):
            print(value, end="")
