FILE_PATHS = [
    "/home/mori/Desktop/page_1024.txt",
    "/home/mori/Desktop/page_1025.txt",
    "/home/mori/Desktop/page_1026.txt",
    "/home/mori/Desktop/page_1027.txt",
    "/home/mori/Desktop/page_1028.txt",
]

OUTPUT_FILE = "/home/mori/Desktop/split_8bit_16bit_signed_native.txt"

def read_data(file_paths)->list:
    return [
        int(line.strip())
        for path in file_paths
        for line in open(path)
        if line.strip().isdigit()
    ]

def split_data(data)->list:
    return [
        (
            num >> 24,
            (num >> 16) & 0xFF,
            num & 0xFFFF,
            (num & 0xFFFF) if (num & 0x8000) == 0 else (num & 0xFFFF) - 0x10000,
        )
        for num in data
    ]

def write_results(file_path, split_data):
    with open(file_path, "w") as f:
        f.write(
            "High 8 bits | Mid 8 bits | Low 16 bits (unsigned) | Low 16 bits (signed)\n"
        )
        f.writelines(
            f"{row[0]} | {row[1]} | {row[2]} | {row[3]}\n" for row in split_data
        )

def main():
    data = read_data(FILE_PATHS)
    split_data_signed = split_data(data)
    write_results(OUTPUT_FILE, split_data_signed)
    print("Done")
    
if __name__ == "__main__":
    main()
