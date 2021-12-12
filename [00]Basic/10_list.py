# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway)

subway = ["감자", "고구마", "양파"]
print(subway)

print(subway.index("고구마"))

# 뒤에 값을 추가
subway.append("수박")
print(subway)

# 중간에 값을 추가
subway.insert(1, "고추")
print(subway)
# 감자와 고구마 사이에 값을 넣고 뒤로 민다.

# 값을 제거, 제알 마지막 값을 제거한다.
print(subway.pop())
print(subway)

# 같은 값이 몇개 인지 확인
subway.append("감자")
print(subway)
print(subway.count("감자"))


# 정렬도 가능
num_list = [6,5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 값 제거
# num_list.clear()
print(num_list)

mix_list = ["감자", 44, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)