#!/usr/bin/env python3

import fileinput

def expand(url):
	expansion = []
	url = url.replace("://", ":||").rstrip().rstrip("/")
	path_segments = url.split("/")
	# loop len(path_segments) times, that's how many urls we'll end up with. 
	for i in range(0, len(path_segments)):
		new_url = ""
		for segment in path_segments:
			new_url = new_url + segment + "/"
		expansion.append(new_url.replace(":||", "://")[0:-1])
		path_segments.pop()
	return expansion

for line in fileinput.input():
	for i in expand(line):
		print(i)


