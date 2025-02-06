from PIL import Image

input_file = 'captions.txt'
output_file = 'prompt.json'
output_file2 = 'prompt_20.json'

text = ""

with open(input_file, "r") as f:
    for line in f:
        file, prompt = line.split(': ')

        # Construct image path for checking dimensions
        image_path = f"C:/Users/RoscaMitrut/Desktop/mine/training/VOCdevkit/VOC2012/JPEGImages/{file}"

        # Check image dimensions
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                if width == 500 and height == 375:
                    # Add entry to JSON-like string
                    text += "{"
                    text += f"\"source\":\"VOCdevkit/VOC2012/SegmentationClass/{file[:-4]}.png\", \"target\":\"VOCdevkit/VOC2012/JPEGImages/{file}\", \"prompt\":\"{prompt.strip()}\""
                    text += "}\n"
        except FileNotFoundError:
            print(f"File not found: {image_path}")
        except Exception as e:
            print(f"Error processing {image_path}: {e}")

# Split the filtered entries into 80/20
lines = text.splitlines()
line_nr = len(lines)

split_index = int(line_nr * 0.8)

lines_80 = lines[:split_index]
lines_20 = lines[split_index:]

string_80 = "\n".join(lines_80)
string_20 = "\n".join(lines_20)

# Write to output files
with open(output_file, "w") as file1:
    file1.write(string_80)

with open(output_file2, "w") as file2:
    file2.write(string_20)
