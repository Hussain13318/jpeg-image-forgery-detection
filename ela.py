
import cv2
import os

COMPRESSION_VALUE = 95
MULTIPLIER = 30

def ela_algorithm(image_path, output_path):
    # Read original image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Cannot read", image_path)
        return

    # Recompress image as JPEG
    cv2.imwrite(
        "compressed.jpg",
        img,
        [cv2.IMWRITE_JPEG_QUALITY, COMPRESSION_VALUE]
    )

    compressed_img = cv2.imread("compressed.jpg")

    # Calculate absolute pixel differences
    diff = cv2.absdiff(img, compressed_img)

    # Increase differences to make them visible
    ela_result = cv2.convertScaleAbs(
        diff,
        alpha=MULTIPLIER
    )

    # Save ELA result
    cv2.imwrite(output_path, ela_result)

    print("ELA result saved:", output_path)


# Analyze original photograph
ela_algorithm(
    "original.jpg",
    "result_original_img.jpg"
)

# Analyze manipulated photograph
ela_algorithm(
    "photoshopped_img.jpg",
    "result_edited_img.jpg"
)

print("\nELA analysis completed!")
