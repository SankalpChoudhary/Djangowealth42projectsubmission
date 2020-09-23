from django.urls import path

from app.views import home_view,student_view,teacher_view

urlpatterns = [
	path('home/', home_view),
	path('std/', student_view),
	path('tch/', teacher_view)
]