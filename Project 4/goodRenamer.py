import os

def renamer():
    img = 0
    docs = 0
    Videos = 0
    path1 = "C:\\Users\\user\\Project 5.0\\img\\"
    path2 = "C:\\Users\\user\\Project 5.0\\docs\\"
    path3 = "C:\\Users\\user\\Project 5.0\\videos\\"

    for filename1 in os.listdir(path1):
        names1 = f"picture {img}.jpg"
        src1 = path1 + filename1
        dest1 = path1 + names1
        
        os.rename(src1,dest1)
        img = img + 1

    for filename2 in os.listdir(path2):
        names2 = f"Document {docs}.pdf"
        src2 = path2 + filename2
        dest2 = path2 + names2
        
        os.rename(src2,dest2)
        docs = docs + 1

    for filename3 in os.listdir(path3):
        names3 = f"Video {Videos}.mkv"
        src3 = path3 + filename3
        dest3 = path3 + names3
        
        os.rename(src3,dest3)
        Videos = Videos + 1
    
if __name__ == "__main__":
    renamer()

# rename 300 files/images/songs/videos/docs using goodRenamer