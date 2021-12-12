# 필요한 것 끼리 모여있는 부품
# 모듈은 같은 경로에 있어야 사용이 가능 하다.

import module1
module1.price(3)
module1.price_morning(4)

# 모듈의 이름을 mv 로 사용하겠다.
import module1 as mv
mv.price(3)

# *을 사용하면 더 줄일수 있다.
from module1 import *
price(3)
price_morning(4)

# 필요한 함수만 사용하는것도 가능 하다.
from module1 import price, price_morning
price(3)
price_morning(4)

# price를 사용했는데 군인 가격이 나온다.
# price는 변수 이름 같은 것이다.
from module1 import price_soldier as price
price(3)