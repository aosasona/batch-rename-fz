import os


def rename(path: str):
    path = path.strip("/")
    for file in os.scandir(path):
        if file.is_dir() == True:
            rename(file.path)
            continue
        ext = file.name.split(".").pop()
        filename_arr = file.name.split("_")
        new_filename = " ".join(filename_arr[:len(filename_arr)-1]) + f".{ext}"
        src, dest = f"{path}/{file.name}", f"{path}/{new_filename}"
        os.rename(src, dest)
        print(f"--> Renamed {src} to {dest}")

    print("All done!")


def main():
    path = input("Enter the path to the target directory: ")

    print(f"Attempting to read path: {path}")

    if os.path.exists(path) == False:
        print("File does not exist")
        exit()

    rename(path)

if __name__ == "__main__":
    main()
