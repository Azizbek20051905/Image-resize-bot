from PIL import Image

def format_img(file, file_name):
    img = Image.open(file)
    n = img.resize((300,400))
    name = f"{file_name}.jpg"
    n.save(name)
    return name