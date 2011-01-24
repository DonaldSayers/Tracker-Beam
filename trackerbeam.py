
import sys,re

def parse(data):
	allmatches = re.findall("(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z])| ?(96 ?[0-9]{20})| ?(91 ?[0-9]{20})| ?([0-9]{30}|[0-9]{20}|[a-z]{2} ?[0-9]{9} ?[a-z]{2})| ?([a-z]{3} ?[0-9]{6}|[0-9]{15}|[0-9]{12})", data)
	##usps = re.findall("( ?[0-9]{30})", data)
	##usps += re.findall("( ?[0-9]{20})", data)
	
	for (ups,fx,uusps,usps,fedex) in allmatches:
		if ups:
			print "got ups,  ", ups
		elif usps:
			print "got usps, ", usps
		elif uusps:
			print "got usps, ", uusps
		elif fx:
			print "got fedex,", fx			
		else:
			print "got fedex,", fedex

if len(sys.argv)<2:
	print "No Source File Specified."
else:
	f = open(sys.argv[1], "r")
	data=f.read()
	parse(data)
