import cv2

CAMERA_INDEX = 0
MIN_AREA = 1000
THRESHOLD_VALUE = 25


# ==============================
# START CAMERA
# ==============================

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    print("Try changing CAMERA_INDEX from 0 to 1.")
    exit()


print("Motion Detection System Started")
print("Move something in front of the camera.")
print("Press Q to quit.")


# ==============================
# PREVIOUS FRAME
# ==============================

previous_gray = None


# ==============================
# MAIN LOOP
# ==============================

while True:

    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # =================================
    # TOPIC 1: IMAGE OPERATIONS
    # =================================

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Reduce image noise
    gray = cv2.GaussianBlur(
        gray,
        (21, 21),
        0
    )


    # =================================
    # FIRST FRAME
    # =================================

    if previous_gray is None:

        previous_gray = gray

        cv2.putText(
            frame,
            "Initializing...",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.imshow(
            "Motion Detection System",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        continue


    # =================================
    # TOPIC 2: IMAGE SEGMENTATION
    # =================================

    # Compare current frame with previous frame
    difference = cv2.absdiff(
        previous_gray,
        gray
    )

    # Convert difference into binary image
    _, mask = cv2.threshold(
        difference,
        THRESHOLD_VALUE,
        255,
        cv2.THRESH_BINARY
    )

    # Expand white areas slightly
    mask = cv2.dilate(
        mask,
        None,
        iterations=2
    )


    # =================================
    # TOPIC 3: MOTION DETECTION
    # =================================

    # Find moving regions
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    motion_detected = False


    # Check each detected region
    for contour in contours:

        # Calculate area
        area = cv2.contourArea(contour)

        # Ignore very small changes
        if area < MIN_AREA:
            continue


        # Get bounding box
        x, y, w, h = cv2.boundingRect(
            contour
        )


        # Draw bounding box
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )


        # Display label
        cv2.putText(
            frame,
            "Motion Detected",
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )


        motion_detected = True


    # =================================
    # MOTION STATUS
    # =================================

    if motion_detected:

        status = "Motion Detected"
        status_color = (0, 0, 255)

    else:

        status = "No Motion"
        status_color = (255, 255, 255)


    cv2.putText(
        frame,
        status,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        status_color,
        2
    )


    # =================================
    # DISPLAY WINDOWS
    # =================================

    cv2.imshow(
        "Motion Detection System",
        frame
    )

    cv2.imshow(
        "Motion Mask",
        mask
    )


    # =================================
    # SAVE CURRENT FRAME
    # =================================

    previous_gray = gray


    # =================================
    # EXIT
    # =================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==============================
# CLEANUP
# ==============================

cap.release()

cv2.destroyAllWindows()

print("Motion Detection System Closed")