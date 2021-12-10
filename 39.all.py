#from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
# 이것게 하면 에러가 발생한다.
# 이유는 공개 처리를 안했기 때문이다.
# 공개 처리는 __init__ 에서 한다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()