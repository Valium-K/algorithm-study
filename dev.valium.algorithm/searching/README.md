# 탐색

## 빠른 입력
이진 탐색과 같은 문제는 입력 데이터가 앖거나, 탐색 범위가 매우 넓다.  
즉, 시간 초과가 일어날 확률이 높기에 가능한 input()이 아닌   
sys.stdin.readline().restrip()을 사용하면 시간 초과를 피할 수 있다.

```python
import sys

# rstrip(): 개행문자 제거
data = sys.stdin.readline().rstrip()
```