# A package manager meant for Pythonista, built on StaSh.

import requests
import sys
import argparse
import tarfile
from os import remove, mkdir, rename
from shutil import rmtree

def main(sargs):
	parser = argparse.ArgumentParser()
	parser.add_argument("method", help="What action to perform (install, remove, etc)", type=str)
	parser.add_argument("package", help="Name of package", type=str)
	args = parser.parse_args(sargs)

	if args.method == "install":
		packagec = args.package+".tar.gz"
		url = "https://raw.githubusercontent.com/Seanld/Latte/master/public-packages/"
		print("Downloading " + packagec)
		try:
			request = requests.get(url+packagec, stream=True)
		except:
			print("Package doesn't exist")
		data = request.raw.read()
		opened = open(packagec, "wb")
		opened.write(data)
		opened.close()
		# Now inflate the new package, and move all contents to correct locations
		print("Extracting contents")
		tar = tarfile.open(packagec, "r:gz")
		tar.extractall()
		tar.close()
		# Move to correct locations
		print("Installing")
		rename(args.package+"/meta.latte", "stash_extensions/bin/"+args.package+".latte")
		rename(args.package+"/index.py", "stash_extensions/bin/"+args.package+".py")
		mkdir("stash_extensions/bin/"+args.package)
		rename(args.package+"/lib", "stash_extensions/bin/"+args.package+"/lib")
		remove(packagec)
		remove(args.package)
		print("Successfully installed!")
	elif args.method == "remove":
		remove("stash_extensions/bin/"+args.package+".latte")
		remove("stash_extensions/bin/"+args.package+".py")
		mkdir("stash_extensions/bin/"+args.package)
		print("Removed "+args.package+" successfully!")
	elif args.method == "update":
		pass # Check for any Latte updates
	elif args.method == "new":
		mkdir(args.package)
		mkdir(args.package+"/lib")
		config = open(args.package+"/"+args.package+".latte", "w")
		config.write("str developer=Your name here\nstr description=Enter description of your app here\nfloat version=0.1")
		config.close()
		index = open(args.package+"/index.py", "w")
		index.write("import sys\nimport argparse\n\ndef main(sargs):\n\tparser = argparse.ArgumentParser()\n\tparser.add_argument('echo', help='What you want the command to echo back.')\n\targs = parser.parse_args(sargs)\n\t\n\tprint('Echoing back: '+args.echo)\n\nif __name__ == '__main__':\n\tmain(sys.argv[1:]")
		index.close()
		external = open(args.package+"/lib/external.py", "w")
		external.write("# You can put any extra programs or dependencies your command requires in this /lib folder. This is the best counter to a crowded /bin folder in StaSh.")
		external.close()
	else:
		raise Exception("Unknown argument '" + args.method + "'!")

if __name__ == "__main__":
	main(sys.argv[1:])
