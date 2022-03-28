from rest_framework.permissions import BasePermission
from  rest_framework.exceptions import PermissionDenied
import re


class MyPermission(BasePermission):
    def __init__(self):
        # 不需要权限的路径
        self.common_paths = ['/user/login/']
    def  has_permission(self,request,view):
        curent_url = request.path_info
        method = request.method
        p = re.compile('([a-zA-Z]|[0-9]|[.])|(/.*)')
        url = p.findall(curent_url)[0][1]
        if url == "/":
            raise PermissionDenied('不能访问此路径')
        for i in self.common_paths:
            i = '^{}$'.format(i)
            flag = re.match(i,url)



