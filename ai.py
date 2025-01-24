from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
