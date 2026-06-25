text = input("Please enter  text: ")
count_letters = 0
count_words = 0
count_sentences = 0


for char in text:
    if char.isalpha():
        count_letters += 1

# print(count_letters)


words = text.split()
# print(count_words)
count_words = len(words)
# print(count_words)

for sentence in text:
    if sentence == "." or sentence == "!" or sentence == "?":
        count_sentences += 1

# print(count_sentences)

l = count_letters / count_words * 100
s = count_sentences / count_words * 100
index = 0.0588 * l - 0.296 * s - 15.8

grade = round(index)
if index < 1:
    print("Before Grade")

elif index > 16:
    print("Grade:  16")

else:
    print(f"Grade: {grade}")

