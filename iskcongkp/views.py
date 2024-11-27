from django.shortcuts import render
from events.models import Event
from .LoggerData import LogData 

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home_view(request):
    function_name = __name__ + '.' + home_view.__name__
    ipAddress = visitor_ip_address(request)
    log_id = LogData('DscWeb', ipAddress, function_name,
                     "Website loaded Successfully", request.POST)

    faculty = [
        {
            "name": "Santosh Kumar",
            "email": "santosh.recb@gmail.com",
            "area": "Networking, Algorithms, SDN",
            "image": "http://recb.ac.in/FacultyPhoto/Faculty21313_20072019012028.jpg",
        },
        {
            "name": "Sudhir Goswami",
            "email": "sudhirgoswami.recb@gmail.com",
            "area": "Image Processing and Algorithm Design",
            "image": "http://recb.ac.in/FacultyPhoto/Faculty04512_20072019012212.JPG",
        },
    ]
    events = Event.objects.all().filter(is_active=True)
    context = {
        "title": "DSC",
        #"members": members,
        "events": events,
        "faculty": faculty,
    }
    return render(request, "home.html", context)


def about_view(request):
    function_name = __name__ + '.' + about_view.__name__
    ipAddress = visitor_ip_address(request)
    context = {"title": "About Us"}
    LogData('DSCweb', ipAddress, function_name,
            'About Page loaded Successfully...', request.POST)
    return render(request, "about.html", context)