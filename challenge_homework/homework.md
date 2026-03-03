# 数据库系统作业 —— 题目一
## 题目
解释关系数据库中“关系”的含义。
## 作答
在关系数据库中，关系是由若干行和列组成的二维表结构，每一行表示一个元组，每一列表示一个属性，用于描述同一类实体的数据集合。


# 数据库系统作业 —— 题目三
## 一、题目说明
本题通过调用大语言模型API，分别使用DeepSeek V3和R1模型回答SQL查询问题，并对结果进行对比分析。
## 二、SQL问题描述
已知表结构如下：
```sql
create table classroom
(building varchar(15),
 room_number varchar(7),
 capacity numeric(4,0),
 primary key (building, room_number)
);
```
问题：找出容量最大的教师房间号。
## 三、DeepSeek V3回答
```sql
SELECT room_number
FROM classroom
WHERE capacity = (SELECT MAX(capacity) FROM classroom);
```
## 四、R1回答
```sql
SELECT room_number
FROM classroom
WHERE capacity = (SELECT MAX(capacity) FROM classroom);
```
## 五、结果分析
两个模型均采用MAX函数和子查询获取最大容量，并通过WHERE条件筛选对应记录，查询逻辑正确，结果符合教材标准答案。
## 六、大模型辅助说明
本作业在代码编写与文档整理过程中使用了ChatGPT辅助，核心内容由本人理解并核实后完成。
