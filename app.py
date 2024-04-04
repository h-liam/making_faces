from flask import Flask, send_file
from create_face import CreateFace

app = Flask(__name__)
test = CreateFace(400, 400)

@app.route("/")
def return_image():
  # Replace 'path/to/your/image.jpg' with the actual path to your image
  width, height = 400, 400
  
  test.random_color()
  test.drawing_random_circle(amount=1_000)
  test.save_image()
  image = test.throw_image()
  print(test)
  return send_file("image.jpg", mimetype='image/jpg')
  # return "Hello"
  
@app.route("/image/<int:amount>")
def load_image(amount:int=500):
  test.random_color()
  test.drawing_random_circle(amount=amount)
  test.save_image()
  return send_file("image.jpg", mimetype='image/jpg')

@app.route("/image/face")
def random_face():
  test.random_color()
  test.draw_face()
  test.save_image()
  return send_file("image.jpg")

if __name__ == "__main__":
  app.run(host='localhost', port=5000)
