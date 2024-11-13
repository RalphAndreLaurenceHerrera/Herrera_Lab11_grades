WordsList = []
PassedWords = []
Loopcounter = 0

while Loopcounter < 10: # 10 = Number of words
    
    if Loopcounter == 0:
        Rank = "1st"
    elif Loopcounter == 1:
        Rank = "2nd"
    elif Loopcounter == 2:
        Rank = "3rd"
    else:
        Rank = str(Loopcounter+1)+"th"
    
    InputtedWords = input(f"Input {Rank} word: ")
    WordsList.append(InputtedWords)
    
    Loopcounter += 1
    
Wordlength = int(input("Enter word length: "))
print(f"Words that you inputted: {WordsList}")

for Word in WordsList:
    if len(Word) >= Wordlength:
        PassedWords.append(Word)
           
print(f"Words that you inputted that is above {Wordlength} letters: {PassedWords}")