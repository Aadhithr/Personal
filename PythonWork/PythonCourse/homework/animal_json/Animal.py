import json
from collections import OrderedDict as Od

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

# Printing 
for name_likes_dislikes in range(len(Animal_Names)):
    print("{}. {} likes {} and dislikes {}\n" .format(
                                                a,
                                                Animal_Names[name_likes_dislikes],
                                                Animal_Likes[name_likes_dislikes], 
                                                Animal_Dislikes[name_likes_dislikes] ))

    a +=1

def like_food(a):
    index_of_food = [index for index, element in enumerate(Animal_Likes) if element == a]
    Animal_Lik = [Animal_Names[x] for x in index_of_food]
    if len(Animal_Lik) > 0:
        return(Animal_Lik)
    else:
        print("No animals like this food")
    
    

def dislike_food(a):
    index_of_food = [index for index, element in enumerate(Animal_Dislikes) if element == a]
    Animal_Dis = [Animal_Names[x] for x in index_of_food]
    if len(Animal_Dis) > 0:  
        return(Animal_Dis)
    else:
        print("No animals like this food")

Lik_Food = input("Enter a food to find the animals that likes the food: ").lower()
print(like_food(Lik_Food))
Dis_Food = input("Enter a food to find the animals that dislikes the food: ").lower()
print(dislike_food(Dis_Food))

print("-"*80)

new_dict = {}

test_dict1 = {}
test_dict2 = {}

Animal_food = Animal_Likes + Animal_Dislikes
sorted_food = (list(Od.fromkeys(Animal_food)))

for x in sorted_food:
    test_dict1[x] = like_food(x)
    test_dict2[x] = dislike_food(x)
    
new_dict.update([("Likes" , test_dict1), ("Dislikes" , test_dict2)])



    



print(new_dict)
    
