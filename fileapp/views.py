from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedFile
from django.shortcuts import render, get_object_or_404
from .models import UploadedFile
from .models import ContactQuery
from django.contrib import messages



def home(request):
    return render(request, "fileapp/home.html")

def about(request):
    return render(request, "fileapp/about.html")

def services(request):
    return render(request, "fileapp/services.html")

def tdls(request):
    return render(request, "fileapp/tdls.html")

def file_detail(request, pk):
    file_obj = get_object_or_404(UploadedFile, pk=pk)
    return render(request, "fileapp/file_detail.html", {"file": file_obj})


def tdls(request):
    # Fetch all files with category "TDL"
    tdl_files = UploadedFile.objects.filter(category="TDL").order_by('-uploaded_at')
    return render(request, "fileapp/tdls.html", {"tdl_files": tdl_files})




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ContactQuery.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, "Your query has been submitted successfully!")
        return redirect('contact')

    return render(request, 'fileapp/contact.html')
