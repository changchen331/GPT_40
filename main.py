from data.file_paths import subtitles_path
from data.system_prompts import system_prompt_2, system_prompt_1
from data.user_prompts import user_prompt_1
from utils.write_file import write_file, write_files

if __name__ == '__main__':
    # serial_number = "test" + str(331)
    # write_file(subtitles_path + serial_number + '.txt', system_prompt_2, user_prompt_1)

    start_number = 10
    end_number = 12
    write_files(subtitles_path, start_number, end_number, system_prompt_2, user_prompt_1)
