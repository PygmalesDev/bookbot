DIR: str = "books/"
FILE_NAME: str = "frankenstein.txt"

def main():
    text = get_content(FILE_NAME)
    print(f"\n------- READING: {DIR}{FILE_NAME} -------")
    print(f"This book contains: {count_words(text)} words; Character analysis:", end="")
    chars = count_chars(text)
    chars = sort_dict(chars)
    for i in range(len(chars)):
        entry = chars[i]
        raw = "↵" if entry["char"] == "\n" else entry["char"]
        tab = "\t" if entry["num"] >= 10 else "\t\t"
        if i%5 == 0:
            print("\n| ", end="")
        print(f'{i+1}.\t [{raw}]: {entry["num"]}{tab}| ', end="")
        i += 1
    print()
    print("---------------- FINISHED ----------------")

def get_content(path: str) -> str:
    try:
        with open(f"{DIR}{path}") as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Could not read file from provided path: {DIR}{path}")

def count_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict[str, int]:
    chars = {}
    for ltr in text.lower():
        if ltr not in chars: 
            chars[ltr] = 0
        chars[ltr] += 1
    return chars

def sort_dict(orig: dict) -> list[dict]:
    sort_list = []
    for ltr, num in orig.items():
        sort_list.append({"char": ltr, "num": num})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

def sort_on(orig: dict) -> int:
    return orig["num"]


main()
