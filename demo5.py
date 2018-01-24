#循环
#第一种for...in类似C#里的foreach
names = ["Jonathan Joestar","Joseph Joestar ","Kuujou Joutarou","Higashikata Josuke","Giorno Giovanna","Jolyne Kujo",
    "Johnny Joestar","Josuke Higashikata"]
for name in names:
    print(name)
#range(x)方法可以生成从0开始到小于指定数x的序列
sum = 0
for i in list(range(5)):
    sum = sum + i
    print("",sum)
#while和c#一样，同样可以用break跳出循环，continue继续下次循环
while sum > 100:
    print("",sum)
    if sum > 50:
        break
    else:
        continue
#字典
#用大括号包含，冒号连接key和value
scores = { "Anna":95,"Booker":90,"Comstock":80}
newdict = { 5:5,"s":10,"a":"b"}
#使用in判断key是否存在，或者使用get()方法
if "anna" in scores:
    print(scores["anna"])
print(scores.get("anna"))
print(newdict.get(4,-1))#找不到就返回-1
#用pop(key)可以删除key和对应value
newdict.pop(5)
