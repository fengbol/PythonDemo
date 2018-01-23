#列表和元祖
#列表和元组都是有序的
students = ["张三","李四","赵四","王五"]
students = list(["张三","李四","赵四","王五"])  #同上
#索引,同样是从0开始，但是可以用-1表示倒数第一个元素，并且可以以此类推
students[0]
students[-2]
#追加，用append可以添加元素到末尾
students.append("小二")
#插入，用insert添加元素到指定索引
students.insert(2,"吉良吉影")
#删除，pop删除指定索引位置的元素，不加参数则删除末尾元素
students.pop(2)
#赋值
students[1] = "卖鱼强"
#list里的值可以不同类型，也可以嵌套list
newlist = ["JoJo",8,True]
morelist = [["Dio",2,3],"acdc",9] #注意len(morelist)结果为3
morelist[0][0] #结果为Dio，这么看有点像二维数组

#元组感觉像是常量型的列表，一旦初始化就不能更改，用小括号
teachers = ("张老师","邓校长",8)
#如果元组只有一个值，要加,防歧义
newTuple = (2,)
#元组也可以改变的
varTuple = (2,["a","b"],"c")#可以修改里面列表的值，但是不能改变列表指向
