import re
import json

from data.file_paths import result_jsonl_path
from data.system_prompts import system_prompts_1
from data.user_prompts import user_prompt_1
from utils.ask_gpt_4o import ask_gpt_4o_sys_user
from utils.get_complete_prompt import get_complete_prompt

regular_expression = re.compile(r'<(.*?)>')


def write_txt_file(file):
    with open(file, "r", encoding="utf-8") as file:
        file_path = "data\\results\\" + file.name.split("\\")[-1]
        user_prompt = get_complete_prompt(user_prompt_1, file.read())

        response = ask_gpt_4o_sys_user(system_prompts_1, user_prompt)
        # print(response)

    with open(file_path, "w", encoding="utf-8") as file:
        match = re.findall(regular_expression, response)
        for sentence in match:
            if sentence != match[-1]:
                file.write(sentence + "\n")
            else:
                file.write(sentence)

    return file_path


def write_jsonl_file(file, open_with, sentence_id):
    sentences = []
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            sentences.append(line)
        # print(sentences)

    with open(result_jsonl_path, open_with, encoding="utf-8") as file:
        # data = {"id": 1, "content": "测试"}
        # print(json.dumps(data, ensure_ascii=False, indent=4))

        for sentence in sentences:
            if len(sentence.strip("。")) <= 20:
                continue
            data = {"id": sentence_id, "content": sentence.strip("\n")}
            # print(json.dumps(data, ensure_ascii=False, indent=4))
            file.write(json.dumps(data, ensure_ascii=False, indent=4) + '\n')
            sentence_id += 1

    return sentence_id
