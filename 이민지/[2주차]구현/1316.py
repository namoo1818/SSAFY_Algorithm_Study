n = int(input())
ans = 0
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        # 연달아 같은 문자가 안 올 경우
        if word[i] != word[i+1]:
            # 다른 문자가 온 순간을 기준으로 단어 잘라서 새 단어 만들기
            new_word = word[i+1:]
            # 새 단어에 아까 문자가 올 경우 그룹 단어가 아니므로 break
            if word[i] in new_word:
                break
    # for-else문
    # if문을 다 통과했다는 의미는 그룹 단어라는 말이니까
    # ans+1
    else:
        ans+=1
print(ans)
    