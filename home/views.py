from django.shortcuts import render

# Create your views here.
# render 找 home 資料夾底下的 index.html
def index(request):
    return render(request, 'home/index.html') 

# json demo
def json_demo(request):
    return render(request, 'home/json.html')


