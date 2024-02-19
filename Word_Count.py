# Program to print the word occurences in a file content.
dict_word = {}
file_name = 'myfile.txt'
list_content = open(file_name, 'r')
words = list_content.read().lower().split()
for word in words:
    cnt = words.count(word)
    dict_word[word] = cnt
for word, cnt in dict_word.items():
    print(word, '', cnt)
