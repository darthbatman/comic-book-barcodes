import requests

def getComicBook(mainBarcode, issueCode):
	r = requests.get("http://www.upcitemdb.com/upc/" + mainBarcode)
	numNameVariations = len(r.content.split("<td><b>")) - 1
	masterName = r.content.split("<td><b>")[1].split("</b></td>")[0]
	for i in range (2, numNameVariations + 1):
		currentName = r.content.split("<td><b>")[i].split("</b></td>")[0]
		minNameLength = 0
		if (len(currentName) < len(masterName)):
			minNameLength = len(currentName)
		else:
			minNameLength = len(masterName)
		if (i > 1):
			tempName = ""
			for j in range (0, minNameLength - 1):
				if (currentName[j] == masterName[j]):
					tempName += currentName[j]
				else:
					masterName = tempName
					break
	masterName = masterName[:len(masterName) - 1]
	issueCode = issueCode[:len(issueCode) - 2]
	for i in range (0, len(issueCode)):
		if issueCode[0] == "0":
			issueCode = issueCode[1:]
	return {"series": masterName, "issue": issueCode}

print getComicBook("761941311586", "00111")


