# 🖼️ BgRemoveServer

A lightweight **background removal server** that processes images and removes backgrounds automatically using AI models.  
This project provides a simple backend service that can be integrated into web apps, mobile apps, or automation workflows to generate transparent images from uploaded photos.

---

## 🚀 Features

- 🧠 AI-powered background removal
- ⚡ Fast server-side processing
- 📤 Image upload API
- 🖼️ Transparent PNG output
- 🔌 Easy integration with frontend apps
- 🛠️ Simple setup and deployment

---

## 📦 Tech Stack

- **Backend:** Node.js
- **Framework:** Express.js
- **Image Processing:** AI background removal model
- **API:** RESTful API

---

## 📂 Project Structure
```project structure
BgRemoveServer
│
├── src/
│ ├── controllers/
│ ├── routes/
│ ├── services/
│ └── utils/
│
├── uploads/
├── outputs/
├── package.json
└── server.js
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Fa-had/BgRemoveServer.git
cd BgRemoveServer
```
### Install dependencies
```bash
npm install
```
### Start the server
```bash
npm start
```
#### Development mode
```bash
npm dev
```
---

## 🧪 API Usage
### Endpoint
```bash
POST /remove-bg
```
### Request
- **Content-Type:** multipart/form-data
- **Body parameter:**

| Name  | Type | Description      |
| ----- | ---- | ---------------- |
| image | file | Image to process |

### Example using curl
```bash
curl -X POST http://localhost:3000/remove-bg \
  -F "image=@photo.jpg" \
  -o output.png
```
---

## 📸 Example Workflow
1. Upload an image to the API
2. Server processes the image using an AI model
3. Background is removed
4. Transparent PNG is returned

---

## ⚙️ Configuration

You can configure the server using environment variables.
### Example `.env` file:
```bash
PORT=3000
UPLOAD_DIR=uploads
OUTPUT_DIR=outputs
MAX_FILE_SIZE=5MB
```
---

## 📌 Supported Image Formats
### Input formats:
- JPG
- JPEG
- PNG
- WEBP
### Output format:
- PNG (Transparent background)

---

## 🤝 Contributing

Contributions are welcome!
1. Fork the repository
2. Create a new branch
```bash
git checkout -b feature/new-feature
```
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👤 Author
**Fahad**
GitHub:
https://github.com/Fa-had
