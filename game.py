import random

def randomWordGenerate() -> str:
    wordsList = ["alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordsList)

wordTemplate = list()

word = randomWordGenerate()
#print(word)
#list-comprehension ehelyett jobb lesz.
for i in range(len(word)):
    wordTemplate.append("_")
 
print()
print(" ".join(wordTemplate))

print("\nTaláld ki a gondolt szót! 10 lehetőséged van. hogy megadj egy-egy karaktert.")
tip = input("Az ön tippje: ")

if tip not in word:
    print("Hát ez bizony rossz ötlet volt.")
else:
    for i in range(len(word)):
        if word[i] == tip:
            wordTemplate[i] = tip 

print(" ".join(wordTemplate)) 