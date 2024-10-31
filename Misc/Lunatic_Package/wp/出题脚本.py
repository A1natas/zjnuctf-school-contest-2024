import zipfile
import tarfile
import py7zr
import os


def check_exist(directory_path):
    if os.path.exists(directory_path):
        print(f"[+]{directory_path}目录已存在")
    else:
        os.mkdir(directory_path)
        print(f"[+]{directory_path}目录创建成功")


def compress_7z(archive_file):
    check_exist("./tmp")
    output_file = "./tmp/flag.7z"
    output_file_name = "flag.7z"
    with py7zr.SevenZipFile(output_file, 'w') as archive:
        archive.write(archive_file)
    print(f"[+] {archive_file} ==> {output_file} 成功")
    os.remove(archive_file)
    os.system("mv ./tmp/flag.7z ./flag.7z")
    os.removedirs("./tmp")
    return output_file_name


def compress_zip(archive_file):
    check_exist("./tmp")
    output_file = "./tmp/flag.zip"
    output_file_name = "flag.zip"
    with zipfile.ZipFile(output_file, 'w') as zf:
        zf.write(archive_file)
    print(f"[+] {archive_file} == > {output_file} 成功")
    os.remove(archive_file)
    os.system("mv ./tmp/flag.zip ./flag.zip")
    os.removedirs("./tmp")
    return output_file_name


def compress_tar_gz(archive_file):
    check_exist("./tmp")
    output_file = "./tmp/flag.tar.gz"
    output_file_name = "flag.tar.gz"
    with tarfile.open(output_file, 'w:gz') as tar:
        tar.add(archive_file)
    print(f"[+] {archive_file} ==> {output_file} 成功")
    os.remove(archive_file)
    os.system("mv ./tmp/flag.tar.gz ./flag.tar.gz")
    os.removedirs("./tmp")
    return output_file_name


if __name__ == "__main__":
    morse_code = "--.. .--- -. ..- -.-. - ..-. ----.-- ..-. ..- -. -----.-"
    morse_code = morse_code[::-1]
    print(morse_code)
    length = len(morse_code)
    archive_file = "flag.txt"
    for i in range(length):
        if morse_code[i] == '.':
            archive_file = compress_zip(archive_file)
            print(archive_file)
        elif morse_code[i] == '-':
            archive_file = compress_7z(archive_file)
            print(archive_file)
        else:
            archive_file = compress_tar_gz(archive_file)
            print(archive_file)
