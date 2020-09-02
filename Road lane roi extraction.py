import matplotlib.pyplot as plt
import numpy as np
import cv2

# The matplotlib actually works in images in the form of matrices...
# we can see in the graph, the x axis from top to bottom as 0 to x values.

image = cv2.imread('road.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


# to focus on the region of interest(ROI) we mask the irrelevent data in the image
print(image.shape)
height = image.shape[0]
width = image.shape[1]

roi_vertices = [
    (0,height),
    (width/2,height/2),
    (width,height)
]

# masking all irrelevent stuff...
def roi(img,vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,)* channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

cropped_image = roi(image,
                    np.array([roi_vertices],np.int32))

title = ['Original','ROI image']
images = [image,cropped_image]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])

plt.show()

