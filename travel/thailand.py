class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 (야시장 투어) 50만원")

# 이곳 파일에서 실행할때 나오는 부분이다.
# 외부에서 불러와 사용할 때는 실행되지 않는다.
# 테스트 용으르 사용한다.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문중은 모듈을 직접 실행할 때만 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")