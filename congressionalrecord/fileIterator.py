import os

def main():
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
	      contents = cleanContents(contents)
	      print(contents)

def cleanContents(contents):
  bodystart = contents.index('<body>') + 6
  bodyend = contents.index('</body>')
  ret = contents[bodystart:bodyend]
  if (ret.index("<pre>") != -1):
  	retstart = ret.index('<pre>') + 5
  	retend = ret.index('</pre>')
  	ret = ret[retstart:retend]
  return ret

main()