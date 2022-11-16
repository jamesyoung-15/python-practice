import whisper

model = whisper.load_model("base")
print("Enter file name: ")
filename = input()
print("Enter output name: ")
output_name = input()
result = model.transcribe(filename)
with open(output_name,'w') as f:
    f.write(result["text"])

