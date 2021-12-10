# glob : 경로 내의 폴더 / 파일 목록 조회 (원도우 dir)
import glob
# " " : 안에 검색할 것을 넣자.
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능 : 폴더 생성, 삭제
import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재 하는 폴더")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했다")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했다")

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘의 날짜 : " , datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("100일 지난 날짜 : ", today + td)