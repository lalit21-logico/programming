import cv2
import time
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Run keypoint detection')
parser.add_argument("--device", default="cpu", help="Device to inference on")
parser.add_argument("--image_file", default="sample.webp", help="Input image")

args = parser.parse_args()


MODE = "COCO"

if MODE is "COCO":
    protoFile = "pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "pose/coco/pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [[1, 0], [1, 2], [1, 5], [2, 3], [3, 4], [5, 6], [6, 7], [1, 8], [
        8, 9], [9, 10], [1, 11], [11, 12], [12, 13], [0, 14], [0, 15], [14, 16], [15, 17]]

elif MODE is "MPI":
    protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
    POSE_PAIRS = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [
        1, 14], [14, 8], [8, 9], [9, 10], [14, 11], [11, 12], [12, 13]]


frame = cv2.imread(args.image_file)
frameCopy = np.copy(frame)
frameWidth = frame.shape[1]
frameHeight = frame.shape[0]
threshold = 0.1

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

if args.device == "cpu":
    net.setPreferableBackend(cv2.dnn.DNN_TARGET_CPU)
    print("Using CPU device")
elif args.device == "gpu":
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    print("Using GPU device")

t = time.time()
# input image dimensions for the network
inWidth = 368
inHeight = 368
inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                (0, 0, 0), swapRB=False, crop=False)

net.setInput(inpBlob)

output = net.forward()
print("time taken by network : {:.3f}".format(time.time() - t))

H = output.shape[2]
W = output.shape[3]

# Empty list to store the detected keypoints
points = []

for i in range(nPoints):
    # confidence map of corresponding body's part.
    probMap = output[0, i, :, :]

    # Find global maxima of the probMap.
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    # Scale the point to fit on the original image
    x = (frameWidth * point[0]) / W
    y = (frameHeight * point[1]) / H

    if prob > threshold:
        cv2.circle(frameCopy, (int(x), int(y)), 4, (0, 255, 255),
                   thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frameCopy, "{}".format(i), (int(x), int(
            y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

        # Add the point to the list if the probability is greater than the threshold
        points.append((int(x), int(y)))
        print(x, ':::::::::::', y)

    else:
        points.append(None)

print([x[1] for x in points])
print(points[1])
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (400, 420)
fontScale = 1
fontColor = (255, 255, 255)
lineType = 2
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
part_1 = [x[1] for x in points]
if(part_1[9]+8 >= part_1[12] and part_1[9]-8 <= part_1[12]):
    print('yes')
    if(part_1[8]+8 >= part_1[11] and part_1[8]-8 <= part_1[11]):
        print('yes')
        if(part_1[2]+8 >= part_1[5] and part_1[2]-8 <= part_1[5]):
            print('yes')
            if(part_1[3]+8 >= part_1[6] and part_1[3]-8 <= part_1[6]):
                print('yes')
                if(part_1[4]+8 >= part_1[7] and part_1[4]-8 <= part_1[7]):
                    if(part_1[4] < part_1[3] < part_1[2] < part_1[8] < part_1[9] and part_1[7] < part_1[6] < part_1[5] < part_1[11] < part_1[12]):
                        print("tadadsan")
                        cv2.putText(frameCopy, 'tadadsan', bottomLeftCornerOfText,
                                    font, fontScale, fontColor, lineType)


# Draw Skeleton
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
        cv2.circle(frame, points[partA], 4, (0, 0, 255),
                   thickness=-1, lineType=cv2.FILLED)

cv2.imshow('Output-Keypoints', frameCopy)
cv2.imshow('Output-Skeleton', frame)


cv2.imwrite('Output-Keypoints.jpg', frameCopy)
cv2.imwrite('Output-Skeleton.jpg', frame)

print("Total time taken : {:.3f}".format(time.time() - t))

cv2.waitKey(0)
