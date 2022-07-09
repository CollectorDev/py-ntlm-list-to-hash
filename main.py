import hashlib,binascii
from progress.bar import Bar

source = input("List path: ")

sum = sum(1 for line in open(source, 'r', encoding="ISO-8859-1"))

f = open("hashes.txt", "w")
f.write("")
print("hashes.txt cleared..")
f = open("hashes.txt", "a", encoding="utf-8")
print("Encoding started!")
file = open(source, encoding='ISO-8859-1').read().splitlines()

with Bar('Processing', max=sum, suffix=f"%(percent)d%% | %(index)d/%(max)d") as bar:
    for line in file:
        hash = hashlib.new('md4', line.encode('utf-16le')).digest()
        hashedLine = binascii.hexlify(hash).decode("utf-8")
        f.write(f"{line}|{hashedLine}\n")
        bar.next()

exit('Encoding finished')
