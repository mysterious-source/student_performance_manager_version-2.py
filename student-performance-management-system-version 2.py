students = []
marks_math = []
marks_computer_science = []
marks_english_language = []
marks_english_fist_language = []
marks_physics = []
marks_chemistry = []
marks_biology = []
marks_history = []
marks_geography = []
marks_ICT = []
marks_economics = []
marks_business = []
answer = input('''Welcome to student performance manager. Please select between the numbers to let us know what you want to do:
1-menu
2-Exit
Enter: ''')
while answer.lower() != "exit":
    print("This app is meant for the british system")
    system = input("Are you in the british system?: ")
    if system.lower() in ["yes"," yes","yes "," yes " ,"yeah","yeah "," yeah"," yeah "]:
        print("Ok let's proceed, please answer the questions below")
    else:
        print("Bye! ")
        exit()
    print("This app gives access to students in IB and IGCSE")
    i = input(" Please are you in IB or in IGCSE?: ")
    if i.lower() in ["ig","igcse"]:
        answer = input(''' Please select between the numbers to let us know what you want to do:
1- Add student and their marks              
2-View student
3-Get average
4-View student marks
5-Exit
Enter: ''')
    if "add"  in answer.lower():
        student_name = input("Enter  name: ")
        print("Ok student name added. ")
        subject1 = input("Enter subject : ")
        subject2 = input("Enter subject ")
        subject3 = input("Enter subject ")
        subject4 = input("Enter subject ")
        subject5 = input("Enter subject ")
        subject6 = input("Enter subject ")
        if "Math"  in [subject1 or subject2 or subject3 or subject4 or subject5 or subject6] :
         math_mark = int(input("Enter their math mark: "))
         print("Ok, math mark added")
        else:
            print("Tis student doesn't do Math")
        if "computer"  in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         computer_science_mark = int(input("Enter computer science mark: "))
         print("Ok, computer science mark added")
        else:
            print("This student doesn't do computer science")
        if  "Physics" in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         physics_mark = int(input("Enter their physics mark: "))
         print("Ok, physics mark added")
        else:
            print("This student doesn't do physics")
        if " Chemistry " in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         chemistry_mark = int(input("Enter chemistry mark: "))
         print("Ok, enter chemistry mark added")
        else:
            print("This student doesn't do chemistry")
        if "Biology"  in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         biology_mark = int(input("Enter biology mark: "))
         print("Ok, biology mark has been added")
        else:
            print("This student doesn't do biology")
        if "History" in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         history_mark = int(input("Enter history mark: "))
         print("Ok history mark has been added")
        else:
            print("Thus student doesn't do history")
        if "Geography"  in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         geography_mark = int(input("Enter your geography mark: "))
         print("Ok geography mark has been added")
        else:
            print("This student doesn't do geography")
        if "ICT"  in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         ict_mark = int(input("Enter ICT mark: "))
         print("Ok, ICT mark has been added")
        else:
            print("This student doesn't do ICT")
        if  "Economics"  in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         economics_mark = int(input("Enter economics mark: "))
         print("Ok mark has been added ")
        else:
         print("This student doesn't do economics")
        if "Business" in subject1 or subject2 or subject3 or subject4 or subject5 or subject6:
         business_mark = int(input("Enter business mark: "))
         print("Ok business mark has been added")
        else:
            print("This student doesn't dobusiness")
        marks_geography.append(geography_mark)
        marks_ICT.append(ict_mark)
        marks_economics.append(economics_mark)
        marks_business.append(business_mark)
        students.append(student_name)
        marks_math.append(math_mark)
        marks_history.append(history_mark)
        marks_computer_science.append(computer_science_mark)
        marks_physics.append(physics_mark)
        marks_chemistry.append(chemistry_mark)
        marks_biology.append(biology_mark)

    elif "V" or"VIEW" "v" or "View" or " View" or " View " or "VI" or "Vi" or "vi" in answer.lower():
        a = input("Do you want all student name  or specific student marks")
        if a.lower() == "all student name":
            print("Wait for a minute, we are preparing the resources ")
            print("Your students are: ", students)
        elif a.lower() == "specific student grades":
            student_number = int(input("Enter the number of the student"))
            b = student_number - 1
            average_1 = (marks_math[b] + marks_computer_science[b] + marks_physics[b] + marks_chemistry[b] +
                         marks_biology[b]+marks_history[b]+marks_geography[b]+marks_ICT[b]+marks_economics[b]+marks_business [b]) / 5
            if average_1 >= 90:
                print("This student, has achieved excellent grades in his subjects")
                print("His marks are: ", marks_math[b], marks_computer_science[b], marks_physics[b], marks_chemistry[b],
                      marks_biology[b],marks_history[b],marks_geography[b],marks_ICT[b],marks_economics[b],marks_business [b])
            elif 80 >= average_1 < 90:
                print("This is a good achievement from this student, he got ", average_1, "as his average")
                print("His marks are: ", marks_math[b], marks_computer_science[b], marks_physics[b], marks_chemistry[b],
                      marks_biology[b],marks_history[b],marks_geography[b],marks_ICT[b],marks_economics[b],marks_business [b])

            elif 70 >= average_1 < 80:
                print("This student's results where not bad because he got", average_1, "as his average")
            elif 60 >= average_1 < 70:
                print("This student got a pass mark ,his average is ", average_1)
            elif 50 >= average_1 < 60:
                print("This student's result are not good but he passed with an average of", average_1)
            elif 40 >= average_1 < 50:
                print("This student has failed with an average of", average_1)
            else:
                print("This student has failed badly, his paper couldn't be graded")
    elif answer == "4" or answer.lower() == "view student marks":
        print("The math marks are: ", marks_math)
        print("The computer science marks: ", marks_computer_science)
        print("The physics marks are: ", marks_physics)
        print("The chemistry marks are: ", marks_chemistry)
        print("Yhe biology marks are: ", marks_biology)
    elif answer == "3" or answer.lower() == "get average":
        print(students)
        human_number = int(input("Please enter the number of the student: "))
        computer_number = human_number - 1
        average = (marks_math[computer_number] + marks_computer_science[computer_number] + marks_physics[
            computer_number] + marks_chemistry[computer_number] + marks_biology[computer_number]) / 5
        print(average)

    elif answer == "5" or answer.lower() == "exit":

        pass
