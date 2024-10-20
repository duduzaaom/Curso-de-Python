from difflib import get_close_matches

text = input('Write text: ')
splitted_text = text.split()
correct_words = []
wrong_words = {}
new_text = ''

with open('wordlist.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        correct_words.append(line)

for word in splitted_text:
    if word.lower() not in correct_words:
        new_text += f'*{word}* '
        wrong_words[word] = get_close_matches(word.lower(), correct_words)
    else:
        new_text += f'{word} '

print(new_text)
print("suggestions:")
for word, close_match in wrong_words.items():
    print(f'{word}: {close_match[0]}, {close_match[1]}, {close_match[2]}')