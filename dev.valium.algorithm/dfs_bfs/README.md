# DFS/BFS

### Basis
파이썬에서 스택은 별도의 import 없이 사용가능하다.
```python
stack = []

stack.append(5)
stack.pop()
```  

파이썬에서 큐는 deque 라이브러리를 사용한다.
```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(6)
queue.popleft()
queue.reverse()
```

### DFS
Depth-First Search 로 깊이 우선탐색이다.


