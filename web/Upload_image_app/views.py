from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import filepath
from .forms import ImageForm

# Create your views here.
def Image_upload(request):
        if request.method == "POST":
            myfile = request.FILES['myfile']
            print(myfile)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
            Path = filepath(path=uploaded_file_url)
            Path.save()
            return render(request,'Upload_image/index.html')

        else:
            return render(request,'Upload_image/index.html')

def View_uploads(request):
            Path=filepath.objects.all()
            return render(request,'Upload_image/upload_view.html',{"path":Path})






def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'Upload_image/uploadimage.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()    
        return render(request, 'Upload_image/uploadimage.html', {'form': form})