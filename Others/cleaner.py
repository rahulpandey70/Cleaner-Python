import os

def createIfNotExits(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

if __name__ == "__main__":

    files = os.listdir()
    #print(files)

    createIfNotExits('Images')
    createIfNotExits('Docs')
    createIfNotExits('Musics')
    createIfNotExits('Others')

    imgExts = [".png",".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    #print(images)

    docExts = [".txt",".docx",".doc",".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    #print(docs)

    musicExts = [".mp3",".mp4"]
    musics = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]
    #print(musics)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if(ext not in imgExts) and (ext not in docExts) and (ext not in musicExts) and os.path.isfile(file):
            others.append(file)
    print(others)

    move("Images",images)
    move("Docs",docs)
    move("Musics",musics)
    move("Others",others)