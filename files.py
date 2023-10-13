from pathlib import Path
import os


path = str(Path('spam', 'bacon', 'eggs'))
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

# for file in myFiles:
#     print(path + '/' + file)


p = Path('/Users/friedrichtenhagen/coding/testdirectory/data.rtf')


print(p.read_text())