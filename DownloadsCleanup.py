#!/usr/bin/python
#Moves all files used for application installs in the download folder to a seperate folder.

import shutil, os, send2trash
from pathlib import Path

home = Path.home()
originPath = Path(home / 'Downloads')

try:
    Path.mkdir(originPath / 'InstallerFiles')
    print('InstallerFiles directory created')
except FileExistsError:
    pass

try:
    Path.mkdir(originPath / 'Docs')
    print('Docs directory created')
except FileExistsError:
    pass

installPath = Path(originPath / 'InstallerFiles')
docPath = Path(originPath / 'Docs')

countMoved = 0
countDelete = 0
for filename in os.listdir(originPath):
    filePath = originPath / filename
    if filename.endswith('.exe') or filename.endswith('.msi'):        
        try:
            shutil.move(str(filePath), str(installPath))
            print(f'{filename} moved to {installPath}')
            countMoved += 1
        except shutil.Error:
            print(f'{filename} already exists in {installPath}.\nFile moved to trash.')
            send2trash.send2trash(str(filePath))
            countDelete += 1

print('Finished')
print(f'Files moved: {countMoved}')
print(f'Files deleted: {countDelete}')
print('Press ENTER to exit...')
input()
