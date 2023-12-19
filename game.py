import random

def randomWordGenerate() -> str:
    wordsList = ["alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordsList)

wordTemplate = list()

word = randomWordGenerate()
#print(word)
for i in range(len(word)):
    wordTemplate.append("_")
 
print(" ".join(wordTemplate))   