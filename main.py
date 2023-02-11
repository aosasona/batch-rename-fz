import os
import sys


def rename(path: str):
    for file in os.scandir(path):
        if file.is_dir() == True:
            rename(file.path)
            continue

        ext = file.name.split(".").pop()
        filename_arr = file.name.split("_")

        if len(filename_arr) <= 1:
            print("[done] nothing to rename here... :)")
            exit(0)

        new_filename = " ".join(filename_arr[:len(filename_arr)-1]) + f".{ext}"
        src, dest = f"{path}/{file.name}", f"{path}/{new_filename}"
        os.rename(src, dest)
        print(f"[renamed] {file.name} --> {new_filename}")

    print("[done] all done!")


def main():
    args = sys.argv

    if len(args)>= 2:
        path = args[1]
    else:
        path = input("Enter the path to the target directory: ")


    if path.startswith("~"):
        path = os.path.expanduser(path)

    print(f"Target --> {path}")

    if os.path.exists(path) == False:
        print("File does not exist")
        exit(1)

    rename(path)

if __name__ == "__main__":
    main()
