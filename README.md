# Simple line by line NTLM encoder 

Requires:
```
python 3.5+
pip install progress
```

Simple python script which encodes all source file lines to NTLM.

```
source.txt

123456
12345
123456789
password
iloveyou
```
Converts to rainbow table in
pass|hash format
```
hashes.txt

123456|32ed87bdb5fdc5e9cba88547376818d4
12345|7a21990fcd3d759941e45c490f143d5f
123456789|c22b315c040ae6e0efee3518d830362b
password|8846f7eaee8fb117ad06bdd830b7586c
iloveyou|b963c57010f218edc2cc3c229b5e4d0f
```

## Usage

```
python3 main.py

List path: ../source.txt
```
