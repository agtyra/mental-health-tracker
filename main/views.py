from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306172086',
        'name': 'Kezia Salsalina Agtyra Sebayang',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)

# Create your views here.
