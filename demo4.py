#条件判断
#基本和c#相似，不过不要括号，结尾用冒号
if 2 < 1 or 1 > 2:
    print("%s" %True)
elif not 3 != 2:#不等于既可以用!=也可以 <>，不清楚有什么区别
    pass
else:
    s = "dfs"
    print("s is ",s)
#和C#一样从上到下，有为true的条件就执行并忽略之后的条件
x=None
if x:
    pass
#只要x不为空、非零，就返回true

#输入
inputage = input("请输入年龄：")
age = int(inputage)
if age > 18:
    print("成年人")
else:
    print("未成年")
#测试

ih = input("请输入身高(m)：")
iw = input("请输入体重(kg)：")
height = int(ih)
weight = int(iw)
bmi = weight / (height * height)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28:
    print("过重")
elif bmi >= 28 and bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")