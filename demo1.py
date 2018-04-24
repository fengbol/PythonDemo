#数据类型
i = 1
f = 1.1e9 #1.23 * 10的9次方
#另外Python里的整数和浮点数没有大小限制

hello = "I\'m \"Kidding\"!" #\转义符，I'm "Kidding"!
#也可以写成 
hello1 = r"I'm 'Kidding'!"
#另外"和'好像没什么区别，c#里用"代表字符串，'代表字符，所以我以后基本上会用"包含字符串

#多行文字 我觉得很不方便，尽量不要这么用吧
print("""sdf
    asdf
    sdf"""
)
#bool and or not 相当于c#里的& | !目前不清楚和&& ||的区别，另外True、False必须大写
print(True and False)
print(True or False)
print(not True)

#空值 None类似于C# null，但是要注意None不会输出的

#赋值，这是Python和C#最大的区别，Python里的变量类型是不固定的，即动态语言
#C#里有var关键字这样类似动态语言的写法，但var其实只是方便写法，类型还是固定的。
#var a=xxx 之后不能把a赋值为不同与xxx类型的值，Python下面的写法没问题
a = 1
a = "abc"

#常量，Python里没有常量机制，因为没有不能改的值，所以通常用全大写表示常量
PI = 3.14159265

#另外//和c#里的/一样，但是两个整数/却会得到浮点数，而%和c#一样是取余的