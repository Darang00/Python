#%% 문자 형변환
# print("%c " %65) #A
#print("%d" %'A') #TypeError
# chr(정수) : 정수를 문자로 바꿔주는 함수
# ord(문자) : 문자를 정수로 바꿔주는 함수
# 

print(ord('A')) # 65
print(ord('A') * 3) # 195
print(chr(ord('A') * 3)) # Ã (암호화됨)
print("\n")
print(ord('A')) # 65
print(ord('A') * 4) # 260
print(chr(ord('A') * 4)) # Ą (암호화됨)
print("\n")
print(ord('A')) # 65
print(ord('A') * 9) # 585
print(chr(ord('A') * 9)) # ɉ (암호화됨)
print("\n\n")


#%% 비밀번호 암호화/복호화

pw = "a1b2c3"
en_pw = "" # 암호화된 비밀번호 담는 공간
de_pw = "" # 복호화된 비밀번호 담는 공간

# 암호화
for i in pw:
    en_pw += chr(ord(i) * 9);
    
print("기존 비밀번호: %s" %pw); # a1b2c3
print("암호화된 비밀번호: {pw}".format(pw=en_pw)) # ƹͲǂͻǋ

# 복호화
for i in en_pw:
    de_pw += chr(ord(i) // 9)

print("암호화된 비밀번호: {en_pw}\n복호화된 비밀번호  : {de_pw}".format(en_pw=en_pw, de_pw=de_pw))



# 결론: 아스키코드를 통해서 암호화를 할 수 있다.
# 회원가입 시 사용자의 비밀번호 혹은 개인정보를 암호화 할 때 
# 아스키 코드를 사용한다.
    


