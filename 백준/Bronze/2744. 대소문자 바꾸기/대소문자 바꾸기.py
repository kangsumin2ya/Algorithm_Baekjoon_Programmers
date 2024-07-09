# 단어 입력
word = str(input())

# 변경한 단어 저장
new = []

# 비교해서 대소문자 변환
for w in word:
    if w.isupper():
        new.append(w.lower())
    else:
        new.append(w.upper())

# 결과 출력
print(''.join(new))