import cv2

# Load the image
image = cv2.imread("../Images/car.jpg")
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    print("Image loaded successfully!")
    print("Image dimensions:", image.shape)

    # Display the image
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
