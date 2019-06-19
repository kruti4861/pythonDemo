try:
    with open("test.txt", 'w', encoding='utf-8') as f:
        f.write("my first file\n")
        f.write("This file\n\n")
        f.write("contains three lines\n")
        f.write("This is practice for try finally block")
    for i in range(2):
        f = open("test.txt", "a")
        f.write("I am appending new line")
    with open("test.txt",'r') as f:
        f.read()
finally:
    f.close()