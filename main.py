import re
from pathlib import Path

from data.file_paths import subtitles_path
from utils.write_file import write_jsonl_file, write_txt_file

if __name__ == '__main__':
    count = 0
    sentence_id = 1
    regular_expression = re.compile(r"\d+")

    p = Path(subtitles_path)
    for file in p.rglob('*.txt'):
        # print(file)

        number = int(re.search(regular_expression, file.name).group())
        # print(number)

        target_file = write_txt_file(file)
        if count == 0:
            open_with = "w"
        else:
            open_with = "a"
        sentence_id = write_jsonl_file(target_file, open_with, sentence_id)
        count += 1
        print(file.name + " is done")

        # if number >= 10:
        #     break
        if sentence_id >= 1000:
            break

    print("共处理 " + str(count) + " 个文件")

    # target_file = write_txt_file("data\\subtitles\\test2.txt")
    # sentence_id = write_jsonl_file(target_file, "w", sentence_id)
    # print(sentence_id)
