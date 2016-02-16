#!/usr/bin/python3
#coding: UTF-8
import sys
my_file = open(sys.argv[1], "r")
totoal = 0.0;
word_map = {"</s>":0}
for line in my_file:
	line = line.strip()
	word_map["</s>"] += 1
	totoal +=1
	if len(line) != 0:
		word_with_dagbor_list = line.split(" ")
		for word_with_dagbor in word_with_dagbor_list:
			word_list = word_with_dagbor.split(" ")
			for word in word_list:
				if word in word_map:
					word_map[word] +=1
				else:
					word_map[word] = 1
				totoal +=1

for word in word_map:
	print "%s %s" %(word ,word_map[word]/totoal)