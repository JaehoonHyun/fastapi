import sys

print('sys.path from util.py')
print('\n'.join(sys.path))
print()

print('__name__ of util.py')
print(__name__)
print()

# relative import : 현재 모듈이 위치한 기준으로 모듈을 찾는다.
# 직접 실행하면 에러남
# 해결방법1 : sys.path에 직접 추가한다.
# 해결방법2 : PYTHONPATH 환경변수에 추가한다.
# 해결방법3 : 모듈에서 직접 실행하지 않는다.
from . import library
