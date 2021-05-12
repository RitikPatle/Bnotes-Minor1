from .models import *
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def notes(request):
   
    subs=Notes.objects.all()
 
    return render(request,'notes.html',{'subs':subs})

def cs(request):
    obj1=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","1"])
    obj2=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","2"])
    obj3=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","3"])
    obj4=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","4"])
    obj5=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","5"])
    obj6=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","6"])
    obj7=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","7"])
    obj8=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["cs","8"])

    return render(request,'subn.html',{'streamname':'Computer Science Engineering','obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5,'obj6':obj6,'obj7':obj7,'obj8':obj8})

def me(request):
    obj1=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","1"])
    obj2=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","2"])
    obj3=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","3"])
    obj4=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","4"])
    obj5=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","5"])
    obj6=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","6"])
    obj7=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","7"])
    obj8=Sub.objects.raw('select * from bnotes_sub where stream=%s and sem=%s',["me","8"])

    return render(request,'subn.html',{'streamname':'Mechanical Engineering','obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4,'obj5':obj5,'obj6':obj6,'obj7':obj7,'obj8':obj8})

def papers(request):

    psubs=Papers.objects.all()

    return render(request,'papers.html',{'psubs':psubs})

def pcs(request):
    objp1=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","1"])
    objp2=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","2"])
    objp3=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","3"])
    objp4=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","4"])
    objp5=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","5"])
    objp6=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","6"])
    objp7=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","7"])
    objp8=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["cs","8"])

    return render(request,'subp.html',{'streamname':'Computer Science Engineering','objp1':objp1,'objp2':objp2,'objp3':objp3,'objp4':objp4,'objp5':objp5,'objp6':objp6,'objp7':objp7,'objp8':objp8})

def pme(request):
    objp1=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","1"])
    objp2=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","2"])
    objp3=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","3"])
    objp4=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","4"])
    objp5=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","5"])
    objp6=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","6"])
    objp7=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","7"])
    objp8=Pub.objects.raw('select * from bnotes_pub where stream=%s and sem=%s',["me","8"])

    return render(request,'subp.html',{'streamname':'Mechanical Engineering','objp1':objp1,'objp2':objp2,'objp3':objp3,'objp4':objp4,'objp5':objp5,'objp6':objp6,'objp7':objp7,'objp8':objp8})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'cu.html')

def feedback(request):
    if request.method == 'POST':
            post=Post()
            post.name=request.POST["name"]
            post.email=request.POST["email"]
            post.mobno=request.POST["mobno"]
            post.comments=request.POST["comments"]
            post.save()

    return redirect('contact')