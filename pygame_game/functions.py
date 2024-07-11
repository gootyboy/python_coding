import pgzrun

def fruit_score(fruit):
    if fruit == "apple":
        return 10
    if fruit == "orange":
        return 5

apple_score = fruit_score("apple")
orange_score = fruit_score("orange")
total = apple_score + orange_score
print(total)

pgzrun.go()