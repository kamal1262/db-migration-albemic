import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root, parent_3 = file.parent, file.parents[1], file.parents[3]

print(f'parent : {parent}')

print(f'root: {root}')

print(f'parent_3: {parent_3}')

print('file_path: ', __file__)

print("file: ", file)

# sys.path.append(str(root))
import os 

parent_dir = os.path.abspath(os.getcwd())
print('parent_dir:', parent_dir)
# sys.path.append(parent_dir) 
