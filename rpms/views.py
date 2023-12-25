from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
import uuid
import json

day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year

date = f"{day}-{month}-{year}"

def calculate_position_and_highest_mark(stu_id):
    # Get all the students and their marks
    results = Result.objects.get(stu_id=stu_id)
    reportCard = ReportCard.objects.filter(stu_id=stu_id)

    # Sort the results by marks in descending order
    sorted_reports = reportCard.order_by('-overAll_marks')

    # Calculate the total number of students in the class
    total_students = len(sorted_reports)

    # Initialize variables to track position and highest mark
    position = None
    highest_mark = None

    # Loop through the sorted results to find the position and highest mark
    for i, report in enumerate(sorted_reports):
        if i == 0:
            highest_mark = report.overAll_marks
        if report.stu_id == stu_id:
            position = i + 1  # Adding 1 because position starts from 1, not 0
            break

    return position, highest_mark, total_students


def index(request):
    return render(request, 'index.html')

def report_card(request, id):
    results = Result.objects.filter(check_id=id)
    report_card = ReportCard.objects.get(check_id=id)
    students = Student.objects.filter(class_name=report_card.stu_id.class_name)
    total_stu = len(students)
    context = {
        'report': report_card,
        'results': results,
        'total_stu':total_stu,
    } 
    return render(request, "report-card.html", context)

