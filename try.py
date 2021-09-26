import requests
import json
course=[]
id_list=[]
slug_list=[]

print("*****************welcome****meraki navgurukul***************************")

def frist_api():

    res=requests.get("http://saral.navgurukul.org/api/courses")
    print(res)
    a = res.json()
    print(type(a))

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
        # print()
        courses_index+=1

frist_api()

def second_api():
    global b
    user=int(input("enter the id ="))
    b=id_list[user]
    data2=requests.get("http://saral.navgurukul.org/api/courses/"+ b +"/exercises")
    content = data2.json()

    with open("data1.json","w") as f2:
        json.dump(content,f2,indent=4)
    i=0
    while i<len(content["data"]):
        print(i+1,content["data"][i]["name"])
        print()
        if content["data"][i]["childExercises"]==[]:
            print("       ",  "[]")
            store=content["data"][i]["slug"]
            slug_list.append(store)
        else:
            j=0
            while j<len(content["data"][i]["childExercises"]):
                print("         ",j+1,content["data"][i]["childExercises"][j]["name"])
                j+=1
        i+=1 
    # print("   " ,  slug_list)
second_api()

i=0
while i<len(slug_list):
    print(i+1,slug_list[i])
    i=i+1

def third_api(): 
    user=int(input("enter the id ="))
    b=id_list[user]   
    while True:
        user=input("entre the slug/up=")
        user=input("enter the slug=")
        if user=="up":
            frist_api()
            second_api()
        # third_api()
        if user=="slug":
            length=len(slug_list)
            slug_index=int(input("enter the slug_index="))
            # data3=requests.get(" http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+slug_list[slug])
            # data3=reque/sts.get(" http://saral.navgurukul.org/api/courses/"+str(b)+")+"/exercise/getBySlug?slug="+slug_list[slug])
            var=(" http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json")
            var=var.replace("requests_using-json",(slug_list[slug_index]))
            var=var.replace("75",str(b))
            call=requests.get(var)
            print(call.text)

            while True:

                user=input("enter the up/next/perivous/exit=")
                print(" ")
                if user=="up":
                    frist_api()
                    second_api()
                    # third_api()
                elif user=="next":
                    if slug_index==length-1:
                        print("no next slug exits")
                    else:
                        var=var.replace((slug_list[slug_index]),(slug_list[slug_index+1]))
                        call2=requests.get(var)
                        print(call2.text)
                        # third_api()

                elif user=="perivous":
                    if slug_index==0:
                        print("no pervious")
                    else:
                        var=var.replace((slug_list[slug_index]),( slug_list[slug_index-1]))
                        call1=requests.get(var)
                        print(call1.text)
                        third_api()
                else:
                    print("***************Exit***************")
                    print("****************THANKU************")
                    break
            
third_api()
