from django.contrib import admin
from django.urls import path
from courses.views import course_list, course_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_list, name='index'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
