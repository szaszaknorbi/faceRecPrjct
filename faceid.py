import cv2
import face_recognition


camera = cv2.VideoCapture(0)

image_1 = face_recognition.load_image_file("person_1.jpg")
image_1_encoding = face_recognition.face_encodings(image_1)[0]

ret, frame = camera.read()

face_locations = face_recognition.face_locations(frame)

face_encodings = face_recognition.face_encodings(frame, face_locations)

for face_encoding in face_encodings:

    match = face_recognition.compare_faces([image_1_encoding], face_encoding)
if match[0]:
            print("Matched")

cv2.imshow("Frame", frame)
key = cv2.waitKey(1) & 0xFF
if key == ord("q"):
    cv2.destroyAllWindows()
    camera.release()

unknown_face_encoding = face_recognition.face_encodings(unknown_face_image)[0]
results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

if True in results:

    index = results.index(True)
    print(f"Match found: {known_face_names[index]}")
else:
    print("No match found")

