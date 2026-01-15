import cv2

file1path="./flag_7ae18c704272532658c10b5faad06d74.png"
file2path="./lemur_ed66878c338e662d3473f0d98eedbd0d.png"

foo = cv2.imread(file1path)
bar = cv2.imread(file2path)

key = cv2.bitwise_xor(foo, bar)

cv2.imwrite("xored.png", key)

cv2.imshow("xored data", key)

cv2.waitKey(0)
cv2.destroyAllWindows()