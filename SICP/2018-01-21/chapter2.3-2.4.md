# 2.3 序列
序列是数据值的有序集合。与具有明确的两个元素的值对不同，序列可以有任意(但是有限)数量的有序元素。

序列不是特定的抽象数据类型，而是不同类型共享的行为集合。就是说，序列有许多种，但是它们都具有某些属性，尤其是，
- **长度**，序列是有限长度的。
- **元素选择**，序列有一个元素对应的小于其长度的任意非负整数的索引，第一个元素从0开始。

与抽象数据类型不同，我们没有说明如何构造一个序列。序列抽象是不完全指定类型(即，使用构造函数和选择器)的行为集合，但是可以在几个类型间共享。**序列提供了一个抽象层，可以准确隐藏特定程序操纵哪个序列类型的细节。**

## 2.3.1 嵌套对
这是一个嵌套元组的Python表达式，
```python
>>> ((1, 2), (3, 4))
((1, 2), (3, 4))
```
将具有以下结构，被称为*box-and-pointer*记法。
![box-and-pointer](http://i65.tinypic.com/j6iw44.jpg)

**我们使用元组作为其他元组元素的能力为我们的编程语言提供了一种新的组合手段**。我们称在这种方式中嵌套元组的能力为元组数据类型的*封闭性*。通常，**如果组合的结果本身可以使用相同的方法进行组合，则用于组合数据值的方法将满足封闭性。封闭是以任何方式进行组合的关键，因为它允许我们创建分层结构。**

> 列表包含列表、元组包含元组、字典包含字典；程序包含程序  
> 自包含为模块化设计提供了方便

## 2.3.2 递归列表