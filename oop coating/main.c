#include <stdio.h>


// 전역 변수
// 생성, 소멸 : 프로세스의 생성과 소멸과 같다
int g_num = 10;

// 지역변수 
// 생성, 소멸 : 함수의 호출과 종료와 같다

int func(int a, int b, int ** dbl_ptr)
{
    int c;
    c = a + b;

    // heap 영역에 할당
    // 생성 시점: 내가 원할때
    *dbl_ptr = (int*)malloc(sizeof(int));

    return c;
}

int main(void)
{
    int a = 10;
    int b = 20;
    int *ptr = NULL;

    func(a, b, &ptr);

    printf("%d \n", 8ptr)

    // heap 영역의 메모리 해제 시점
    // 해제 : 내가 원할때
    free(ptr);
    ptr = NULL;
    // 습관적으로 위와 같이 코드를 작성하는게 좋다
    // OS가 막아 놓긴 했지만
    // ptr에 주소가 남아 있기 때문에 접근 하려 한다
    // (Dangling Pointer)
    // 고로 NULL을 넣어 실수 하지 않도록 하자


    return 0;
}

