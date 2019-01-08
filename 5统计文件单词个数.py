f = open("english.txt")
content = f.read()
content = content.replace(",", "").replace('"', "").replace(".", "").replace("!", "").replace("\n", " ").replace("?",
                                                                                                                 "")
content = content.lower()  # 把字符的字母统一转换为小写
# content = content.upper()  # 把字符的字母统一转换为大写
f.close()
# print(content)
words = content.split(" ")
# print(words)

# 常规方法
# word_count = {}  # 定义一个空字典
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

# 调用python包
from collections import Counter

word_count = Counter(words)
top_10 = word_count.most_common(10)  # 统计词频最高的10个词
print(word_count)  # 输出结果对词频进行了排序
print(top_10)
