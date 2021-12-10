# 패키지 = 모듈을 모은 집합
# 폴더를 만든다.

from travel import thailand
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# travel.thailand 모듈에서 TahilandPackage 클래스를 가지고 온다라는 뜻
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 파일의 위치를 확인 하는 것
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))