import requests
import json

API_KEY = "my_API_KEY"

url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def ask(model_name, question):

    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "你是一个数据库专家"},
            {"role": "user", "content": question}
        ],
        "temperature": 0.2
    }

    res = requests.post(url, headers=headers, json=data)

    result = res.json()

    # 防止报 KeyError
    if "choices" not in result:
        print("接口调用失败：")
        print(result)
        return None

    return result["choices"][0]["message"]["content"]



question = """
已知如下表结构：

create table classroom
(building varchar(15),
 room_number varchar(7),
 capacity numeric(4,0),
 primary key (building, room_number)
);

请写出【严格符合数据库教材标准答案】的SQL语句，
要求：

1. 只返回 room_number
2. 不返回 building 或 capacity
3. 使用子查询 + MAX
4. 不要附加解释，只输出SQL
"""

# 调 DeepSeek V3
ans_v3 = ask("deepseek-chat", question)

# 调 R1
ans_r1 = ask("deepseek-reasoner", question)

print("=== DeepSeek V3 ===")
print(ans_v3)

print("\n=== R1 ===")

print(ans_r1)
