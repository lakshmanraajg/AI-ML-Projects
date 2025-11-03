# 🧠 Handwritten Digits Recognition (MNIST)

A simple deep learning project to recognize handwritten digits (0–9) using the **MNIST dataset** and **TensorFlow/Keras**.  
This project trains a neural network to classify digits and can also make predictions on custom handwritten images.

---

## 🚀 Features

- Trains a **Neural Network (NN)** from scratch using the MNIST dataset  
- Achieves high accuracy on test data  
- Can **predict digits from custom handwritten images**  
- Saves and loads trained models for reuse  
- Simple and clean Python implementation  

---

## 🧩 Tech Stack

- **Python 3.x**
- **TensorFlow / Keras**
- **NumPy**
- **OpenCV**
- **Matplotlib**

---


---

## ⚙️ How It Works

1. **Dataset Loading:**  
   Loads the MNIST dataset (60,000 training + 10,000 test samples).

2. **Normalization:**  
   Each image pixel (0–255) is scaled to a range of 0–1 for better convergence.

3. **Model Architecture:**
   - Input Layer: Flattened 28×28 pixels  
   - Hidden Layer 1: 128 neurons, ReLU activation  
   - Hidden Layer 2: 128 neurons, ReLU activation  
   - Output Layer: 10 neurons, Softmax activation  

4. **Training:**  
   Uses `adam` optimizer and `sparse_categorical_crossentropy` loss for 3 epochs.

5. **Evaluation:**  
   Prints validation accuracy and loss.

6. **Prediction:**  
   Reads images from `digits/` folder and predicts the digit value.

---

## 🖼️ Preparing Custom Images

To test with your own digits:

1. Create a folder named `digits/` in your project directory.  
2. Add images named as `digit1.png`, `digit2.png`, etc.  
3. Ensure:
   - The images are **28×28 pixels** (or will be resized manually if needed).  
   - The digit is **black on white background**.  
   - Images are clear and centered.

---

## ▶️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Handwritten-Digits-Recognition.git
   cd Handwritten-Digits-Recognition
