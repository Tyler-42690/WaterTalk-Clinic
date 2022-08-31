import cv2

def capture_from_video():
    img_counter = 0
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow("test",frame)
        else:
            break
        key = cv2.waitKey(1)
        if key%256 == 27: #ESC character pressed
            print("Escape hit, closing...")
            break
        elif key%256 == 32: #SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print("{} written...".format(img_name))
            img_counter+=1
        cam.release()
        cv2.destroyAllWindows()

def main():
    capture_from_video()

if __name__ == "__main__":
    main()
