input_file = 'captions.txt'

output_file = 'prompt.json'
output_file2 = 'prompt20.json'

text=""

with open(input_file, "r") as f:
    for line in f:
        file,prompt = line.split(': ')

        text += "{"
        text += f"\"source\": \"VOCdevkit/VOC2012/JPEGImages/{file}\",\"target\":\"VOCdevkit/VOC2012/SegmentationClass/{file[:4]}.png\",\"prompt\":\"{prompt.strip()}\""
        text += "}\n"

lines = text.splitlines()

line_nr = len(lines)

split_index = int(line_nr*0.8)

lines_80=lines[:split_index]
lines_20=lines[split_index:]

string_80 = "\n".join(lines_80)
string_20 = "\n".join(lines_20)

with open("prompt.json", "w") as file1:
    file1.write(string_80)

with open("prompt_20.json", "w") as file2:
    file2.write(string_20)