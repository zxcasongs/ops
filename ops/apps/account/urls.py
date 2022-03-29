from django.conf.urls import url
from apps.account.view.user import UserLogin,SendCodeView


urlpatterns = [
    url(r'(?P<version>[v1|v2]+)/user/login$',UserLogin.as_view(),name='login'),
    url(r'(?P<version>[v1|v2]+)/user/sendcodeview$',SendCodeView.as_view(),name='getuser')

]