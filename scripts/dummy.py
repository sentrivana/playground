import random


with open("SOME_FILE.md", "w") as f:
    f.write("Hello world!\n")
    f.write(str(random.randint(1, 10000)))
