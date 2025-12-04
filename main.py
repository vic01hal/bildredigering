from PIL import Image, ImageEnhance

mona = Image.open("img/mona.png")
mona = ImageEnhance.Brightness(mona).enhance(10)
mona.save("processed/mona.png")

beans = Image.open("img/beans.png")
beans = ImageEnhance.Sharpness(beans).enhance(100)
beans.save("processed/beans.png")

baby = Image.open("img/baby.png")
baby = ImageEnhance.Contrast(baby).enhance(0.3)
baby.save("processed/baby.png")
