python = "Python is Amazing"
print(python.lower())                   # 문자를 전부 소문자로 변경
print(python.upper())                   # 문자를 전부 대문자로 변경
print(python[0].isupper())              # [0] 번째 문자가 대문자이냐?
print(len(python))                      # 문자의 길이
print(python.replace("Python", "Java")) # Python을 Java로 변경한다.

index = python.index("n")               # n의 위치
print(index)
index = python.index("n", index + 1)    # n 이후 또 다른 n의 위치
print(index)

print(python.find("n"))                 # find는 원하는 값이 없을 때 -1을 반환한다.
print(python.find("Java"))

print(python.count("n"))                # python에 n 이 몇개 있냐?