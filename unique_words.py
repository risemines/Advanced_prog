unique_words=[]
i=0
while True:
  i=i+1
  word=input("Enter a word: ")
  if word in unique_words:
    print(f"you typed in {i} words")
    break
  else:
    
    unique_words.append(word)
