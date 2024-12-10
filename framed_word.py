string= input("Word: ")
frame_width = 30
space = (frame_width - len(str)) // 2 - 1

print(
    "*" * frame_width
    + "\n"
    + "*"
    + " " * space
    + string
    + " " * (frame_width - len(string) - space - 2)
    + "*"
    + "\n"
    + "*" * frame_width
)