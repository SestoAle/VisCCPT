from sys import platform
import gdown
import zipfile
import os


'''--------------'''
'''Check for Data'''
'''--------------'''

if platform != 'linux' and platform != 'linux2':
    raise Exception("The environment is available only on Linux")

print("Downloading pre-made data...")
gdown.download(id="1WMMR4RUpQk2VMnn7JLsHlZ9A-iBh-POR", output='arrays/experiments.zip')
print("Downloading models...")
gdown.download(id="1GOjfLQqCBk3DLrOZXkbBF0YHEZttISMm", output='saved/models.zip')

print("Extracting files...")
with zipfile.ZipFile("arrays/experiments.zip", 'r') as zip_ref:
    zip_ref.extractall("arrays/")
with zipfile.ZipFile("saved/models.zip", 'r') as zip_ref:
    zip_ref.extractall("saved/")

os.remove('arrays/experiments.zip')
os.remove('saved/models.zip')
