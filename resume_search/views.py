from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from resume_parser import resumeparse
from pyresparser import ResumeParser
from django.conf import settings
from django.contrib import messages
import os
from django.db import IntegrityError
from .models import Resume


#directory to display the file from:/media/ scanned_resumes
# Create your views here.
def index(request):
    context={}
    if request.method == 'POST':
        uploaded_file=request.FILES['resumes']
        fsUploaded=FileSystemStorage()
        name=fsUploaded.save(name=uploaded_file.name,content=uploaded_file)
        #print(name)
        context['link']=fsUploaded.url(name)
        context['name']=name
        files = os.listdir("C:/Users/HP/Desktop/Ideate/Resume_Filterate-1/media/scanned_resumes/")
        fsResult=FileSystemStorage(location="C:/Users/HP/Desktop/Ideate/Resume_Filterate-1/media/scanned_resumes/")
        # context['list_files']=files
        print(*files, sep="\n")
        tempArr = []
        for f in files :
            fileObj = {}
            fileObj['fileURL'] = fsResult.url(f)
            fileObj['fileName'] = f
            print(fsResult.url(f),sep='\n')
            tempArr.append(fileObj)
            # context['scan']=fs.url(f)
            context['display']=f

        context['resumeListDetails'] = tempArr
    return render(request,'index.html',context)

def scanned_results(request):
    print("Python Program to print list the files in a directory.")
    Direc = input(r"Enter the path of the folder: ")
    print(f"Files in the directory: {Direc}")
    files = os.listdir(Direc)
    files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
    print(*files, sep="\n")
    return render(request, "index.html")

