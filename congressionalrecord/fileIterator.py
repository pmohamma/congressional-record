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
	      contents = cleanForSpeeches(contents)
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

def cleanForSpeeches(contents):
  record = ""
  while (True):
    if ("Mr." not in contents and "Mrs." not in contents and "Ms." not in contents):
      break
    else:
      spotToCheck = float('inf')
      prefixes = ["Mr. ", "Mrs. ", "Ms. "]
      for prefix in prefixes:
      	temp = contents.find(prefix)
      	if temp >= 0 and temp < spotToCheck:
      	  spotToCheck = temp + len(prefix)

      #TODO: Account for names like McGOVERN and LaMALFA
      if (contents[spotToCheck+1].isupper() and contents[spotToCheck+2].isupper()):
   	  	contents = contents[spotToCheck:]
   	  	continue
      else:
   	    endSpot = contents.find("____________________")
   	    record += contents[spotToCheck:endSpot]
   	    contents = contents[endSpot:]
  return record
main()