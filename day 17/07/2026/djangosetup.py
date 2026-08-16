# Import HttpResponse
from django.http import HttpResponse


# Create a view function
def home(request):

    # Return a message to the browser
    return HttpResponse("Hello, Django!")
# Import admin
from django.contrib import admin

# Import path
from django.urls import path

# Import views from myapp
from myapp import views


# URL patterns
urlpatterns = [

    # Django admin URL
    path('admin/', admin.site.urls),

    # Home page URL
    path('', views.home),
]
