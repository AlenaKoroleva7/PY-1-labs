# TODO исправьте опечатку в слове
fruits = ["яблоко", "банан", "опельсин", "виноград"]
incorrect_word = fruits[2]
correct_word = "a" + incorrect_word[1:]
fruits[2] = correct_word
print(fruits)