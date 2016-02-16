#coding:UTF-8
import sys,  math
prob_map = {}

model_file = open(sys.argv[1], "r")

for line in model_file:
	line = line.strip()
	pair = line.split(" ")
	prob_map[pair[0]]=pair[1]
print prob_map.keys()
H = 0.0
test_file = open(sys.argv[2], "r")
word_count = 0
unk_count = 0
for line in test_file:
	line = line.strip()
	word_array = line.split(" ")
	word_array.append("</s>")
	for word in word_array:
		word_count += 1
		p = (1 - 0.95) / 1000000.0
		# print "%.10f" %p
		if word in prob_map.keys():
			# print "    %.10f" % float(prob_map[word])
			p = p + 0.95 * float(prob_map[word])
			# print p
		else:
			unk_count += 1
		H += -math.log(p, 2)
		print "%5s,p=%.10f, -lb=%.10f" % (word, p, -float(math.log(p, 2)))
# print "H:%d" % H
print "word num:%d" % word_count
print "entropy=%.10f" % float(H / word_count )
