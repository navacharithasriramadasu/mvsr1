from django.db import models
from django.core.validators import *

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Sem(models.Model):
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(8)])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch.name} - Semester {self.semester}"

#        return str(self.semester)



class Student(models.Model):
    Name=models.CharField(max_length=50)
    Rollno = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{2}-\d{3}-\d{3}$',
            )
        ]
    )
    Year=models.PositiveIntegerField(MaxValueValidator(4))
    Branch=models.CharField(max_length=30)
    Semester = models.PositiveIntegerField(validators=[MaxValueValidator(8)])
   # Semester=models.ForeignKey(Sem, on_delete=models.CASCADE)
    Password=models.DateField()
    def __str__(self):
        return f"{self.Name} ({self.Rollno})"
    


class Notifications(models.Model):
    notification = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True) 
    due_date = models.DateTimeField()
    end_date = models.DateTimeField()
    semester = models.IntegerField()  

    def __str__(self):
        return f"{self.notification} - Semester {self.semester} - {self.start_date.strftime('%Y-%m-%d')}"
    

class Subject(models.Model):
    subject_name=models.CharField(max_length=60)
    subject_code=models.CharField(max_length=10)
    semester = models.ForeignKey(Sem, on_delete=models.DO_NOTHING)
    subject_type = models.CharField(
        max_length=20,
        choices=[("Theory", "Theory"), ("Lab", "Lab")],
        default="Theory",
    )

    def __str__(self):
        return f"{self.subject_name} ({self.semester})"
    

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    notification = models.ForeignKey(Notifications, on_delete=models.DO_NOTHING)
    subjects = models.ManyToManyField(Subject)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed")],
        default="Pending"
    )
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.student.Name} for {self.notification.notification} - {self.payment_status}"
