score_file = open("score.txt", "r", encoding="utf8")

# 파일의 내용이 몇 줄인지 알 수 없을 때 반복문을 사용
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()