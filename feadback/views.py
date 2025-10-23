from django.shortcuts import render
from .forms import feadbackform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def fead(request):
    if request.method=='POST':
        form=feadbackform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'feadtick.html')
    else:
        form=feadbackform()
    return render(request,'feadback.html',{'form':form})

  