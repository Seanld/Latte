# A package manager meant for Pythonista, built on StaSh.

import requests
import sys
import argparse
import tarfile
from os import mkdir, rename
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
		os.mkdir("stash_extensions/bin/"+args.package)
		rename(args.package+"/lib", "stash_extensions/bin/"+args.package+"/lib")
		rmtree(packagec)
		print("Successfully installed!")
	elif args.method == "remove":
		pass # Uninstall a package
	elif args.method == "update":
		pass # Check for any Latte updates
	else:
		raise Exception("Unknown argument '" + args.method + "'!")

if __name__ == "__main__":
	main(sys.argv[1:])
