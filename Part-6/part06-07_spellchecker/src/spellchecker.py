text = input('Write text: ')
splitted_text = text.split()
correct_words = []
new_text = ''

with open('wordlist.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        correct_words.append(line)

for word in splitted_text:
    if word.lower() not in correct_words:
        new_text += f'*{word}* '
    else:
        new_text += f'{word} '

print(new_text)