@login_required(login_url='login')
def dashboard(request):
    classes = StudentClasses.objects.all()
    class_s = len(classes)

    students = Student.objects.all()
    student = len(students)

    subjects = Subject.objects.all()
    subject = len(subjects)

    results = ReportCard.objects.all()
    result = len(results)
    current_user = Staff.objects.get(user=request.user)
    context = {
        "class": class_s,
        "current_user": current_user,
        "student": student,
        "subject": subject,
        "result": result,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def student_class(request):
    current_user = Staff.objects.get(user=request.user)
    classes = StudentClasses.objects.all()
    subjects = Subject.objects.all()
    context = {
        "classes": classes,
        "current_user":current_user,
        "subjects": subjects
    }
    if request.method == 'POST':
        class_name = request.POST['class_name']
        subj_name = request.POST['subj']
        term = request.POST['term']

        if StudentClasses.objects.filter(class_name=class_name).exists():
            error = "This class name already exist!!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        else:
            new_class = StudentClasses.objects.create(class_name=class_name, term=term, subjects=subj_name, date_registered=date)
            new_class.save()
            success = 'Class Registered Successfully..'
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
    return render(request, "student-classes.html", context)

@login_required(login_url='login')
def add_staff(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        staff_phone = request.POST['staff_phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        role = request.POST['role']
        address1 = request.POST['address1']
        #  next of kin
        full_name = request.POST['full_name']
        p_number = request.POST['p_number']
        address2 = request.POST['address2']
        email2 = request.POST['email2']

        if User.objects.filter(username=username).exists():
            error = "Username aready taken!!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        elif User.objects.filter(email=email).exists():
            error = "Email aready exists!!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        elif len(password) < 8:
            error = "Password should be atleast 8 characters above !!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        elif cpassword != password:
            error = "Password and Confirm password missed match!!!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        else:
            new_staff = User.objects.create_user(
                username=username, email=email, password=password
            )
            new_staff.save()

            user_model = User.objects.get(username=username)
            new_profile = Staff.objects.create(
                user=user_model, id_user=user_model.id, f_name=fname, m_name=mname, l_name=lname, dob=dob,
                gender=gender, role=role, staff_address=address1, staff_phone=staff_phone, n_fullname=full_name, 
                n_phone_number=p_number, n_email=email2, n_address=address2, staff_id='STAFF/'+str(user_model.id),
                staff_fullname=f"{fname} {lname} {mname}", date_registered=date
            )
            new_profile.save()

            success = "Staff Added successfully..."
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
        

# def getStaffs(request):
#     staffs = Staff.objects.all()
#     data = [staff.staffData() for staff in staffs]
#     response = {'data': data}
#     return JsonResponse(response)

@login_required(login_url='login')
def staff(request):
    current_user = Staff.objects.get(user=request.user)
    staffs = Staff.objects.all()
    context = {
        "staffs":staffs,
        "current_user":current_user
    }
    return render(request, 'staff.html', context)

@login_required(login_url='login')
def subject(request):
    current_user = Staff.objects.get(user=request.user)
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
        "current_user":current_user
    }
    if request.method == 'POST':
        subj_name = request.POST['subj_name']
        subj_descript = request.POST['subj_descript']

        if Subject.objects.filter(subject_name=subj_name).exists():
            error = "This subject already exist!!"
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        else:
            new_subject = Subject.objects.create(subject_name=subj_name, description=subj_descript, date_registered=date)
            new_subject.save()
            success = 'Subject Registered Successfully..'
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
    return render(request, "subjects.html", context)

@login_required(login_url='login')
def student(request):
    current_user = Staff.objects.get(user=request.user)
    classes = StudentClasses.objects.all()
    students = Student.objects.all()
    context = {
        'classes': classes,
        'students': students,
        "current_user":current_user
    }
    if request.method == 'POST':
        stu_uuid = uuid.uuid4()
        fname = request.POST['fname']
        lname = request.POST['lname']
        mname = request.POST['mname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        stu_address = request.POST['stu_address']
        student_class = request.POST['student_class']
        term = request.POST['term']
        full_name = request.POST['full_name']
        p_number = request.POST['p_number']
        g_address = request.POST['g_address']
        relationship = request.POST['relationship']
        email = request.POST['email']
        stu_fullname = f"{fname} {lname}"

        new_stu = Student.objects.create(
            f_name=fname, l_name=lname, m_name=mname, dob=dob, gender=gender, stu_address=stu_address,
            g_fullname=full_name, g_phone_number=p_number, g_address=g_address, relationship=relationship,
            email=email, date_registered=date, class_name=student_class, term=term, stu_uuid=stu_uuid, stu_fullname=stu_fullname
        )
        new_stu.save()

        stu_id = Student.objects.get(stu_uuid=stu_uuid)
        stu_id.stu_id = f"STU/-{stu_id.id}"
        stu_id.save()

        success = 'Student Registered Successfully..'
        response_data = {'success': True, 'message': success}
        return JsonResponse(response_data)
    return render(request, "students.html", context)

def result(request):
    results = Result.objects.all()
    current_user = Staff.objects.get(user=request.user)
    return render(request, "result-processting.html", {"current_user":current_user, "results":results})

def decleared(request):
    current_user = Staff.objects.get(user=request.user)
    report_card = ReportCard.objects.all()
    context = {
        'current_user':current_user,
        'reports': report_card,
    }
    return render(request, "decleared-result.html", context)

def declear_result(request, id):
    result = Result.objects.get(id=id)
    student = Student.objects.get(id=result.check_id)
    student_t = Result.objects.filter(check_id=result.check_id)
    stu_total = sum([t.total_marks for t in student_t])
    current_user = Staff.objects.get(user=request.user)

    context = {
        "result": result,
        "stu":student,
        "current_user":current_user,
    }
    if request.method == 'POST':
        if request.FILES.get("sign") != None:
            sign = request.FILES.get("sign")
            comment = request.POST["comment"]
            check_id = result.check_id
            staff_username = current_user.user.username
            staff_fullname = current_user.staff_fullname
            staff_role = current_user.role
            term = result.term
            if ReportCard.objects.filter(stu_id=result.stu_id).exists():
                messages.error(request, f"Report Card for {student.stu_fullname} already exist!!")
                return render(request, "declear-result.html", context)
            else:
                new_report = ReportCard.objects.create(
                    check_id=student.id,stu_id=student, term=term, staff_username=staff_username, staff_fullname=staff_fullname, staff_role=staff_role,
                    date_registered=date, examiner_comment=comment, year=year, examiner_sign=sign, overAll_marks=stu_total 
                )
                new_report.save()
                get_posi = ReportCard.objects.get(check_id=result.check_id)
                # if get_posi.overAll_marks >= 200:
                #     get_posi.position = 'Upper Credit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 100:
                #     get_posi.position = 'Merit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 50:
                #     get_posi.position = 'Credit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 40:
                #     get_posi.position = 'Pass'
                #     get_posi.save()
                # else:
                #     get_posi.position = 'Failed'
                #     get_posi.save()
                student.overAll_marks = stu_total
                student.save()
                students = Student.objects.filter(class_name=result.class_name)
                students = students.order_by('-overAll_marks')
                current_position = 1  # Initialize the position as 1 for the first student
                previous_student = None  # Initialize the previous student
                positions = []  # Create a list to store the positions

                for stu in students:
                    if previous_student is not None and stu.overAll_marks < previous_student.overAll_marks:
                        current_position += 1  # Increment the position when the score changes
                    positions.append((current_position, stu))
                    previous_student = stu

                if positions[0]:
                    get_posi.position = '1th'
                    get_posi.save()
                elif positions[1]:
                    get_posi.position = '2nd'
                    get_posi.save()
                elif positions[2]:
                    get_posi.position = '3rd'
                    get_posi.save()
                else:
                    get_posi.position = 'Pass'
                    get_posi.save()
                messages.success(request, "Report Generated Successfully...")
                return redirect("/result")
        
        if request.FILES.get("sign") == None:
            sign = "No signature Uploded"
            comment = request.POST["comment"]
            check_id = result.check_id
            staff_username = current_user.user.username
            staff_fullname = current_user.staff_fullname
            staff_role = current_user.role
            term = result.term
            if ReportCard.objects.filter(stu_id=result.stu_id).exists():
                messages.error(request, f"Report Card for {student.stu_fullname} already exist!!")
                return render(request, "declear-result.html", context)
            else:
                new_report = ReportCard.objects.create(
                    check_id=student.id,stu_id=student, term=term, staff_username=staff_username, staff_fullname=staff_fullname, staff_role=staff_role,
                    date_registered=date, examiner_comment=comment, year=year, examiner_sign=sign, overAll_marks=stu_total 
                )
                new_report.save()
                get_posi = ReportCard.objects.get(check_id=result.check_id)
                # if get_posi.overAll_marks >= 200:
                #     get_posi.position = 'Upper Credit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 100:
                #     get_posi.position = 'Merit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 50:
                #     get_posi.position = 'Credit'
                #     get_posi.save()
                # elif get_posi.overAll_marks >= 40:
                #     get_posi.position = 'Pass'
                #     get_posi.save()
                # else:
                #     get_posi.position = 'Failed'
                #     get_posi.save()
                student.overAll_marks = stu_total
                student.save()
                students = Student.objects.filter(class_name=result.class_name)
                students = students.order_by('-overAll_marks')
                current_position = 1  # Initialize the position as 1 for the first student
                previous_student = None  # Initialize the previous student
                positions = []  # Create a list to store the positions

                for stu in students:
                    if previous_student is not None and stu.overAll_marks < previous_student.overAll_marks:
                        current_position += 1  # Increment the position when the score changes
                    positions.append((current_position, stu))
                    previous_student = stu
                third_position = positions[1]  # 0-based index
                third_student = third_position[1]
                if positions[0]:
                    get_posi.position = '1th'
                    get_posi.save()
                elif positions[1]:
                    get_posi.position = '2nd'
                    get_posi.save()
                elif positions[2]:
                    get_posi.position = '3rd'
                    get_posi.save()
                else:
                    get_posi.position = 'Pass'
                    get_posi.save()
                messages.success(request, "Report Generated Successfully...")
                return redirect("/result")
    return render(request, "declear-result.html", context)

@login_required(login_url='login')
def add_result(request):
    current_user = Staff.objects.get(user=request.user)
    if request.method == 'POST':
        stu_id = request.POST['stu_id']
        subj_name = request.POST['subj_name']
        assessment = request.POST['assessment']
        marks = request.POST['marks']
        class_name = request.POST['class_name']
        term = request.POST['term']
        staff_username = current_user.user.username
        staff_fullname = current_user.staff_fullname
        staff_role = current_user.role
        check_id = Student.objects.get(id=stu_id)

        if Result.objects.filter(stu_id=stu_id).exists() and Result.objects.filter(subj_name=subj_name).exists():
            error = 'This assessment already exists!!'
            response_data = {'success': False, 'message': error}
            return JsonResponse(response_data)
        elif assessment == "1st C.A":
            new_assessment = Result.objects.create(
                stu_id=check_id, subj_name=subj_name,check_id=check_id.id, first_ca=marks,
                class_name=class_name, term=term, staff_username=staff_username, staff_fullname=staff_fullname,
                staff_role=staff_role, date_registered=date
            )
            new_assessment.save()
            stu_result_updates = Result.objects.filter(stu_id=stu_id)
            for stu_result_update in stu_result_updates:
                stu_result_update.total_marks = int(stu_result_update.first_ca) + int(stu_result_update.second_ca) + int(stu_result_update.third_ca) + int(stu_result_update.exam)
                stu_result_update.save()
                if int(stu_result_update.total_marks) >= 100:
                    stu_result_update.grade = "A"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 60:
                    stu_result_update.grade = "B"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 30:
                    stu_result_update.grade = "C"
                    stu_result_update.save()
                else:
                    stu_result_update.grade = "F"
                    stu_result_update.save()
            success = "Assessment added successfully..."
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
        elif assessment == "2nd C.A":
            new_assessment = Result.objects.create(
                stu_id=check_id, subj_name=subj_name,check_id=check_id.id, second_ca=marks,
                class_name=class_name, term=term, staff_username=staff_username, staff_fullname=staff_fullname,
                staff_role=staff_role
            )
            new_assessment.save()
            stu_result_updates = Result.objects.filter(stu_id=stu_id)
            for stu_result_update in stu_result_updates:
                stu_result_update.total_marks = int(stu_result_update.first_ca) + int(stu_result_update.second_ca) + int(stu_result_update.third_ca) + int(stu_result_update.exam)
                stu_result_update.save()
                if int(stu_result_update.total_marks) >= 100:
                    stu_result_update.grade = "A"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 60:
                    stu_result_update.grade = "B"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 30:
                    stu_result_update.grade = "C"
                    stu_result_update.save()
                else:
                    stu_result_update.grade = "F"
                    stu_result_update.save()
                student_t = Result.objects.filter(check_id=stu_id)
            success = "Assessment added successfully..."
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
        
        elif assessment == "3rd C.A":
            new_assessment = Result.objects.create(
                stu_id=check_id, subj_name=subj_name,check_id=check_id.id, third_ca=marks,
                class_name=class_name, term=term, staff_username=staff_username, staff_fullname=staff_fullname,
                staff_role=staff_role
            )
            new_assessment.save()
            stu_result_updates = Result.objects.filter(stu_id=stu_id)
            for stu_result_update in stu_result_updates:
                stu_result_update.total_marks = int(stu_result_update.first_ca) + int(stu_result_update.second_ca) + int(stu_result_update.third_ca) + int(stu_result_update.exam)
                stu_result_update.save()
                if int(stu_result_update.total_marks) >= 100:
                    stu_result_update.grade = "A"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 60:
                    stu_result_update.grade = "B"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 30:
                    stu_result_update.grade = "C"
                    stu_result_update.save()
                else:
                    stu_result_update.grade = "F"
                    stu_result_update.save()
            success = "Assessment added successfully..."
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)
        
        elif assessment == "Exam":
            new_assessment = Result.objects.create(
                stu_id=check_id, subj_name=subj_name,check_id=check_id.id, exam=marks,
                class_name=class_name, term=term, staff_username=staff_username, staff_fullname=staff_fullname,
                staff_role=staff_role
            )
            new_assessment.save()
            stu_result_updates = Result.objects.filter(stu_id=stu_id)
            for stu_result_update in stu_result_updates:
                stu_result_update.total_marks = int(stu_result_update.first_ca) + int(stu_result_update.second_ca) + int(stu_result_update.third_ca) + int(stu_result_update.exam)
                stu_result_update.save()
                if int(stu_result_update.total_marks) >= 100:
                    stu_result_update.grade = "A"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 60:
                    stu_result_update.grade = "B"
                    stu_result_update.save()
                elif int(stu_result_update.total_marks) >= 30:
                    stu_result_update.grade = "C"
                    stu_result_update.save()
                else:
                    stu_result_update.grade = "F"
                    stu_result_update.save()
            success = "Assessment added successfully..."
            response_data = {'success': True, 'message': success}
            return JsonResponse(response_data)

        

@login_required(login_url='login')
def get_student_info(request, student_name):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        stu_info = Student.objects.filter(stu_fullname=student_name).values('id', 'class_name', 'term', 'stu_id')
        return JsonResponse({'data': list(stu_info)})
    return HttpResponse('Wrong request')

@login_required(login_url='login')
def get_term(request, class_name):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        terms = StudentClasses.objects.filter(class_name=class_name).values('id', 'term')
        return JsonResponse({'data': list(terms)})
    return HttpResponse('Wrong request')

@login_required(login_url='login')
def get_staff_data(request, id):
    staff = Staff.objects.get(id_user=id)
    subjects = Subject.objects.all()
    current_user = Staff.objects.get(user=request.user)
    return render(request, "update-staff.html", {"staff": staff, "subjects": subjects, "current_user": current_user})

@login_required(login_url='login')
def get_result(request, id):
    result = Result.objects.get(id=id)
    student = Student.objects.get(id=result.check_id)
    current_user = Staff.objects.get(user=request.user)
    return render(request, "update-result.html", {"result": result, "current_user":current_user, "stu":student})

def update_result(request, id):
    current_user = Staff.objects.get(user=request.user)
    result = Result.objects.get(id=id)
    if request.method == 'POST':
        assessment = request.POST['assessment']
        marks = request.POST['marks']

        if assessment == "1st C.A":
            result.first_ca = marks
            result.last_update = date
            result.total_marks = int(result.first_ca) + int(result.second_ca) + int(result.third_ca) + int(result.exam)
            result.save()
            if int(result.total_marks) >= 100:
                result.grade = "A"
                result.save()
            elif int(result.total_marks) >= 60:
                result.grade = "B"
                result.save()
            elif int(result.total_marks) >= 30:
                result.grade = "C"
                result.save()
            else:
                result.grade = "F"
            messages.success(request, "Assessment Updated successfully...")
            return redirect("/result")
    
        elif assessment == "2nd C.A":
            result.second_ca = marks
            result.last_update = date
            result.total_marks = int(result.first_ca) + int(result.second_ca) + int(result.third_ca) + int(result.exam)
            result.save()
            if int(result.total_marks) >= 100:
                result.grade = "A"
                result.save()
            elif int(result.total_marks) >= 60:
                result.grade = "B"
                result.save()
            elif int(result.total_marks) >= 30:
                result.grade = "C"
                result.save()
            else:
                result.grade = "F"
            messages.success(request, "Assessment Updated successfully...")
            return redirect("/result")
        
        elif assessment == "3rd C.A":
            result.third_ca = marks
            result.last_update = date
            result.total_marks = int(result.first_ca) + int(result.second_ca) + int(result.third_ca) + int(result.exam)
            result.save()
            if int(result.total_marks) >= 100:
                result.grade = "A"
                result.save()
            elif int(result.total_marks) >= 60:
                result.grade = "B"
                result.save()
            elif int(result.total_marks) >= 30:
                result.grade = "C"
                result.save()
            else:
                result.grade = "F"
            messages.success(request, "Assessment Updated successfully...")
            return redirect("/result")
        
        elif assessment == "Exam":
            result.exam = marks
            result.last_update = date
            result.total_marks = int(result.first_ca) + int(result.second_ca) + int(result.third_ca) + int(result.exam)
            result.save()
            if int(result.total_marks) >= 100:
                result.grade = "A"
                result.save()
            elif int(result.total_marks) >= 60:
                result.grade = "B"
                result.save()
            elif int(result.total_marks) >= 30:
                result.grade = "C"
                result.save()
            else:
                result.grade = "F"
        messages.success(request, "Assessment Updated successfully...")
        return redirect("/result")

# Update section
@login_required(login_url='login')
def update_staff(request, id):
    if request.method == "POST":
        staff = Staff.objects.get(id_user=id)
        staff_log = User.objects.get(id=id)

        if request.FILES.get("profileimg") == None:
            staff_photo = staff.staff_photo
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            dob = request.POST['dob']
            staff_phone = request.POST['staff_phone']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            gender = request.POST['gender']
            role = request.POST['role']
            address1 = request.POST['address1']
            subjects = request.POST['subj']
            #  next of kin
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            address2 = request.POST['address2']
            email2 = request.POST['email2']
            if password:
                if cpassword == password:
                    staff_log.set_password(password)
                    staff_log.save()
                    messages.success(request, "Password Updated Successful..")
                    return redirect("staff")
                else:
                    messages.error(request, "Password and Confirm Password missed match!!")
                    return redirect("/get-staff-data/"+str(id))
            else:
                staff.staff_photo = staff_photo
                staff.f_name = fname
                staff.m_name = mname
                staff.l_name = lname
                staff.dob = dob
                staff.staff_phone = staff_phone
                staff_log.email = email
                staff_log.username = username
                staff.gender = gender
                staff.role = role
                staff.staff_address = address1
                staff.n_fullname = full_name 
                staff.n_phone_number = p_number
                staff.n_address = address2
                staff.n_email = email2
                staff.subjects = subjects
                staff.staff_fullname = f"{fname} {lname} {mname}"
                staff.last_update = date
                staff.save()
                staff_log.save()
                messages.success(request, "Staff Updated Successfully...")
                return redirect("staff")
            
        if request.FILES.get("profileimg") != None:
            staff_photo = request.FILES.get("profileimg")
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            dob = request.POST['dob']
            staff_phone = request.POST['staff_phone']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            gender = request.POST['gender']
            role = request.POST['role']
            address1 = request.POST['address1']
            subjects = request.POST['subj']
            #  next of kin
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            address2 = request.POST['address2']
            email2 = request.POST['email2']
            if password:
                if cpassword == password:
                    staff_log.set_password(password)
                    staff_log.save()
                    messages.success(request, "Password Updated Successful..")
                    return redirect("staff")
                else:
                    messages.error(request, "Password and Confirm Password missed match!!")
                    return redirect("/get-staff-data/"+str(id))
            else:
                staff.staff_photo = staff_photo
                staff.f_name = fname
                staff.m_name = mname
                staff.l_name = lname
                staff.dob = dob
                staff.staff_phone = staff_phone
                staff_log.email = email
                staff_log.username = username
                staff.gender = gender
                staff.role = role
                staff.staff_address = address1
                staff.n_fullname = full_name 
                staff.n_phone_number = p_number
                staff.n_address = address2
                staff.n_email = email2
                staff.subjects = subjects
                staff.staff_fullname = f"{fname} {lname} {mname}"
                staff.last_update = date
                staff.save()
                messages.success(request, "Staff Updated Successfully...")
                return redirect("staff")

@login_required(login_url='login')
def manage_acc(request):
    staff = Staff.objects.get(user=request.user)
    subjects = Subject.objects.all()
    current_user = Staff.objects.get(user=request.user)
    return render(request, "manage_acc.html", {"staff": staff, "subjects":subjects, "current_user":current_user})
            
@login_required(login_url='login')
def update_acc(request):
    if request.method == "POST":
        staff = Staff.objects.get(user=request.user)
        staff_log = User.objects.get(username=request.user)

        if request.FILES.get("profileimg") == None:
            staff_photo = staff.staff_photo
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            dob = request.POST['dob']
            staff_phone = request.POST['staff_phone']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            gender = request.POST['gender']
            role = request.POST['role']
            address1 = request.POST['address1']
            subjects = request.POST['subj']
            #  next of kin
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            address2 = request.POST['address2']
            email2 = request.POST['email2']
            if password:
                if cpassword == password:
                    staff_log.set_password(password)
                    staff_log.save()
                    messages.success(request, "Password Updated Successful..")
                    return redirect("manage-acc")
                else:
                    messages.error(request, "Password and Confirm Password missed match!!")
                    return redirect("manage-acc")
            else:
                staff.staff_photo = staff_photo
                staff.f_name = fname
                staff.m_name = mname
                staff.l_name = lname
                staff.dob = dob
                staff.staff_phone = staff_phone
                staff_log.email = email
                staff_log.username = username
                staff.gender = gender
                staff.role = role
                staff.staff_address = address1
                staff.n_fullname = full_name 
                staff.n_phone_number = p_number
                staff.n_address = address2
                staff.n_email = email2
                staff.subjects = subjects
                staff.staff_fullname = f"{fname} {lname} {mname}"
                staff.last_update = date
                staff.save()
                staff_log.save()
                messages.success(request, "Profile Updated Successfully...")
                return redirect("manage-acc")
            
        if request.FILES.get("profileimg") != None:
            staff_photo = request.FILES.get("profileimg")
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            dob = request.POST['dob']
            staff_phone = request.POST['staff_phone']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            gender = request.POST['gender']
            role = request.POST['role']
            address1 = request.POST['address1']
            subjects = request.POST['subj']
            #  next of kin
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            address2 = request.POST['address2']
            email2 = request.POST['email2']
            if password:
                if cpassword == password:
                    staff_log.set_password(password)
                    staff_log.save()
                    messages.success(request, "Password Updated Successful..")
                    return redirect("manage-acc")
                else:
                    messages.error(request, "Password and Confirm Password missed match!!")
                    return redirect("manage-acc")
            else:
                staff.staff_photo = staff_photo
                staff.f_name = fname
                staff.m_name = mname
                staff.l_name = lname
                staff.dob = dob
                staff.staff_phone = staff_phone
                staff_log.email = email
                staff_log.username = username
                staff.gender = gender
                staff.role = role
                staff.staff_address = address1
                staff.n_fullname = full_name 
                staff.n_phone_number = p_number
                staff.n_address = address2
                staff.n_email = email2
                staff.subjects = subjects
                staff.staff_fullname = f"{fname} {lname} {mname}"
                staff.last_update = date
                staff.save()
                messages.success(request, "Profile Updated Successfully...")
                return redirect("manage-acc")

@login_required(login_url='login')          
def get_class(request, id):
    class_id = StudentClasses.objects.get(id=id)
    teachers = Staff.objects.filter(role='teacher')
    subjects = Subject.objects.all()
    current_user = Staff.objects.get(user=request.user)
    context = {
        'class': class_id, 
        'teachers': teachers,
        "subjects":subjects,
        "current_user": current_user
    }
    return render(request, 'update-class.html', context)

@login_required(login_url='login')
def update_class(request, id):
    class_id = StudentClasses.objects.get(id=id)
    student = Student.objects.filter(class_name=class_id.class_name)

    for stu in student:

        if request.method == 'POST':
            class_name = request.POST['class_name']
            term = request.POST['term']

            class_id.class_name = class_name
            class_id.term = term
            class_id.last_update = date
            class_id.save()

            stu.class_name = class_name
            stu.term = term
            stu.save()
            messages.success(request, 'Class updated successfully ....')
            return redirect('/student_class')

@login_required(login_url='login')
def get_subject(request, id):
    subject = Subject.objects.get(id=id)
    current_user = Staff.objects.get(user=request.user)
    return render(request, "update-subject.html", {'subject':subject, "current_user":current_user})

@login_required(login_url='login')
def update_subject(request, id):
    subject = Subject.objects.get(id=id)
    if request.method == 'POST':
        subj_name = request.POST['subj_name']
        subj_descript = request.POST['subj_descript']

        subject.subject_name = subj_name
        subject.description = subj_descript
        subject.last_update = date
        subject.save()
        messages.success(request, 'Subject updated successfully...')
        return redirect('/subject')

@login_required(login_url='login')
def get_student(request, id):
    student = Student.objects.get(id=id)
    current_user = Staff.objects.get(user=request.user)
    return render(request, "update-student.html", {"student": student, "current_user": current_user})

@login_required(login_url='login')
def update_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)

        if request.FILES.get("profileimg") == None:
            student_photo = request.FILES.get("profileimg")
            fname = request.POST['fname']
            lname = request.POST['lname']
            mname = request.POST['mname']
            dob = request.POST['dob']
            gender = request.POST['gender']
            stu_address = request.POST['stu_address']
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            g_address = request.POST['g_address']
            relationship = request.POST['relationship']
            email = request.POST['email']
            stu_fullname = f"{fname} {lname}-{mname}"

            student.student_photo = student_photo
            student.f_name = fname
            student.m_name = mname
            student.l_name = lname
            student.dob = dob
            student.gender = gender
            student.stu_address = stu_address
            student.g_fullname = full_name
            student.g_phone_number = p_number
            student.g_address = g_address
            student.relationship = relationship
            student.email = email
            student.stu_fullname = stu_fullname
            student.save()
            messages.success(request, "Student Updated Successfully..")
            return redirect("student")
            
        if request.FILES.get("profileimg") != None:
            student_photo = request.FILES.get("profileimg")
            fname = request.POST['fname']
            lname = request.POST['lname']
            mname = request.POST['mname']
            dob = request.POST['dob']
            gender = request.POST['gender']
            stu_address = request.POST['stu_address']
            full_name = request.POST['full_name']
            p_number = request.POST['p_number']
            g_address = request.POST['g_address']
            relationship = request.POST['relationship']
            email = request.POST['email']
            stu_fullname = f"{fname} {lname}-{mname}"
            
            student.student_photo = student_photo
            student.f_name = fname
            student.m_name = mname
            student.l_name = lname
            student.dob = dob
            student.gender = gender
            student.stu_address = stu_address
            student.g_fullname = full_name
            student.g_phone_number = p_number
            student.g_address = g_address
            student.relationship = relationship
            student.email = email
            student.stu_fullname = stu_fullname
            student.save()
            messages.success(request, "Student Updated Successfully..")
            return redirect("student")

# Delete Section
@login_required(login_url='login')
def deleteStaff(request, id):
    staff = User.objects.get(id=id)
    staff.delete()
    return JsonResponse({'success': True, 'message': 'Staff Deleted Successful...'})

def deleteClass(request, id):
    class_id = StudentClasses.objects.get(id=id)
    class_id.delete()
    return JsonResponse({'success': True, 'message': 'Class Deleted Successful...'})

def deleteSubject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return JsonResponse({'success': True, 'message': 'Subject Deleted Successful...'})

def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return JsonResponse({'success': True, 'message': 'Student Deleted Successful...'})

def deleteResult(request, id):
    result = Result.objects.get(id=id)
    result.delete()
    return JsonResponse({'success': True, 'message': 'Result Deleted Successful...'})

def deleteReport(request, id):
    report = ReportCard.objects.get(check_id=id)
    report.delete()
    return JsonResponse({'success': True, 'message': 'Report Deleted Successful...'})

@login_required(login_url='login')
def full_details(request, id):
    staff = Staff.objects.get(id_user=id)
    context = {
        'staff': staff
    }
    return render(request, "full-details.html", context)

@login_required(login_url='login')
def full_details_class(request, id):
    class_id = StudentClasses.objects.get(id=id)
    students = Student.objects.filter(class_name=class_id.class_name)
    context = {
        'class': class_id,
        'students': students
    }
    return render(request, "full-details.html", context)

@login_required(login_url='login')
def full_details_subject(request, id):
    subject = Subject.objects.get(id=id)
    context = {
        'subject': subject
    }
    return render(request, "full-details.html", context)

@login_required(login_url='login')
def full_details_student(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, "full-details.html", context)

@login_required(login_url='login')
def full_details_result(request, id):
    result = Result.objects.get(id=id)
    context = {
        'result': result,
    }
    return render(request, "full-details.html", context)

# authentication
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if len(username) < 3:
            return JsonResponse({'success': False, 'message': 'Username is required please.'})
        elif len(password) < 3:
            return JsonResponse({'success': False, 'message': 'Password is required please.'})
        elif user is not None:
            auth.login(request, user)
            return JsonResponse({'success': True, 'message': 'Login Successful...'})
        else:
            return JsonResponse({'success': False, 'message': 'invalid Credentials.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')