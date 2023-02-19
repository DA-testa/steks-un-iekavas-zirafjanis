# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # pass
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
            # if not are_matching(last_open.char, next):
            #     return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position 
    return "Success"

def main():
    lmao = input("xd \n")
    text = input()
    mismatch = find_mismatch(text)
    # if isinstance(mismatch, int):
    #     print(f"{mismatch}")
    # else:
    print(mismatch)


if __name__ == "__main__":
    main()
