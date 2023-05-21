import cv2

src = cv2.imread("nur.jpg", cv2.IMREAD_UNCHANGED)

scale_percent = 50

new_width = int(src.shape[1] * scale_percent / 100)  # {resize the photo width wise}
new_height = int(src.shape[0] * scale_percent / 100)  # {resize the photo height wise}

dsize = (new_width, new_height)

output = cv2.resize(src, dsize)
cv2.imwrite('newImage.png', output)
cv2.waitKey(0)
