from nltk import tokenize

p = "Good morning Dr. Adams. The patient is waiting for you in room number 3."
p = '안녕하세요. 제 이름은 박장원입니다. 오늘은 치킨을 사먹을 예정입니다.'
print(tokenize.sent_tokenize(p))
