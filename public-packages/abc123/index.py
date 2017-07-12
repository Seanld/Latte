# The main program that gets called whenever the package is run from StaSh.

import sys
import argparse

def main(sargs):
	parser = argparse.ArgumentParser()
	parser.add_argument("echo", help="What (no-spaced) text you want the program to echo back", type=str)
	args = parser.parse_args(sargs)

	print("Echoed back: " + args.echo)

if __name__ == "__main__":
	main(sys.argv[1:])
