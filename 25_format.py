# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 - 표시
print("{0: >+10}".format(-500))
print("{0: >+10}".format(500))

# 왼쪽 정렬하고, 빈칸으로 _채움
print("{0:_<+10}".format(500))
print("{0:_<+10}".format(-500))

# 3 자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000000000))
print("{0:+,}".format(-10000000000000000))

# 3자리 마다 콤마를 찍어주지, 부호도 붙이고, 자릿수 확보
# 빈자리 ^ 로 채움
print("{0:^<+30}".format(1000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리 까지만 표시
print("{0:.2f}".format(5/3))
