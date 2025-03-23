import random
import string
try:
    f = open("example.txt", "w")
except FileNotFoundError:
    f = open("example.txt", "a+")
f.writelines([str(string.ascii_lowercase[random.randint(0, 25)]*random.randint(1, 10))+"\n" for i in range(random.randint(1, 15))])
f.close()
fn = open("example.txt", "r")

lines = fn.readlines()
print(lines)
fn.close()
if len(lines) > 2:
    newLines = []
    newLines.append(lines[-1])
    [newLines.append(i) for i in lines[1:-1]]
    newLines.append(lines[0])
    fn = open("example2.txt", "w")
    print(newLines)

    fn.writelines(newLines)
    fn.close()
else:
    raise Exception("Больше 2")