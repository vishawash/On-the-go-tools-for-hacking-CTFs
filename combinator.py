#!/usr/bin/python3
"""
Combinator- A python based dictionary generator
Author- VeeKay aka Vishawash
last modified on 06/08/18 4:47 pm


"""

# usage ./combinator.py -c <Max no. of words per combo> -f <filename> word1 word2 ......
import sys
from optparse import OptionParser
def combination(word_list,word_num):
	
	nvar=len(word_list)
	max_num=pow(nvar,word_num)
	
	combo_list=[]
	#print(word_list)
	for num in range(max_num):
		word_combo=""
		for digit in range(word_num):
			word_combo+=word_list[int((num/pow(nvar,digit))%nvar)]
		#print(word_combo)
		combo_list.append(word_combo)
	
	return combo_list
parser = OptionParser()
parser.add_option("-c","--count",dest="count",help="Write the max no. of words to be included in a single combination defaults to 4",default=4)
parser.add_option("-f","--filename",dest="filename",help="Write the filename for the dictionary ",default="new")

wlist = parser.parse_args()[1]
(options, args) = parser.parse_args()
#combination zone

combin = int(options.count)
raw_list = wlist
print(raw_list)

#print(combination(raw_list,4))

#file opens here
filename=options.filename+".dict"
dic = open(filename,"w")
for stage in range(1,combin+1):
	#dic.write("stage "+str(stage)+"\n")
	combinated_list=[]
	combinated_list=combination(raw_list,stage)
	for word in combinated_list:
		dic.write(word+"\n")		
dic.close()
