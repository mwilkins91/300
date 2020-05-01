import pickle
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

start = None
try:
    start = pickle.load(open("var.pickle", "rb"))
except (OSError, IOError) as e:
    start = 0
    pickle.dump(start, open("var.pickle", "wb"))
f = open(os.path.join(__location__, '300.txt'), "r")
for i in range(start):
    f.readline()

lines = []
found_text = False

for i, line in enumerate(f, 1):
    lines.append(line)
    if line.strip() != '':
        found_text = True
    if found_text and line.strip() == '':
        start = start + i
        break


pickle.dump(start, open("var.pickle", "wb"))
print("\n".join(filter(lambda l: l.strip() != '', lines)))
