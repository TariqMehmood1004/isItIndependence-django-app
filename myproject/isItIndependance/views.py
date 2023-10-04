import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    independanceDay = datetime.datetime.now()
    isIndependanceDay = False
    
    if independanceDay.month == 8 and independanceDay.day == 14:
        isIndependanceDay = True
    else:
        isIndependanceDay = False
    
    return render(request, "isItIndependance/index.html", {
        'independance': isIndependanceDay,
        'nowTime': independanceDay
        })
    
