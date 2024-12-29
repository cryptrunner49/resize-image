from PIL import Image

image = Image.open(input("image path: "))
print(f"current size: {image.size}")
resized_image = image.resize((int(input("the new width: ")), int(input("the new height: "))))
resized_image.save("./resized_image.png")