#!/usr/bin/python

import sys
import math

invoice_number = sys.argv[1]

def ocr(invoice_number):
	return invoice_number + calculate_checksum(invoice_number)

def calculate_checksum(invoice_number):
	checksum = 0
	for idx, x in enumerate(invoice_number):
		weigth = (idx + 1)%2 + 1
		result = int(x) * weigth
		if result > 9:
			result = result - 9
		checksum = checksum + result

	return str(roundup(checksum) - checksum)

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

print 'invoice_number', invoice_number
print 'ocr', ocr(invoice_number)
