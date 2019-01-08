
# 列表 list
# 创建 添加 删除 更新 查找 遍历

# 字典 dictionary
# 1.创建
a = {}  # a=[]
b = dict()  # a=list()
c = {
    'name': 'zhangsan',
    'age': 20,
    'address': '郑州'
}
print(c)

# 2.添加
# 对于列表: a.append() a.insert()
c['sex'] = '男'
c['name'] = 'lisi'
print(c)

# 3.删除
# a.pop() a.remove()
# 参数1:k=key,删除的字典的字段
c.pop('name')
print(c)
# c.pop('phone')#删除的字段若不存在,则会报错
c.popitem()  # 删除字典的随机一个字段
c.popitem()  # 如果字典已为空,则删除报错

# 4.查找
# 列表操作:#'zhangsan' in ['zhangsan','lisi']
print('age' in c)
print('phone' in c.keys())
print('郑州' in c.values())

# 5.获取
# 列表获取:a[3]

# 不推荐
name = c['age']
print(name)
# 推荐
# 参数1 k=key
# 参数2 default默认值为None, null = none = nil
name = c.get('name', '姓名不存在')
print(name)

# 6.遍历
# 不推荐
for key in c:
    value = c.get(key)
    print(key, value)

# 推荐
for key, value in c.items():
    print(key, value)
