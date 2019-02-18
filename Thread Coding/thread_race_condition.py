# race condition
# 공유자원을 여러 thread에서 경쟁하듯이 접근, 수정 하려고 하는 것
# 이로 인해 예상치 못한 error가 일어난다.

import threading

# 전역 변수
# 모든 thread에서 공유할수 있는 메모리 : 공유 자원 (shared resource)
g_count = 0

def thread_main():
    global g_count
    for _ in range(100000):
        g_count += 1

threads = []

for _ in range(50):
    threads.append(threading.Thread(target=thread_main))

for th in  threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {}'.format(g_count))