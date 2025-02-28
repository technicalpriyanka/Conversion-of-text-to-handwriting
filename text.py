from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

def text_to_handwriting(text, output_path="handwriting.png", font_size=40):
    width, height = 800, 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("Seguihl.ttf", font_size)  # Use a handwriting-style font
    except IOError:
        print("Font not found, using default font.")
        font = ImageFont.load_default()

    # Draw text on image
    draw.text((50, 50), text, font=font, fill="black")

    # Convert to OpenCV format and add noise for handwriting effect
    img_cv = np.array(image)
    noise = np.random.randint(0, 50, img_cv.shape, dtype='uint8')
    img_noisy = cv2.addWeighted(img_cv, 0.9, noise, 0.1, 0)

    cv2.imwrite(output_path, img_noisy)
    print(f"Handwriting image saved as {output_path}")

# Example usage
text_to_handwriting("Inner peace, dear Parth, is not the absence of challenges but the presence of unwavering equanimity in all situations. It is the stillness of the mind, where neither joy nor sorrow can shake one’s essence. As I have told Arjuna in the Bhagavad Gita:", "handwriting_output.png")
