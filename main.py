import os
import sys
import re


def rename(path: str):
    for file in os.scandir(path):
        if file.is_dir() is True:
            rename(file.path)
            continue

        if file.name.startswith(".") is True:
            continue

        ext = file.name.split(".").pop()
        filename_arr = file.name.split("_")

        if len(filename_arr) <= 1:
            continue

        new_filename = " ".join(filename_arr[: len(filename_arr) - 1])
        new_filename = re.sub(
            r"[Bb]lu[Rr]ay\s*(v\d)?\s*(\d{3}p)\s*(v\d\s*)?\([A-Za-z]+.(com|net)\)(.*)?",
            " ",
            new_filename,
        )
        new_filename = new_filename.strip() + f".{ext}"
        src, dest = f"{path}/{file.name}", f"{path}/{new_filename}"
        os.rename(src, dest)
        print(f"[renamed] {file.name} --> {new_filename}")

    print("[done] all done!")


def main():
    args = sys.argv

    if len(args) >= 2:
        path = args[1]
    else:
        path = input("Enter the path to the target directory: ")

    if path.startswith("~"):
        path = os.path.expanduser(path)

    print(f"Target --> {path}")

    if os.path.exists(path) is False:
        print("File does not exist")
        exit(1)

    rename(path)


if __name__ == "__main__":
    main()
