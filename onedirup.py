import os,sys
from time import sleep

# upload files recursively. src[-1] shouldn't be "/" but dest[-1] must be "/".
def upload(src,dest):
	if (os.path.isdir(src)):
		ndest=dest+os.path.split(src)[1]+"/"
		for file in os.listdir(src):
			sleep(1)
			upload(src+"/"+file,ndest)
	else:
		cmd="onedrivecmd put \""+src+"\" \""+dest+"\""
		print("\033[32m >"+cmd+"\033[0m")
		os.system(cmd)

src=sys.argv[1]
dest=sys.argv[2]
if (src[-1]=='/'):
	src=src[:-1]
if (dest[-1]!="/"):
	dest=dest+"/"	
upload(src,dest)