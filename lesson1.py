meme_dict = {
            "CRINGE": "Weird/Emberrasing Things",
            "LOL": "A word in the meaning of lauhing-out-loud",
            'ROFL': 'Like hahaha',
            'SHEESH': 'Not approving',
            'CREEPY': 'Scary',
            'AGGRO': 'Getting Aggressive'
            }
            
word = input("Write a word that u dont know the meaning of!: ")

if word in meme_dict.keys():
    # If ur word matches my knowladge!
    print(meme_dict[word])
    
else:
    # What if the word doesn't exist in my absulute knowledge!
    print('Im sorry but i dont know that word yet!')

  
