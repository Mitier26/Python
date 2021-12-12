import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 파일의 내용을 불러와 profile_file 에 넣는다.
# 픽클의 로드를 이용하여 파이 내용을 출력한다.
# with 는 close() 가 필요 없다.

with open("study.txt", "w", encoding="utf8 ") as study_file:
    study_file.write("파이썬을 공부하고 있다")

with open("study.txt", "r", encoding="utf8 ") as study_file:
    print(study_file.read())