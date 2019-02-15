import requests
import json
# url= "http://saral.navgurukul.org/api/courses"
# a= requests.get(url)
# # print(a)
# data=a.json()
# # print(data)
# v = (a.text)

# with open("courses.json","w") as var:
# 	var.write(a.text)

x= open("courses.json","r+")
j=json.load(x)
# print (type(j))
y= j["availableCourses"]
# print (y[0]["name"])

for i in range(len(y)):
	print (i,y[i]['name'])
user=int(input("Enter any input:"))
for i in range(len(y)):
	if user == i:
		ID=(y[i]['id'])
		print (ID)
		# link=" http://saral.navgurukul.org/api/courses/"+str(ID)+"/exercises"
		# d=requests.get(link)
		# inf=d.json()
		# # print (inf)

# data1=inf["data"]
# # print (data1)
# number=0
# for i in data1:
# 	name=i["name"]
# 	childexercise=i["childExercises"]
# 	print (number,name)
# 	number+=1
# 	print ("                   ",childexercise)
# user=int(input("enter your exercises index"))
# slug=data1[user]["slug"]
# print (slug)
# r=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+slug)
# print(r.text)