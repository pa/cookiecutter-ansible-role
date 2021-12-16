import os
import shutil

source_dir = os.getcwd()
target_dir = "{{ cookiecutter.destination_dir }}"

if( not target_dir.startswith('#')):
    files_list = os.listdir(source_dir)
    for file in files_list:
        shutil.move(source_dir + file, target_dir + file)
