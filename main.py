# !/usr/bin/python
import shutil, os
from os import walk

current = os.getcwd()

origin_path = f'{current}/origin'
destiny_path = f'{current}/destiny'


f_destiny = []
d_destiny = []
for (dirpath, dirnames, filenames) in walk(destiny_path):
    f_destiny.extend(filenames)
    d_destiny.extend(dirnames)
    break

f_origin = []
d_origin = []
for (dirpath, dirnames, filenames) in walk(origin_path):
    f_origin.extend(filenames)
    d_origin.extend(dirnames)
    break

lst_file_copy = []
lst_file_destiny = []
for f_o in f_origin:
    if f_o not in f_destiny:
        lst_file_copy.append(f'{origin_path}/{f_o}')
        lst_file_destiny.append(f'{destiny_path}/{f_o}')

lst_dir_copy = []
lst_dir_destiny = []
for d_o in d_origin:
  if d_o not in d_destiny:
    lst_dir_copy.append(f'{origin_path}/{d_o}')
    lst_dir_destiny.append(f'{destiny_path}/{d_o}')

for i in range (0, len(lst_dir_copy)):
    shutil.copytree(lst_dir_copy[i], lst_dir_destiny[i])

for i in range (0, len(lst_file_copy)):
  shutil.copy(lst_file_copy[i], lst_file_destiny[i])
