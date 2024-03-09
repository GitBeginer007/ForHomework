#include<sys/timeb.h>
#include<stdio.h>
#include<stdlib.h>
#if defined(WIN32)
# define TIMEB _timeb
# define ftime _ftime
typedef __int64 TIME_T;
#else
#define TIMEB timeb
typedef long long TIME_T;
#endif
int time_interval()
{
    struct TIMEB ts1,ts2;
    TIME_T t1,t2;
    int ti;
    ftime(&ts1);
    {
        int i;
        for(i=0;i<100000;i++)
        {
            int *p=malloc(10000);
            int *q=malloc(10000);
            int *s=malloc(10000);
            int *t=malloc(10000);
            free(p);
            free(q);
            free(s);
            free(t);
        }
    }
    ftime(&ts2);
    t1=(TIME_T)ts1.time*1000+ts1.millitm;
    printf("t1=%lld\n",t1);
    t2=(TIME_T)ts2.time*1000+ts2.millitm;
    printf("t2=%lld\n",t2);
    ti=t2-t1;
    return ti;
}
int main()
{
    int t,m=1;
    for(t=1;t<=1000000;t++)
    {m++;}
    int ti=time_interval();
    printf("time interval=%d\n",ti);
    printf("%d\n",m);
}