import json
import re
from pathlib import Path

from utils.ask_gpt_4o import ask_gpt_4o_sys_user
from utils.get_complete_prompt import get_complete_prompt

regular_expression_file = re.compile(r"<(.*?)>")
regular_expression_files = re.compile(r"\d+")


# def write_txt_file(file):
#     with open(file, "r", encoding="utf-8") as file:
#         file_path = "data\\results\\" + file.name.split("\\")[-1]
#         user_prompt = get_complete_prompt(user_prompt_1, file.read())
#
#         response = ask_gpt_4o_sys_user(system_prompt_1, user_prompt)
#         # print(response)
#
#     with open(file_path, "w", encoding="utf-8") as file:
#         match = re.findall(regular_expression, response)
#         for sentence in match:
#             if sentence != match[-1]:
#                 file.write(sentence + "\n")
#             else:
#                 file.write(sentence)
#
#     return file_path


# def write_jsonl_file(file, open_with, sentence_id):
#     sentences = []
#     with open(file, "r", encoding="utf-8") as file:
#         for line in file:
#             sentences.append(line)
#         # print(sentences)
#
#     with open(result_jsonl_path, open_with, encoding="utf-8") as file:
#         # data = {"id": 1, "content": "测试"}
#         # print(json.dumps(data, ensure_ascii=False, indent=4))
#
#         for sentence in sentences:
#             if len(sentence.strip("。")) <= 20:
#                 continue
#             data = {"id": sentence_id, "content": sentence.strip("\n")}
#             # print(json.dumps(data, ensure_ascii=False, indent=4))
#             file.write(json.dumps(data, ensure_ascii=False, indent=4) + '\n')
#             sentence_id += 1
#
#     return sentence_id


def write_file(file, system_prompt, user_prompt):
    with open(file, encoding="utf-8") as file:
        user_prompt = get_complete_prompt(user_prompt, file.read())
        response = ask_gpt_4o_sys_user(system_prompt, user_prompt)

        file_path = "data\\results\\" + file.name.split("\\")[-1].replace(".txt", ".jsonl")
        file.close()

    with open(file_path, "w", encoding="utf-8") as file:
        sentence_id = 0
        match = re.findall(regular_expression_file, response)
        for sentence in match:
            data = {"id": sentence_id, "content": sentence.strip("\n")}
            file.write(json.dumps(data, ensure_ascii=False, indent=4) + '\n')
            sentence_id += 1

        print(file.name + " is done")
        file.close()


def write_files(file_path, start_number, end_number, system_prompt, user_prompt):
    count = 0
    p = Path(file_path)
    for file in p.rglob('*.txt'):
        number = int(re.search(regular_expression_files, file.name).group())
        if start_number <= number <= end_number:
            write_file(file, system_prompt, user_prompt)
            count += 1
        if count >= end_number - start_number + 1:
            break

    print("共处理 " + str(count) + " 个文件")
