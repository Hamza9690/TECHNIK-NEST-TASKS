students = {}

students['101'] = {'name': 'HAMZA', 'age': 20, 'grade': 'A'}
students['102'] = {'name': 'Sara', 'age': 21, 'grade': 'B'}

print("All Students:")
for roll_no, info in students.items():
    print(f"{roll_no}: {info}")

students['101']['grade'] = 'A+'

del students['102']

print("\nAfter Update & Delete:")
for roll_no, info in students.items():
    print(f"{roll_no}: {info}")

sentence = "This is a test. This test is simple."

sentence = sentence.replace('.', '').lower()

words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
    

