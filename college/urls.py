from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('student_application/', views.student_application, name='student_application'),
    path('save_application/', views.save_application, name='save_application'),
    path('student_reg/', views.student_reg, name='student_reg'),
    path('staff_reg/', views.staff_reg, name='staff_reg'),
    path('save_staff_reg/', views.save_staff_reg, name='save_staff_reg'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('staff_log_status/', views.staff_log_status, name='staff_log_status'),
    path('student_log_status/', views.student_log_status, name='student_log_status'),
    path('save_std_reg/', views.save_std_reg, name='save_std_reg'),
    path('std_detail/', views.std_detail, name='std_detail'),
    path('staff_detail/', views.staff_detail, name='staff_detail'),
    path('student_logout/', views.student_logout, name='student_logout'),
    path('staff_logout/', views.staff_login, name='staff_logout'),
    path('student_list/', views.student_list, name='student_list'),
    path('staff_list/', views.staff_list, name='staff_list'),
    # path('dep_details/', views.dep_details, name='dep_details'),
    path('staff_ece/', views.staff_ece, name='staff_ece'),
    path('staff_cse/', views.staff_cse, name='staff_cse'),
    path('staff_mec/', views.staff_mec, name='staff_mec'),
    path('staff_eee/', views.staff_eee, name='staff_eee'),
    path('staff_it/', views.staff_it, name='staff_it'),
    path('std_ece/',views.std_ece,name='std_ece'),
    path('std_eee/',views.std_eee,name='std_eee'),
    path('std_cse/',views.std_cse,name='std_cse'),
    path('std_it/',views.std_it,name='std_it'),
    path('std_mec/',views.std_mec,name='std_mec'),
    path('std_dep/',views.std_dep,name='std_dep'),

]
