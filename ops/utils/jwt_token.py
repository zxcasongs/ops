import datetime
import  jwt
from jwt import exceptions
JWT_SALT = '(mi_r9mgq1j$9@1e41_f9i4n2a1121uvaqm-fax_ye8ycgqj=_'

def create_jwt_token(payload,timeout=20):
    headers = {
        'type':'jwt',
        'alg':'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key =JWT_SALT,algorithm="HS256", headers=headers).decode("utf-8")
    return  result

def parse_payload(token):
    result={'status': False, 'data': None, 'errmsg': None}
    try:
        verified_payload = jwt.decode(token,JWT_SALT,True)
        result['data'] = verified_payload
        result['status'] = True
    except exceptions.ExpiredSignatureError:
        result['errmsg'] = 'token已失效'

    except jwt.DecodeError:
        result['errmsg'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['errmsg'] = '非法的token'
    return result