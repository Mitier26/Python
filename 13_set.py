# 세트 (set)
# 중복이 안됨, 순서 없음
my_set = {1,2,3,3,5,6,6,6}
print(my_set)

java = {"감자", "고구마", "양파"}
python = set(["감자", "수박"])

# 교집합 (자바와 파이썬을 모두 할 수 있는 것)
print(java & python)
print(java.intersection(python))

# 합집합 (자바 할 수도 있거나 파이썬 할 수 있는 것)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬은 할 수 없는 것)
print(java - python)
print(java.difference(python))

# 파이썬 할 줄 아는 것이 늘어남
python.add("양파")
print(python)

# 자바를 잊어버림
java.remove("고구마")
print(java)