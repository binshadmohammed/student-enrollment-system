from django.shortcuts import render
from . models import *
from django.core.files.storage import FileSystemStorage


# Create your views here
def studentsreg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        relegion=request.POST.get('relegion')
        adhar=request.FILES['adhar']
        a=FileSystemStorage()
        aa=a.save(adhar.name,adhar)
        
        photo=request.FILES['photo']
        p=FileSystemStorage()
        pp=p.save(photo.name,photo)
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        guardianname=request.POST.get('guardianname')
        guardianmobile=request.POST.get('guardianmobile')
        
        sslccertificate=request.FILES['sslccertificate']
        s=FileSystemStorage()
        ss=s.save(sslccertificate.name,sslccertificate)
        sslcpassoutyear=request.POST.get('sslcpassoutyear')
        schoolname=request.POST.get('schoolname')
        schoollocation=request.POST.get('schoollocation')
       
        hssname=request.POST.get('hssname') 
        hsscertificate=request.FILES['hsscertificate']
        h=FileSystemStorage()
        hh=h.save(hsscertificate.name,hsscertificate)
        hsspersentage=request.POST.get('hsspersentage')
        hsspassoutyear=request.POST.get('hsspassoutyear')
        reg=student_register(name=name,email=email,mobile=mobile,dob=dob,gender=gender,relegion=relegion,
                             adhar=adhar,photo=photo,address=address,state=state,city=city,pincode=pincode,
                             guardianname=guardianname,guardianmobile=guardianmobile,
                             sslccertificate=sslccertificate,sslcpassoutyear=sslcpassoutyear,schoolname=schoolname,
                             schoollocation=schoollocation,hss_name=hssname,hsscertificate=hsscertificate,
                             hsspersentage=hsspersentage,hsspassoutyear=hsspassoutyear)
        reg.save()

        
    return render(request,'studentregister.html')