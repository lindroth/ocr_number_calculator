#!/usr/bin/python

import sys
import math

invoice_number = sys.argv[1]

#The caclulated ocr number contains three parts. The invoice number, lenght digit and checksum digit.
def ocr(invoice_number):
	partial_ocr = invoice_number + length_number(invoice_number)
	return partial_ocr + calculate_checksum(partial_ocr)

def calculate_checksum(invoice_number):
	checksum = 0
	#The checksum is calculated in reverse, right to left.
	for idx, x in enumerate(reversed(invoice_number)):
		#each x is multiplied by a weigth that is 1 or 2 starting on 2
		weigth = (idx + 1)%2 + 1
		result = int(x) * weigth
		if result > 9:
			result = result - 9
		checksum = checksum + result

	return str(roundup(checksum) - checksum)

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

# Length is represented by only one digit, 3, 13, 23 are all represented by 3. 5, 15, 25 by 5 etc.
# The length is the invoice number including the length digit and checksum digit, therefor the +2
def length_number(invoice_number):
	return str((len(invoice_number)+2) % 10)

print 'ocr:', ocr(invoice_number)
