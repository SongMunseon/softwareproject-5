import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]
			if len(parse)>=4:
			    print("잘못입력하셨습니다.")
		elif parse[0] == 'del':
			if len(parse)==2:
			    for p in scdb:
				    if p['Name'] == parse[1]:
					     scdb.remove(p)
			    if p['Name'] != parse[1]:
				    print("그 사람은 없습니다")
			else:
				print("잘못입력하셨습니다.")
					#고 침
		elif parse[0] == 'show':
			try:
			    sortKey ='Name' if len(parse) == 1 else parse[1]
			    showScoreDB(scdb, sortKey)
			except:
				print("잘못입력하셨습니다.")
		elif parse[0] == 'quit':
			if len(parse) == 1:
			    break
			else:
				print("잘못입력하셨습니다")
		elif parse[0] == 'find':
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						print(p['Name'] , p['Age'] , p['Score'])
				if p['Name'] != parse[1]:
						print("존재하지 않습니다.")
			except:
				print("잘못입력하셨습니다.")
		elif parse[0] == 'inc':
			if len(parse) == 3:
				for p in scdb:
					if p['Name'] == parse[1]:
						p['Score']+=parse[2]
				if p['Name'] != parse[1]:
						print("존재하지않는이름입니다.")
			else:
				print("잘못입력하셨습니다.")
			
		else:
			print("Invalid command: " + parse[0])
		
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

