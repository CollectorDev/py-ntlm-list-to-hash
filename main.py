import hashlib,binascii
source = input("List path: ")

f = open("hashes.txt", "w")
f.write("")
print("hashes.txt cleared..")
f = open("hashes.txt", "a")
print("Encoding started!")
file = open(source, encoding='ISO-8859-1').read().splitlines()

for line in file:
    hash = hashlib.new('md4', line.encode('utf-16le')).digest()
    hashedLine = binascii.hexlify(hash).decode("utf-8");
    f.write(hashedLine + "\n")
    print(f"{line} = {hashedLine}")

exit('Encoding finished')
