# 참고 링크 : https://moon-gd.tistory.com/36
length = int(input())
sentence = input().lower().rstrip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in alphabet:
    sentence = sentence.replace(c, ' ')

sentence = list(map(int, sentence.split()))

print(sum(sentence))