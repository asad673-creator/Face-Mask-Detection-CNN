# 😷 Face Mask Detection

A real-time **Face Mask Detection** web application built using **Flask** and **TensorFlow/Keras**.

The application uses the user's webcam to capture an image and passes it through a trained deep learning model to determine whether the person is **wearing a face mask** or **not wearing a face mask**.

## 🚀 Features

* 📷 Live webcam access
* 📸 Capture images directly from the browser
* 🧠 TensorFlow/Keras deep learning model
* 🔍 Face mask classification
* 📐 Image preprocessing to **160 × 160**
* 📊 Prediction confidence
* 🌐 Flask-based web interface

## 🧠 Model

The trained model is stored as:

```text
Face-mask-detection.keras
```

The model uses two classes:

| Class | Label        |
| ----- | ------------ |
| `0`   | With Mask    |
| `1`   | Without Mask |

## 🔄 How It Works

```text
Webcam
   ↓
Capture Image
   ↓
Convert Image
   ↓
Resize to 160 × 160
   ↓
Preprocessing
   ↓
Face-mask-detection.keras
   ↓
Prediction
   ↓
With Mask / Without Mask
```

## 📁 Project Structure

```text
Face-Mask-Detection/
│
├── app.py
├── Face-mask-detection.keras
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 🛠️ Technologies Used

* Python
* Flask
* TensorFlow
* Keras
* NumPy
* Pillow
* HTML
* CSS
* JavaScript
* Web Camera API

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd Face-Mask-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Allow camera access when prompted.

## 📸 Usage

1. Open the application.
2. Allow access to your webcam.
3. Position your face in front of the camera.
4. Click **Capture Photo**.
5. The image is processed and resized to **160 × 160**.
6. The trained model predicts the result.
7. The application displays:

   * **With Mask**
   * **Without Mask**
   * Prediction confidence

## 📦 Requirements

Example `requirements.txt`:

```text
Flask
tensorflow
numpy
Pillow
```

## ⚠️ Notes

The model expects input images of **160 × 160 pixels**.

The application is intended as an educational deep learning project demonstrating how a trained image classification model can be integrated into a Flask web application.

## 🔮 Future Improvements

* Face detection before classification
* Real-time continuous mask detection
* Multiple face detection
* Prediction history
* Improved UI/UX
* Mobile-friendly interface
* Deployment to a cloud platform
* Add model performance metrics

## 👨‍💻 Author

**Asad**

A deep learning project focused on integrating computer vision models with web applications.
