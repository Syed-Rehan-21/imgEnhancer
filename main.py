# importing modules
import streamlit as st
from rembg import remove
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
import base64

# page configurations
st.set_page_config(page_title="Image Enhancer")
st.subheader("Upload an image")

col1, col2 = st.columns(2)
image = st.file_uploader(":arrow_up_small:  ",type=["png", "jpg", "jpeg"])

# Download the enhanced image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(image):
    image = Image.open(image)
    #adding sidebar
    st.sidebar.header("Editing panel")
    col1.write("Original :camera:")
    col1.image(image)

    setting_sharp = st.sidebar.slider("Sharpness")
    setting_color = st.sidebar.slider("Colour")
    setting_brightness = st.sidebar.slider("Brightness")
    setting_contrast = st.sidebar.slider("Contrast")
    setting_flip_image = st.sidebar.selectbox("Flip Image", options=("FLIP-TOP-BOTTOM", "FLIP-LEFT-RIGHT"))

    # writing filters code
    st.sidebar.write("Filters")
    filter_black_and_white = st.sidebar.checkbox("Black & white")
    bgremove=st.sidebar.checkbox("BackGroundRemove")
    filter_blur = st.sidebar.checkbox("Blur")

    if filter_blur:
        filter_blur_strength = st.sidebar.slider("Select Blur strength")

    # checking setting_sharp value
    if setting_sharp:
        sharp_value = setting_sharp
    else:
        sharp_value = 0

    # checking color
    if setting_color:
        set_color = setting_color
    else:
        set_color = 1

    # checking brightness
    if setting_brightness:
        set_brightness = setting_brightness
    else:
        set_brightness = 1

    # checking contrast
    if setting_contrast:
        set_contrast = setting_contrast
    else:
        set_contrast = 1

    # checking setting_flip_image
    flip_direction = setting_flip_image

    # implementing sharpness
    sharp = ImageEnhance.Sharpness(image)
    edited_img = sharp.enhance(sharp_value)

    # implementing colors
    color = ImageEnhance.Color(edited_img)
    edited_img = color.enhance(set_color)

    # implementing brightness
    brightness = ImageEnhance.Brightness(edited_img)
    edited_img = brightness.enhance(set_brightness)

    # implementing contrast
    contrast = ImageEnhance.Contrast(edited_img)
    edited_img = contrast.enhance(set_contrast)

    # implementing flip direction
    if flip_direction == "FLIP-TOP_BOTTOM":
        edited_img = edited_img.transpose(Image.FLIP-TOP-BOTTOM)
    elif flip_direction == "FLIP-LEFT-RIGHT":
        edited_img = edited_img.transpose(Image.FLIP-LEFT-RIGHT)
    else:
        pass

    # implementing filters
    if filter_black_and_white:
        edited_img = edited_img.convert(mode='L')

    if filter_blur:
        if filter_blur_strength:
            set_blur = filter_blur_strength
            edited_img = edited_img.filter(ImageFilter.GaussianBlur(set_blur))
    if bgremove:
        edited_img= remove(edited_img)

    col2.write("Edited")
    col2.image(edited_img)
    st.download_button("Download :arrow_down_small: ", convert_image(edited_img), "output.png", "image/png")

if image is not None:
    fix_image(image)

    