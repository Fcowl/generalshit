from pathlib import Path
import functions2
import os
path = Path(r'C:\Users\Fcowl\CLionProjects\LearningC')
target = list(path.glob('hm?'))
for item in target:
    files = item.glob('?.c')
    for file in files:
        print(file)
        renamed = item / Path(f"{file.parent.name}-{file.name}")
        print("result:",renamed)
        os.rename(file, renamed)
        #file.rename(file,renamed)

