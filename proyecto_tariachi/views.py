from django.shortcuts import render
 

# Create your views here.
 

    
def home(request):
    # title= 'hello world '
    return render(request,'home.html', {
        # 'form':UserCreationForm
    })
