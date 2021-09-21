#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	co = 0
	for c in text:
		if (c.isalnum()):
			co+=1
	return co

def get_word_length_histogram(text):
	maxi = 0
	li = [0]*(len(text)+1)
	for mot in text.split():
		li[get_num_letters(mot)] += 1
		maxi = max(maxi,get_num_letters(mot))
	return li[:maxi+1]

def format_histogram(histogram):
	ROW_CHAR = "*"
	result = ""
	maxlen = len(histogram)
	for i in range(1,len(histogram)):
		result += " "*(len(str(maxlen))-len(str(i)))+str(i)+" "+ROW_CHAR*histogram[i]+"\n"
	return result[:-1]

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	result = ""
	for i in range(max(histogram),0,-1):
		for lenght in histogram[1:]:
			if(i <= lenght):
				result+= BLOCK_CHAR
			else :
				result+= " "
		result+="\n"
	result+= LINE_CHAR*(len(histogram)-1)
		
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
