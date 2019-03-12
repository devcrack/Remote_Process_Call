import os
from os.path import join, getsize
for root, dirs, files in os.walk('.'):
    print(root)
    # print sum(getsize(join(root, name)) for name in files),
    # print "bytes in", len(files), "non-directory files"
    # if 'CVS' in dirs:
    #     dirs.remove('CVS')  # don't visit CVS directories
    for filename in files:
        print(filename)
