from django.shortcuts import render
from django.http import HttpResponse
import roman
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

def upload_excel(request):
    if request.method == "POST":
        excel_file = request.FILES["file"]
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            Student.objects.create(
                Name=row["Name"],
                Rollno=row["Rollno"],
                Year=row["Year"],
                Branch=row["Branch"],
                Semester=row["Semester"],
                Password=row["Password"],  
            )

        messages.success(request, "Student data uploaded successfully!")
        return redirect("upload_excel")

    return render(request, "upload_excel.html")
    

def upload_sub(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        try:
            df = pd.read_excel(file)  
            for _, row in df.iterrows():
                branch_name = row["Branch"]
                semester_number = row["Semester"]
                subject_name = row["Subject_Name"]
                subject_code = row["Subject_Code"]
                branch, _ = Branch.objects.get_or_create(name=branch_name)
                sem, _ = Sem.objects.get_or_create(branch=branch, semester=semester_number)
                Subject.objects.create(subject_name=subject_name, subject_code=subject_code, semester=sem)

            messages.success(request, "Subjects uploaded successfully!")
            return redirect("upload_sub") 

        except Exception as e:
            messages.error(request, f"Error uploading file: {e}")
            return render(request, "upload.html")

    return render(request, "upload.html")  


"""
def notification_view(request):
    form = NotificationDropdownForm()
    return render(request, "notifications.html", {"form": form})
"""


def notification_view(request):
    student_id = request.session.get("student_id")
    
    if not student_id:
        messages.error(request, "Please log in first.")
        return redirect("login")

    student = Student.objects.get(Rollno=student_id)
    form = NotificationDropdownForm()
    subjects = None
    selected_notification = None

    if request.method == "POST":
        form = NotificationDropdownForm(request.POST)
        if form.is_valid():
            selected_notification = form.cleaned_data["notification"]
            date=selected_notification.due_date.date()
            end_date=selected_notification.end_date.date()

            
            #print(f"Student Semester: {student.Semester}, Student Branch: {student.Branch}")
            #print(f"Notification Semester: {selected_notification.semester.semester}, Notification Branch: {selected_notification.semester.branch.name}")

            
            if student.Semester < selected_notification.semester:
                student = Student.objects.get(Rollno=student_id)
                messages.error(request, "You are not eligible for this notification.")
                return render(request, "notifications.html", {"form": form})
          

            
            if "revaluation" in selected_notification.notification.lower():
             subjects = Subject.objects.filter(
                 semester__semester=selected_notification.semester, 
                  semester__branch__name__iexact=student.Branch,                  
             subject_type="Theory",
             )
            else:
             subjects = Subject.objects.filter(
    semester__semester=selected_notification.semester, 
    semester__branch__name__iexact=student.Branch 
)
                               





        if "submit_payment" in request.POST:
            selected_notification = request.POST.get("selected_notification")
            selected_notification = Notifications.objects.get(notification=selected_notification)
            #selected_notification = Notifications.objects.get(notification=selected_notification.notification)
            #selected_notification=Notifications.objects.filter(notification=selected_notification)
            total_amount = request.POST.get("total_amount", "0")
            total_amount = float(total_amount) if total_amount else 0
            
            payment = Payment.objects.create(
                student=student,
                notification=selected_notification,
                amount_paid=total_amount,
                payment_status="Completed"
            )
            selected_subjects = request.POST.getlist("subjects")  
            subjects_add = Subject.objects.filter(id__in=selected_subjects)  
            payment.subjects.set(subjects_add)  

            #payment.subjects.set(Subject.objects.filter(subject_code=selected_subjects))

            messages.success(request, "Payment successful!")
            return redirect("notification_view")


            
            #print("Subjects Retrieved:", list(subjects.values()))
    semester_roman=roman.toRoman(student.Semester)        
    return render(request, "notifications.html", {
        "form": form,
        "subjects": subjects,
        "selected_notification": selected_notification,
       # "due_date":date
       #"end_date":end_date,
        "student": student,
        "semester_roman":semester_roman
    })

def dashboard_view(request):
        student_id = request.session.get("student_id")
    
        if not student_id:
            messages.error(request, "Please log in first.")
            return redirect("login")

        student = Student.objects.get(Rollno=student_id)
        return render(request,"dashboard.html",{"student":student})




def login(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(Rollno=rollno)
            stored_password = student.Password.strftime("%Y-%m-%d")

            if (
                stored_password == password
                and rollno == student.Rollno
            ):
                request.session["student_id"] = student.Rollno
                return redirect("notification_view")
            else:
                messages.error(request, "Invalid credentials")

        except Student.DoesNotExist:
            messages.error(request, "Student details not found")

    return render(request, "login2.html")



def logins(request):
    student_id = request.session.get("student_id")
    if not student_id:
        messages.error(request, "Please log in first")
        return redirect("login")

    student = Student.objects.get(Rollno=student_id)
    return render(request, "logins.html", {"student": student})


