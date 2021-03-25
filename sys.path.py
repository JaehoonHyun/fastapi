# sys.path는 모듈을 import할 때 모듈을 찾아야할 경로들을 저장해둔 list
# 경로들을 저장해둔 list!!
# 경로들을 저장해둔 list!!
# 리스트의 순서대로 찾는다. [A, B, C] 이면, A에서 hit하면 A의 모듈을 씀

import sys
print('sys.path from sys.path.py')
print('\n'.join(sys.path))


#expect
"""
/root/workspace/opensource/fastapi
/usr/lib/python36.zip
/usr/lib/python3.6
/usr/lib/python3.6/lib-dynload
/usr/local/lib/python3.6/dist-packages
/usr/lib/python3/dist-packages
"""

print('__name__ of sys.path.py')
print(__name__)
print()

# pkg/helloworld로 부터(from) library를 가져오겠다(import)
from pkg.helloworld import library

# pkg/helloworld로 부터(from) util를 가져오겠다(import)
# 하지만, util에서 libray를 땡겨오는데, 실행파일 기준으로 해석하므로 못찾음
from pkg.helloworld import util

from pkg.clazz.bag import BackPack

b = BackPack('backpack')
b.add_trick('bag? or pocket') #expected : I am bag add_trick
b.show() #expected : I am BackPack show

import keycloak
keycloak_openid = keycloak.KeycloakOpenID(server_url="http://hooneyo.xtrm-istio.io:80/auth/",
                    client_id="example_client",
                    realm_name="example_realm",)

# 접속실패시 여기서 에러 뿜뿜
config_well_know = keycloak_openid.well_know()

# user / password 
# user가 없으면 invalid
# keycloak user 셋팅에서 user가 있는데 패스워드의 temporary속성이 true이면 다음번에 비번업데이트 필수이다. 이걸하지 않으면 token account is not fully set up 에러가 발생
token = keycloak_openid.token("user", "admin")

userinfo = keycloak_openid.userinfo(token['access_token'])

#Logout: session 지움
keycloak_openid.logout(token['refresh_token'])

#expected it is failed : 401: b'{"error":"invalid_request","error_description":"User session not found or doesn\'t have client attached on it"}'
try:
    userinfo = keycloak_openid.userinfo(token['access_token'])
except keycloak.exceptions.KeycloakAuthenticationError:
    print(sys.exc_info()[0])


print('helloworld')
