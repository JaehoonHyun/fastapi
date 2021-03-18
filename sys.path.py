# sys.path는 모듈을 import할 때 모듈을 찾아야할 경로들을 저장해둔 list
# 경로들을 저장해둔 list!!
# 경로들을 저장해둔 list!!
# 리스트의 순서대로 찾는다. [A, B, C] 이면, A에서 hit하면 A의 모듈을 씀

import sys
print('sys.path from main.py')
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
