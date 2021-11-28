import os

def createIFNOTExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")
files = os.listdir()
files.remove("Main.py")
print(files)
createIFNOTExists('Images')
createIFNOTExists('Docs')
createIFNOTExists('Media')
createIFNOTExists('Others')
print("\n")
imgExts = [".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower()  in imgExts]
print(images)
print("\n")
docExts = [".txt",".docx",".doc",".pdf",".ppt",".cvs",".pptx"]
docs = [file for file in files if os.path.splitext(file)[1].lower()  in docExts]
print(docs)
print("\n")
mediaExts = [".mkv",".m4a",".mp3",".mp4"]
medias = [file for file in files if os.path.splitext(file)[1].lower()  in mediaExts]
print(medias)
print("\n")
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in mediaExts) and (ext not in imgExts) and (ext not in docExts) and os.path.isfile(file):
        others.append(file)
print(others)
print("\n") 

move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Others",others)