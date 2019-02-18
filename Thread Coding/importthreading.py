# single thread example

import threading
import time
# 요소의 개수
n = 1000
num_thread = 4

# 요소의 개수 / thread 개수 -> 한 쓰레드가 담당할 개수
offset = n // num_thread

# thread 에서 실행될 함수
def thread_main(li, start_point):
    # 인위적으로 쓰레드를 지연시켜 join을 통해 메인을 대기했을때와 안했을때 비교를 한다.
    time.sleep(0.5)

    # thread_main 함수 내용
    for idx in range(offset*start_point, offset*(start_point+1)):
        li[idx]*=2

# thread 1 : 0 ~ 249, thread 2 : 250 ~ 499 ...
# 전역 변수: 모든 thread에서 접근가능
li = [i+1 for i in range(n)]

# thread를 담을 리스트
threads = []
for i in range(num_thread):
    th = threading.Thread(target=thread_main, args=(li, i))
    threads.append(th)


# thread의 실행을 시작
for th in threads:
    th.start()

# thread의 실행이 끝날때 까지 메인 thread가 기다린다.
for th in threads:
    th.join()

print(li)