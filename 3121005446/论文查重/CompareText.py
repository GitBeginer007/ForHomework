import sys
import difflib
import time

# 开始计时
start_time = time.time()

#先定义一个采用自带库difflib判断相似度的函数
def Similarity_Rate(file1,file2):
    return difflib.SequenceMatcher(None,file1,file2).ratio()

#从命令行传入需要处理的文件的绝对地址
file_Adrs=sys.argv

#Oritext=sys.argv[1]
#Alttext=sys.argv[2]
#Reptext=sys.argv[3]

#打开文件并且读取内容
try:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        t1=f.read()
    with open(sys.argv[2], 'r', encoding='utf-8') as f:
        t2=f.read()
except:
    if len(file_Adrs) != 4:
        print("Please enter \"你的文件名 *原文件 *相似文件 *报告文件(文件路径)\"")
        sys.exit(1)
    else:
        print("Please check the state of your files")
        sys.exit(2)

#给个标签
rate=Similarity_Rate(t1,t2)

#打印相似度，可用于快速测试
if __name__=='__main__':
    print(Similarity_Rate(t1,t2))

#输出文件
with open(sys.argv[3], 'r', encoding='utf-8') as f:
    f.write("两者相似度为：rate")

# 结束计时
end_time = time.time()

# 计算并打印运行时间
run_time = end_time - start_time
print(f"程序运行时间为: {run_time} 秒")