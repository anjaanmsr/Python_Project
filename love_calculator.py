# Love Calculator

print("Love Calculator ")

name1 = input("Whats your name : ").lower()
name2 = input("Whats your partner name : ").lower()
print(f"Your are {name1} and your partner is {name2} ")

lover = name1 + name2

t = lover.count("t")
r = lover.count("r")
u = lover.count("u")
e = lover.count("e")

true = t + r + u + e

l = lover.count("l")
o = lover.count("o")
v = lover.count("v")
e = lover.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score >10) and (love_score <= 90) :
    print(f"{name1} and {name2} love score is {love_score} , You are alright together like coke & mentos")
elif love_score >= 40 and love_score <= 50 :
    print(f"{name1} and {name2} love score is {love_score} , You are alright together.")
else :
    print(f"{name1} and {name2} love score is {love_score} , You need to worktogether.")