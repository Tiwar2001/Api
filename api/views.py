from django.http import HttpResponse

def Home_Page(request):

    print("Welcome")

    return HttpResponse ("Hi") 