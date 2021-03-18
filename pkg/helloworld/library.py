import sys
print('sys.path from library.py')
print('\n'.join(sys.path))
print()

#expect in play here
"""
/root/workspace/opensource/fastapi/pkg/helloworld
"""

print('__name__ of library.py')
print(__name__)
print()
