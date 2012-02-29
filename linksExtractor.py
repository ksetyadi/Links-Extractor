import sys

def linksExtractor(text):
	start = 0
	status = 1
	
	while status != -1:
		status = text.find("<a", start)
		
		if status != -1:
			start = status
			end = text.find("</a>", start)
			hrefPos = text.find("href=", start)
			linkPos = hrefPos + 6
			linkEndPos = text.find("\"", linkPos)
			linkStr = text[linkPos:linkEndPos]
			descPos = text.find(">", start) + 1
			descEndPos = end
			descStr = text[descPos:descEndPos]
			
			if (linkStr.find("http") != -1):
				print descStr
				print linkStr + "\n"
			
			start = end


try:
	fileSrc = open("sample.html", "r")
except IOError:
	print >> sys.stderr, "File could not be opened"
	sys.exit(1)
	
lines = fileSrc.readlines()

for line in lines:
	linksExtractor(line)