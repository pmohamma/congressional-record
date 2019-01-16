import os

rootdir = 'C:/Users/pouya\python-projects\congressional-record\congressionalrecord\output'

for subdir, dirs, files in os.walk(rootdir):
  for file in files:
    if file.endswith('.htm'):
      fname = subdir + '\\'+ file
      f = open(fname, 'r')
      for line in f:
        print(line)
        #print (os.path.join(subdir, file))
      f.close()