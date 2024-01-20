import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "面白い話して"
        }
    ],
    max_tokens=100,
    temperature=1, # 0~2：高いほど予測の確信度が低い選択肢を取りやすくなる。物語など何度も書かせて良い結果を得たいときに上げるのが一般的。
    n=2
)

print(json.dumps(response, indent=2, ensure_ascii=False))
