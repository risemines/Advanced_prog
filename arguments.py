def anagrams(string1, string2):
  return sorted(string1)==sorted(string2)

word1=input("Enter the first word: ")
word2=input("Enter the second word: ")
print(anagrams(word1, word2))
