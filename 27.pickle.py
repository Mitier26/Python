import pickle
profile_file = open("profile.pickle", "wb")     # wb : 읽고, 바이너리 타입(항상 정의해 주어야 한다

profile = {"이름" : "홍길동", "나이":44, "취미":["축구", "야구", "배구"]}
print(profile)
pickle.dump(profile, profile_file)
# profile 에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
# 파일에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
