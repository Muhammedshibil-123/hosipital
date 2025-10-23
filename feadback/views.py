from django.shortcuts import render
from .forms import feadbackform

# Create your views here.
def fead(request):
    if request.method=='POST':
        form=feadbackform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'feadtick.html')
    else:
        form=feadbackform()
    return render(request,'feadback.html',{'form':form})

  