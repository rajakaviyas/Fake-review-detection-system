# 🛡️ FakeGuard – An Intelligent Machine Learning Framework for Detecting Fraudulent E-Commerce Reviews

FakeGuard is a Machine Learning-powered web application that detects fraudulent e-commerce product reviews while ensuring that **only verified customers can submit reviews** using a **Purchase-Linked Review Token (PLRT)**.

Unlike traditional fake review detection systems, FakeGuard combines **purchase verification** and **machine learning-based review analysis** to improve the authenticity and reliability of online product reviews. This dual-layer approach helps prevent spam, fake reviews, and unauthorized review submissions, thereby increasing customer trust in e-commerce platforms.

---

## 🚀 Key Features

* 🔐 **Purchase-Linked Review Token (PLRT)** ensures that only verified customers can submit reviews.
* 🤖 Detects fake and genuine reviews using Machine Learning.
* 📝 Performs intelligent review text analysis.
* ⚡ Provides fast and accurate review classification.
* 🌐 Interactive web application developed using Flask.
* 📱 Simple, clean, and responsive user interface.
* 🛒 Improves trustworthiness of product reviews on e-commerce platforms.
* 📊 Efficient review processing with real-time prediction.

---

## 🏗️ System Workflow

1. Customer purchases a product.
2. The system generates a unique **Purchase-Linked Review Token (PLRT)**.
3. The customer enters the PLRT before submitting a review.
4. The system verifies the authenticity of the token.
5. The submitted review is analyzed using the Machine Learning model.
6. The review is classified as **Genuine** or **Fake**.
7. The prediction result is displayed through the web interface.

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Database

* MySQL

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
FakeGuard/
│
├── static/                 # CSS, JavaScript, Images
├── templates/              # HTML Templates
├── dataset/                # Training Dataset
├── model/                  # Trained Machine Learning Model
├── app.py                  # Flask Application
├── requirements.txt        # Project Dependencies
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/FakeGuard.git
```

### Navigate to the project folder

```bash
cd FakeGuard
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

### Open in your browser

```text
http://127.0.0.1:5000
```

---

## 🎯 Project Objective

The primary objective of FakeGuard is to improve the reliability of online product reviews by combining **Purchase-Linked Review Token (PLRT)** verification with **Machine Learning-based fake review detection**.

This approach ensures that:

* Only verified customers can submit reviews.
* Fraudulent and spam reviews are detected automatically.
* Customer trust in e-commerce platforms is increased.
* Businesses receive more authentic customer feedback.

---

## 💡 Applications

* E-commerce Platforms
* Online Shopping Websites
* Product Review Systems
* Marketplace Applications
* Customer Feedback Analysis

---

## 🔮 Future Enhancements

* Deep Learning models for higher prediction accuracy.
* Real-time review monitoring.
* REST API integration.
* Cloud deployment using AWS or Azure.
* Multi-language review analysis.
* Sentiment analysis integration.
* Mobile application support.
* Enhanced fraud detection using NLP and Transformer models.

---

## 📄 License

This project was developed for educational and academic purposes.

---

## 👩‍💻 Author

**Rajakaviya S**

**Bachelor of Engineering – Computer Science and Engineering**

**Skills:** Python • Java • SQL • Machine Learning • Flask • HTML • CSS • JavaScript

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
