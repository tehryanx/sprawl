#!/usr/bin/env python3

import fileinput

def expand(path):
	expansion = []
	path = path.rstrip().rstrip("/")
	if "://" in path:
		protocol=path.split("://")[0]
		path=path.split("://")[1]
	else:
		protocol = False

	path_segments = path.split("/")
	for i in range(0, len(path_segments)):
		new_path = ""
		for segment in path_segments:
			new_path = new_path + segment + "/"
		if new_path: 
			if protocol:
				new_path = protocol + "://" + new_path
			expansion.append(new_path[0:-1]) 
		path_segments.pop()
	path_segments = path.split("/")
	for i in range(0, len(path_segments)):
		new_path = ""
		path_segments.pop(0)
		for segment in path_segments:
			new_path = new_path + segment + "/"
		if new_path:
			if protocol:
				new_path = protocol + "://" + new_path
			expansion.append(new_path[0:-1])
	return expansion

def expandx(url):
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
	path_segments = url.split("/")
	for i in range(0, len(path_segments)):
		new_url = ""
		path_segments.pop(0)
		for segment in path_segments:
			new_url = new_url + segment + "/"
		expansion.append(new_url.replace(":||", "://")[0:-1])
	return expansion

for line in fileinput.input():
	for i in expand(line):
		print(i)


