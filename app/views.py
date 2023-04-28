from django.shortcuts import render

# Create your views here.
import datetime
def builtin_filters(request):
    t=datetime.datetime.now()
    d={'data':'Hai this ARe jangO BUiltin FIlters','t':t,'c':1}
    
    return render(request,'builtin_filters.html',d)