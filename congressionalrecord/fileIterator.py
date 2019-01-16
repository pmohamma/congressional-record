import os

rootdir = 'C:/Users/pouya\python-projects\congressional-record\congressionalrecord\output'

for subdir, dirs, files in os.walk(rootdir):
  for file in files:
    if file.endswith('.htm'):
      fname = subdir + '\\'+ file
      f = open(fname, 'r')
      contents = ""
      for line in f:
        contents += line
        #print (os.path.join(subdir, file))
      f.close()
      bodystart = contents.index('<body>') + 6
      bodyend = contents.index('</body>')
      contents = contents[bodystart:bodyend]
      print(contents)