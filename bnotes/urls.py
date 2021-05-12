from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('notes',views.notes,name="notes"),
    path('papers',views.papers,name="papers"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('cs',views.cs,name="cs"),
    path('me',views.me,name="me"),
    path('pcs',views.pcs,name="pcs"),
    path('pme',views.pme,name="pme"),
    path('feedback',views.feedback,name="feedback")
]
