from rest_framework.response import Response

class APIResponse(Response):
    def __init__(self, errcode=0, errmsg=None, data=None, status=None, headers=None, **kwargs):
        dic = {'errcode':errcode,'errmsg':errmsg}
        if data:
            dic = {'errcode': errcode, 'errmsg': errmsg, 'data': data}
        dic.update(kwargs)

        super().__init__(data=dic,status=status,headers=headers,)


