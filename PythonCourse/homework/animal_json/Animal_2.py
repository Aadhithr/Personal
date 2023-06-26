import json

# Loading the json flie and storing in the variable [data]
data = json.load(open("Animal.json"))

# Adding the names of animals into the Animal_names list
Animal_Names = [value_animal["animal"] for value_animal in data]

# Adding the likes of each animal into the Animal_Likes list
Animal_Likes = [value_likes["likes"] for value_likes in data]

# Adding the dislikes of each animal into the Animal_Disklikes list
Animal_Dislikes = [value_dislikes["dislikes"] for value_dislikes in data]

# Counter
a = 1

# Printing what each animal likes and dislikes
for name_likes_dislikes in range(len(Animal_Names)):
    print("{}. {} likes {} and dislikes {}\n" .format(
                                                a,
                                                Animal_Names[name_likes_dislikes],
                                                Animal_Likes[name_likes_dislikes], 
                                                Animal_Dislikes[name_likes_dislikes] ))

    a +=1
    
# Like Function
def like_food(a):
    # Gets the index(as a list) of (a) from the Animal_Likes list. The list can contain multiple of the same
    # food due to the liking of the animal so  there can be multiple indexes
    index_of_food = [index for index, element in enumerate(Animal_Likes) if element == a]
    # Assigning the food that is in the position of the index to another list
    Animal_Lik = [Animal_Names[x] for x in index_of_food]
    # Conditional Statement
        # True then return the list called Animal_Lik
        # False then print "No animals like this food"
    if len(Animal_Lik) > 0:
        return(Animal_Lik)
    else:
        print("No animals like this food")
    
    
# SAME THING AS ABOVE BUT RETURNS THE NAME OF THE ANIMAL THAT DISLIKES THE FOOD
def dislike_food(a):
    index_of_food = [index for index, element in enumerate(Animal_Dislikes) if element == a]
    Animal_Dis = [Animal_Names[x] for x in index_of_food]
    if len(Animal_Dis) > 0:  
        return(Animal_Dis)
    else:
        print("No animals like this food")

# Using the function to get the animals that dislike/like the type of food
Lik_Food = input("Enter a food to find the animals that likes the food: ").lower()
print(like_food(Lik_Food))
Dis_Food = input("Enter a food to find the animals that dislikes the food: ").lower()
print(dislike_food(Dis_Food))

print("-"*80)

# Assigning 3 empty dictionaries to a different variable
   #The main dictionary
new_dict = {}

    # Inside dictionary 1
test_dict1 = {}
    # Inside dictionary 2
test_dict2 = {}

for x in range(len(Animal_Likes)):
     test_dict1.setdefault(Animal_Likes[x], []).append(Animal_Names[x])
     test_dict2.setdefault(Animal_Dislikes[x], []).append(Animal_Names[x])
new_dict["Likes"] = test_dict1
new_dict["Dislikes"] = test_dict2
print(new_dict)
    
