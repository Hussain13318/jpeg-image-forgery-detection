import cv2
import numpy as np

original = cv2.imread("result_original_img.jpg")
edited = cv2.imread("result_edited_img.jpg")

if original is None or edited is None:
    print("Error: ELA result images not found.")
    exit()

edited = cv2.resize(edited, (original.shape[1], original.shape[0]))

cv2.putText(original, "Original ELA", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

cv2.putText(edited, "Edited ELA", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

comparison = np.hstack((original, edited))

cv2.imwrite("comparison.jpg", comparison)

print("Comparison image saved successfully!")