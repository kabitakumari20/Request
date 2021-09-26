import requests
import json
course=[]
id_list=[]
slug_list=[]
print("*****************welcome****meraki navgurukul***************************")
def frist_api():
    res=requests.get("http://saral.navgurukul.org/api/courses")
    print(res)
    # json object me conver karte hai
    a = res.json()
    # print(type(a))
    with open ("courses.json","w") as f:
        json.dump(a,f,indent=4)
    course_list=(a["availableCourses"])
    # print(course_list)
    courses_index=0
    while courses_index<len(course_list):
        course_available=course_list[courses_index]["name"]
        course.append(course_available)
        id_available=course_list[courses_index]["id"]
        id_list.append(id_available)
        print(courses_index,course_available,id_available)
        courses_index+=1
frist_api()
user=int(input("enter the id ="))
b=id_list[user]
def second_api(user):
    data2=requests.get("http://saral.navgurukul.org/api/courses/"+ b +"/exercises")
    content = data2.json()
    with open("data1.json","w") as f2:
        json.dump(content,f2,indent=4)
    i=0
    while i<len(content["data"]):
        print(i+1,content["data"][i]["name"])
        print()
        if content["data"][i]["childExercises"]==[]:
            print("          ",    "[]")
            
            store=content["data"][i]["slug"]
            slug_list.append(store)
        else:
            j=0
            while j<len(content["data"][i]["childExercises"]):
                print("            ",     j+1,content["data"][i]["childExercises"][j]["name"])
                j+=1
        i+=1 
second_api(user)
i=0
while i<len(slug_list):
    print(i,slug_list[i])
    i=i+1
slug=int(input("entre the slug="))
def third_api(slug):
    data3=requests.get(" http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+slug_list[slug])
    content1=data3.json()
    with open ("data3.json","w") as f3:
        json.dump(content1,f3,indent=4)
    with open("data3.json","r") as f4:
        w=json.load(f4)
        print(w["content"])   
third_api(slug)
user=input("enter the up/next/perivous=")
if user=="up":
    frist_api()
    second_api(user)
    third_api(slug)
elif user=="next":
    slug=slug+1
    if slug<len(slug_list):
        third_api(slug)
    else:
        print("sorry-----------page nor found")
        # break
    print("")
elif user=="perivous":
    slug=slug-1
    if slug>=0:
        third_api(slug)
    else:
        print("page not found")
    print("")
else:
    print("invaild input")
    # print(" ")
user1=input("enter the you want stop/you want to again run=")
i=1
while i<=2:
    if user1=="stop":
        break
    else:
        if user=="up":
            frist_api()
        elif user=="next":
            slug=slug+1
            if slug<len(slug_list):
                third_api(slug)
            else:
                print("sorry-----------page nor found")
                # break
            print("")
        elif user=="perivous":
            slug=slug-1
            if slug>=0:
                third_api(slug)
            else:
                print("page not found")
            print("")
        else:
            print("invaild input")
    i=i+1