from openai import OpenAI

client = OpenAI(api_key='your_api_key')


def ask_gpt_4o_sys_user(system_prompt, user_prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ], )
    return completion.choices[0].message.content


def ask_gpt_4o_user(user_prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt},
        ], )
    return completion.choices[0].message.content
