import cv2

def zoom_image(image, zoom_factor):
    height, width = image.shape[:2]
    
    
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    resized_image = cv2.resize(image, (new_width, new_height))


    start_x = (new_width - width) // 2
    start_y = (new_height - height) // 2
    

    cropped_image = resized_image[start_y:start_y + height, start_x:start_x + width]

    return cropped_image

def main():
    image_path = input("Enter image path: ")
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found☹️. Please try again.")
        return

    try:
        zoom_factor = float(input("Enter zoom factor (more than 1): "))
        if zoom_factor <= 1:
            print("I said more than 1😡")
            return
    except ValueError:
        print("Invalid input for zoom factor. Please enter a number.")
        return

    zoomed_image = zoom_image(image, zoom_factor)


    cv2.imshow('Zoomed Image', zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()