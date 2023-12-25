from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('staff/', views.staff, name='staff'),
    path('student_class/', views.student_class, name='student_class'),
    path('subject/', views.subject, name='subject'),
    path('student/', views.student, name='student'),
    path('result/', views.result, name='result'),
    path('decleared/', views.decleared, name='decleared'),
    path('add_result/', views.add_result, name='add_result'),
    path('get_term/<str:class_name>/', views.get_term, name='get_term'),
    path('get-result/<int:id>/', views.get_result, name='get-result'),
    path('report-card/<int:id>/', views.report_card, name='report-card'),
    path('get_student_info/<str:student_name>/', views.get_student_info, name='get_student_info'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('get-staff-data/<int:id>', views.get_staff_data, name='get-staff-data'),
    path('manage-acc/', views.manage_acc, name='manage-acc'),
    path('get-class/<int:id>', views.get_class, name='get-class'),
    path('get-subject/<int:id>', views.get_subject, name='get-subject'),
    path('get-student/<int:id>', views.get_student, name='get-student'),
    path('declear-result/<int:id>', views.declear_result, name='declear-result'),
    path('full-details/<int:id>', views.full_details, name='full-details'),
    path('full-details-class/<int:id>', views.full_details_class, name='full-details-class'),
    path('full-details-subject/<int:id>', views.full_details_subject, name='full-details-subject'),
    path('full-details-student/<int:id>', views.full_details_student, name='full-details-student'),
    path('full-details-result/<int:id>', views.full_details_result, name='full-details-result'),

    # update
    path('update-staff/<int:id>', views.update_staff, name='update-staff'),
    path('update-acc/', views.update_acc, name='update-acc'),
    path('update-class/<int:id>', views.update_class, name='update-class'),
    path('update-subject/<int:id>', views.update_subject, name='update-subject'),
    path('update-student/<int:id>', views.update_student, name='update-student'),
    path('update-result/<int:id>', views.update_result, name='update-result'),

    # delete
    path('deleteStaff/<int:id>/', views.deleteStaff, name='deleteStaff'),
    path('deleteClass/<int:id>/', views.deleteClass, name='deleteClass'),
    path('deleteSubject/<int:id>/', views.deleteSubject, name='deleteSubject'),
    path('deleteStudent/<int:id>/', views.deleteStudent, name='deleteStudent'),
    path('deleteResult/<int:id>/', views.deleteResult, name='deleteResult'),
    path('deleteReport/<int:id>/', views.deleteReport, name='deleteReport'),
]