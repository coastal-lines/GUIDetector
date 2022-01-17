import cv2

class DrawMethods:
    def DrawRectangleByCoordinates(image, x, y, w ,h):
        point1 = (x, y)
        point2 = (x + w, y + h)
        cv2.rectangle(image, point1, point2, (0, 255, 0), 2)

    def DrawRectangleByContours(contours, image):
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            point1 = (x, y)
            point2 = (x + w, y + h)
            cv2.rectangle(image, point1, point2, (0, 255, 0), 1)

    def DrawRectangleByPoints(image, point1, point2):
        cv2.rectangle(image, point1, point2, (0, 255, 0), 2)

    def DrawRectangleByPointsAndPrintText(image, point1, point2, text):
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(image, text, (point2[0], point1[1]), font, 1, (0, 255, 0), 1)
        cv2.rectangle(image, point1, point2, (0, 255, 0), 2)

    def DrawRectangleByBox(box, image):
        cv2.rectangle(image, [box], (0, 255, 0), 1)