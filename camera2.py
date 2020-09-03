import mysql.connector
import base64
import io
import PIL.Image
import cv2


videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()


with open('NewPicture.jpg', 'rb') as f:
    photo = f.read()
encodestring = base64.b64encode(photo)
db= mysql.connector.connect(user="#",password="#",host="34.123.152.95",database="images")
mycursor=db.cursor()
sql = "insert into img values(%s)"
mycursor.execute(sql,(encodestring,))
db.commit()
sql1="select * from img"
mycursor.execute(sql1)
data = mycursor.fetchall()
data1=base64.b64decode(data[0][0])
file_like=io.BytesIO(data1)
img=PIL.Image.open(file_like)
img.show()
db.close()
