# 第一种写法
# 1.打开
# 参数1 file:文件路径
# 参数2 mode:模式(打开这个文件干什么?)
# r=read 读(默认)        rb=readbytes=读二进制
# w=write 写(先清空再写入)       wb=写二进制
# a=append 追加
# 参数4 encoding:编码
f = open('1.txt', 'w')
# 2.操作(读,写)
f.write('hello world\n')
f.write('nice to meet you')
# 一次性写入多个数据
f.writelines(['a', 'b', 'c'])
# 3.关闭
f.close()

# 读文件
f = open("english.txt", "r")
# content = f.read()  # 读取整个文件 缺点:若文件比较大则浪费内存
# content = f.read(5)  # 分批读取,每次读5个
# content = f.readline()  # 读取一行
content = f.readlines()  # 读取所有行,返回一个列表
f.close()
print(content)
