import sys
print('sys.path from sys.path.py')
print('\n'.join(sys.path))

import jwt
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
body = jwt.decode(token, key="your-256-bit-secret", algorithms=["HS256"], verify=True)
print(body)

token_en=jwt.encode(body, key="your-256-bit-secret", algorithm="HS256").decode("UTF-8")

if token == token_en:
    print('token is equal to token_en')
else:
    print(f"{token}")
    print(f"{token_en}")

body = jwt.decode(token_en, key="your-256-bit-secret", algorithms=["HS256"], verify=True)
print(body)
