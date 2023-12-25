from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    staff_id = models.CharField(max_length=100, blank=True)
    f_name = models.CharField(max_length=100, blank=True)
    m_name = models.CharField(max_length=100, blank=True)
    l_name = models.CharField(max_length=100, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=30, blank=True)
    staff_address = models.TextField(max_length=200, blank=True)
    staff_phone = models.CharField(max_length=20, blank=True)
    staff_photo = models.ImageField(upload_to='staff_profile', default='profile.png')
    n_fullname = models.CharField(max_length=100, blank=True)
    n_phone_number = models.CharField(max_length=100, blank=True)
    n_email = models.CharField(max_length=100, blank=True)
    n_address = models.TextField(max_length=200, blank=True)
    subjects = models.TextField(max_length=10000, blank=True)
    staff_fullname = models.CharField(max_length=10000, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    last_update = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Staff Name {self.f_name} {self.m_name} {self.l_name}"


class StudentClasses(models.Model):
    class_name = models.CharField(max_length=100, blank=True)
    subjects = models.TextField(max_length=20000, blank=True)
    teachers = models.TextField(max_length=50000, blank=True)
    teachers_usernames = models.TextField(max_length=50000, blank=True)
    term = models.CharField(max_length=100, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    last_update = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Class Name - {self.class_name}"
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=20000, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    last_update = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.subject_name}"

class Student(models.Model):
    stu_fullname = models.CharField(max_length=100, blank=True)
    stu_uuid = models.CharField(max_length=1000, blank=True)
    stu_id = models.CharField(max_length=100, blank=True)
    f_name = models.CharField(max_length=100, blank=True)
    l_name = models.CharField(max_length=100, blank=True)
    m_name = models.CharField(max_length=100, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    term = models.CharField(max_length=100, blank=True)
    stu_address = models.TextField(max_length=50000, blank=True)
    # guardian section
    g_fullname = models.CharField(max_length=100, blank=True)
    g_phone_number = models.CharField(max_length=100, blank=True)
    g_address = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    last_update = models.CharField(max_length=100, blank=True)
    student_photo = models.ImageField(upload_to='student_profile', default='profile.png')
    overAll_marks = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.stu_id
    
class Result(models.Model):
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_id = models.CharField(max_length=100, blank=True)
    subj_name = models.CharField(max_length=100, blank=True)
    first_ca = models.IntegerField(null=True, blank=True, default=0)
    second_ca = models.IntegerField(null=True, blank=True, default=0)
    third_ca = models.IntegerField(null=True, blank=True, default=0)
    exam = models.IntegerField(null=True, blank=True, default=0)
    total_marks = models.IntegerField(null=True, blank=True, default=0)
    grade = models.CharField(max_length=100, blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    term = models.CharField(max_length=100, blank=True)
    staff_username = models.CharField(max_length=100, blank=True)
    staff_fullname = models.CharField(max_length=100, blank=True)
    staff_role = models.CharField(max_length=100, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    last_update = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Assessment for {self.stu_id}"
    
class ReportCard(models.Model):
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_id = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    term = models.CharField(max_length=100, blank=True)
    staff_username = models.CharField(max_length=100, blank=True)
    staff_fullname = models.CharField(max_length=100, blank=True)
    staff_role = models.CharField(max_length=100, blank=True)
    date_registered = models.CharField(max_length=100, blank=True)
    examiner_comment = models.TextField(max_length=1000000000, blank=True)
    year = models.CharField(max_length=100, blank=True)
    examiner_sign = models.ImageField(upload_to='signatures', blank=True)
    overAll_marks = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"Staff Role - {self.staff_role}"