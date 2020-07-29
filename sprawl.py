#!/usr/bin/env python3

import argparse, textwrap, sys

parser = argparse.ArgumentParser(description = "Expand a list of paths into a much larger wordlist by creating an entry for each path depth.")

parser.add_argument('-s', '--slash', default=False, action="store_true", help="prefix each line with a /, this is left off by default.")
args = parser.parse_args()

prefix = "/" if args.slash else ""

def read_in():
	# Read contents of stdin
	return [x.strip() for x in sys.stdin.readlines()]

def strip_extra(line):
	# Remove protocol handler, domain, querystring
	line = line[1:] if line[0] == "/" else line
	line = "/".join(line.split("/")[3:]) if "//" in line else line
	return line.split("?")[0] if "?" in line else line

def tokenize(line):
	return line.split("/")

def expand(input_line):
	# tokenize the line
	tokens = tokenize(input_line)

	expansion = []
	for t in tokens:
		# add each token by itself as a line
		expansion.append(t)
	for index in range(len(tokens)):
		# truncate each path depth and add each result
		line = "/".join(tokens[0:index+1])
		expansion.append(line)
	for index in range(len(tokens)):
		line = "/".join(tokens[index+1:])
		expansion.append(line)
	return expansion


input_data = read_in()

output_set = set()

for line in input_data:

	line = strip_extra(line)
	expansion = expand(line)
	for entry in expansion:
		output_set.add(f"{prefix}{entry}")

for entry in output_set:
	print(entry)

