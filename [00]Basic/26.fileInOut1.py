# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0" , file=score_file )
# print("영어 : 50" , file=score_file )
# score_file.close()

# a : 있던 파일에 이어서 쓰기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 30")
score_file.write("\n코딩 : 80")
score_file.close()

# 주의!!!
# write를 사용할 경우 자동으로 줄바꿈 해 주지 않는다.
# \n 을 사용하여 줄 바꿈 해 주자.