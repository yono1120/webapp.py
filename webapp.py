import streamlit as st
from PIL import Image
import io

def resize_image(img, ratio, quality):
    """
    Resize an image by the given ratio and save it with the specified quality.

    Args:
    - img: PIL.Image object
    - ratio: float, resize ratio (e.g., 0.5 for half the size)
    - quality: int, JPEG quality level (1-100)

    Returns:
    - resized_img: PIL.Image object
    """
    width, height = img.size
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    
    buffer = io.BytesIO()
    resized_img.save(buffer, format="JPEG", quality=quality)
    return buffer.getvalue()

st.title("画像リサイザ")

uploaded_file = st.file_uploader("画像をアップロードしてください (.png, .jpeg)", type=["png", "jpeg", "jpg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    
    # Display original image with its dimensions
    st.write("オリジナル画像:")
    st.image(img, caption=f"オリジナルサイズ: {img.width}x{img.height}")
    
    st.write("画像の縮小比率と画質を選択してください:")
    
    # Slider to adjust resize ratio
    ratio = st.slider("縮小比率", 0.1, 1.0, 1.0, 0.1)
    
    # Slider to adjust jpeg quality
    quality = st.slider("JPEG 画質 (1-100)", 1, 100, 85)
    
    # Resize the image
    resized_img_bytes = resize_image(img, ratio, quality)
    
    # Display resized image with its dimensions
    st.write("リサイズ後の画像:")
    st.image(resized_img_bytes, caption=f"リサイズ後のサイズ: {int(img.width * ratio)}x{int(img.height * ratio)}")
