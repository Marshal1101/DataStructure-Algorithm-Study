#### 정렬 lambda
```python
## 문자 이터 (a, b) a 정수 오름차순, a 동일 시 b 정수 오름차순
nxy.sort(key=lambda x: (int(x[0]), int(x[1])))

## 문자 a b 에서 a 정수 기준
people.sort(key=lambda x:int(x.split(' ')[0]))

## 문자열 받아서 튜플로 왜? 기준??? -> [0] 기준 같음
data.sort(key=lambda x: tuple(map(int, x.split())))

## [2]->[0]->[1] 작은 순서대로 
eat.sort(key = lambda x : (x[2], x[0], x[1]))
```

#### key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
```python
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
```

#### 플로이드워셜
```python
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if i == j : graph[i][j] = 0; continue
            temp = graph[i][k] + graph[k][j]
            if temp < graph[i][j] :
                graph[i][j] = temp
```
