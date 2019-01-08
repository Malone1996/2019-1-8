# gb18030 中文编码 windows系统软件都采用gb18030
# utf-8 通用编码
f = open("movie.csv", "w", encoding="gb18030")
f.write("蜘蛛侠,3309,http//www.baidu.com\n")
f.write("蜘蛛侠2,13309,http//www.baidu.com\n")
f.write("蜘蛛侠3,23309,http//www.baidu.com\n")
f.close()
