import os,sys,re
from time import sleep

global conf
conf={}
# upload files recursively. src[-1] shouldn't be "/" but dest[-1] must be "/".
def upload(src,dest):
	if (os.path.isdir(src)):
		ndest=dest+os.path.split(src)[1]+"/"
		for file in os.listdir(src):
			sleep(1)
			upload(src+"/"+file,ndest)
	else:
		cmd="onedrivecmd put \""+src+"\" \""+dest+"\""
		print("\n\033[36m>"+cmd+"\033[0m")
		if "--dry-run" in conf:
			print("Not exec because of '--dry-run'.")
		else:
			if "--no-try-again" not in conf:
				while (True):
					print("Try transfering...")
					try:
						tmp=os.popen(cmd).read()
					except:
						print("\033[31mTransfer failed, will try again later.\033[0m")
						sleep(2)
						continue
					print("\033[33mshell message:\033[0m "+tmp)
					if (re.search("Annotations",tmp)==None):
						print("\033[4mTransfer finished!\033[0m")
						break
					else:
						print("\033[31mTransfer failed, will try again later.\033[0m")
						sleep(2)
					
			else:
				os.system(cmd)
				print(1)

src=sys.argv[1]
dest=sys.argv[2]
for i in range(3,len(sys.argv)):
	conf[sys.argv[i]]=True
if (src[-1]=='/'):
	src=src[:-1]
if (dest[-1]!="/"):
	dest=dest+"/"	
upload(src,dest)