# mutual exclusion(상호배제)
# Python에서는 single core만 사용하기 때문에 multi threading이 크게 영향을 끼치지 않는다
# Python에서는 multi threading 은 concurrency 로서의 의미가 있고 parallal의 의미는 없다
# concurrency: 함수를 두개 동시 실행 가능(cpu는 하나만 사용)
# parallal: 함수 두개를 동시 실행 하는데 cpu를 multi로 사용 한다.


# race condition
# 공유자원을 여러 thread에서 경쟁하듯이 접근, 수정 하려고 하는 것
# 이로 인해 예상치 못한 error가 일어난다.

import threading

# 전역 변수
# 모든 thread에서 공유할수 있는 메모리 : 공유 자원 (shared resource)
g_count = 0
# lock 객체
lock = threading.Lock()

def thread_main():
    global g_count
    # 임계영역 : 공유자원에 접근해서 수정하련는 코드
    # Critical section(임계영역)
    # lock을 통해 다른 thread에서 접근하지 못하도록 한다.
    lock.acquire()
    for _ in range(100000):
        g_count += 1
    lock.release()
threads = []

for _ in range(50):
    threads.append(threading.Thread(target=thread_main))

for th in  threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {}'.format(g_count))