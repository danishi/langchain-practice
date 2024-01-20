import json
import openai

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="今日はとてもいい日だが、何かが引っかかる。そうだ！",
    stop="。",
    max_tokens=100,
    temperature=0.5,
    n=2
)

print(json.dumps(response, indent=2, ensure_ascii=False))
