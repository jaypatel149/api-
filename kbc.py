#part 1
question_list=["1.who wrote the mahabharat?","2.what is the capital of India?","3.what is apples colour?","4.what is tree colour?","5.how many months there are in a year?","6.who is the computer invetor?","7.What was the of the first computer?","8.When was the search for a modern computer first?","9.when did the great revalution in the field of computer?","10.what is hindi name of computer?","11.computer literacy day is celebrated?","12.what is the full name of CPU","13.which of these is the search engine?","14.which of the input units is?","15.how many bytes of 1 KB are equal to?"]
first_options=["1.vedavyas","1.Delhi","1.red","1.purple","1.15","1. wannumen","1.ATARIS","1.1949","1.1977","1.garna karnewaala","1.5 Disember","1.Central processing Unit","1.Google","1.mouse","1.1024 byte"]
second_options=["2.valmiki","2.bhopal","2.blue","2.Green","2.6","2.GS kilvi","2.ENIC","2.1951","2.2000","2.sangndak","2.14.Disember","2.Central problem Unit","2.Yahoo","2.key_board","2.1024 Gega byte"]
third_options=["3.tulsidas","3.jaipur","3.yello","3.white","3.13","3.charls baibej","3.TANDY","3.1946","3.1955","3.hisab karnewaala","3.22 Disember","3.Central processing Union","3.Baidu","3.scanner","3.1024 mega byte"]
fourth_options=["4.non of the above","4.chandigarh","4.black","4.pink","4.12","4.non of the above","4.NOVELLA","4.1947","4.1960","4.parigadak","4.2 Disember","4.non of the above","4.Wolfrom Alpha","4.non of the above","4.non of the above"]
win_Rs=[000,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
ans_key=[2,1,1,2,4,3,2,3,4,2,4,1,4,4,1]


for i in range(len(question_list)):
	print question_list[i], len(question_list[i])
	print first_options[i]
	print second_options[i]
	print third_options[i]
	print fourth_options[i]
	user = int(raw_input("Enter the correct option "))
	if user == ans_key[i]:
		print "App jeet gaaye,"
		print "win_Rs",win_Rs[i+1]
	else:
		print "App haar gaaye "
		print "total_Rs",win_Rs[i]
		break
	if i==4:
		print "congrats! Aapka padaav pura ho gaya hai"
		print "                                        "
	elif i==9:
		print "congrats! Aapka padaav pura ho gaya hai"
		print "                                       "
print " "
print "Congratulation Aap",win_Rs[i],"Aap etane rupees jeet chuke hai"

