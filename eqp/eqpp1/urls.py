from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index),
    path('Signup/', views.Signup, name="Signup"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("login/", views.login, name="login"),
    path("update/<int:id>/", views.update, name="Update"),
    path("leasordetails/", views.leasordetails, name="leasordetails"),
    path("admindetails/", views.admindetails, name="admindetails"),
    path("leasseview/", views.leasseview, name="leasseview"),
    path("admins/", views.admins, name="admins"),
    path("pendings/", views.Pendings, name="Pendings"),
    path("customer/", views.customer, name="customer"),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.destroy),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
