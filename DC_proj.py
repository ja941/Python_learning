import filecmp
import os

DR_path = input('Enter path for DR files:\n')
DC_path = input('Enter path for DC files:\n')
fails_dir = input('Enter a path for fails log:\n')

DR_files = []
DC_files = []

if DR_path == DC_path:
    for i in os.listdir(DR_path):
        if i.startswith('DR'):
            DR_files.append(DR_path + '/' + i)
        elif i.startswith('DC'):
            DC_files.append(DC_path + '/' + i)
DR_files.sort(), DC_files.sort()

if len(DR_files) != len(DC_files):
    exit()

# print(DR_files, DC_files)
fails = []
filecmp.clear_cache()

for i in range(len(DR_files)-1):
    cmp_result = filecmp.cmp(DR_files[i], DC_files[i], False)
    if cmp_result is False:
        fails.append(DR_files[i])
        fails.append(DC_files[i])

fails_doc = open(fails_dir + '/fails.txt', 'w')

for i in fails:
    fails_doc.write(str(i)+'\n')
fails_doc.close()
