names = ["유튜버1", "유튜버2", "유튜버3", "유튜버4"]

for name in names:
    email_file = open("{0}.txt".format(name), "w", encoding="utf-8")
    print("안녕하세요? {0} 님".format(name), file=email_file)
    print("\n(주) 나도출판 편지자 나코입니다.", file=email_file)
    print("\n현재 저희츨판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\
            \n{0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\
            \n자세한 내용은 첨부드리는 제안서를 화긴 부탁드리며, 긍정작인 회신 기다리겠습니다.".format(name), file=email_file)
    print("좋은 하루 보내세요 ^^\
            \n감사합니다.\
            \n\n-나코 드림.", file=email_file)
    email_file.close()