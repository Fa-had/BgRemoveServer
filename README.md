# BgRemoveServer

A high-performance background removal service built with FastAPI. Remove image backgrounds with ease using state-of-the-art AI models.

## Features

- 🎨 **Automatic Background Removal** - Uses advanced AI models via `rembg` library
- 🔐 **API Key Authentication** - Secure endpoints with API key verification
- 🌐 **CORS Support** - Cross-origin resource sharing enabled for web clients
- 📦 **RESTful API** - Clean, intuitive API endpoints
- ☁️ **Cloud Ready** - Deploy to Railway or Vercel with included configuration
- 🏥 **Health Checks** - Built-in health check endpoint for monitoring
- 🖼️ **PNG Output** - Transparent PNG format with RGBA color space

## Prerequisites

- Python 3.8 or higher
- pip or poetry for dependency management
- At least 2GB RAM for AI model inference

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Fa-had/BgRemoveServer
cd BgRemoveServer
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### API Keys

Edit `main.py` to define your API keys:

```python
API_KEYS = {"key1", "key2", "key3"}
```

### CORS Origins

Update the allowed origins for CORS:

```python
ALLOWED_ORIGINS = ["http://localhost:3000"]
```

## Running the Server

### Local Development

```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

### Access Interactive Documentation

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## API Endpoints

### 1. Remove Background

**Endpoint:** `POST /remove-background/`

**Headers:**

```
Authorization: <your-api-key>
```

**Request:**

- Multipart form data with image file

**Response:**

```json
{
  "filename": "uuid-string.png"
}
```

**Example (cURL):**

```bash
curl -X POST "http://localhost:8000/remove-background/" \
  -H "Authorization: key1" \
  -F "file=@image.jpg"
```

### 2. Download Processed Image

**Endpoint:** `GET /download/{filename}`

**Response:** PNG image file with transparent background

**Example (cURL):**

```bash
curl "http://localhost:8000/download/uuid-string.png" \
  -o processed-image.png
```

### 3. Health Check

**Endpoint:** `GET /ping`

**Response:**

```json
{
  "res": "pong",
  "version": "0.100.0",
  "time": 1234567890.123
}
```

## Workflow Example

```bash
# 1. Upload image for background removal
RESPONSE=$(curl -X POST "http://localhost:8000/remove-background/" \
  -H "Authorization: key1" \
  -F "file=@photo.jpg")

# Extract filename from response
FILENAME=$(echo $RESPONSE | grep -o '"filename":"[^"]*' | cut -d'"' -f4)

# 2. Download processed image
curl "http://localhost:8000/download/$FILENAME" -o result.png
```

## Deployment

### Railway

The project includes a `railway.json` configuration for easy deployment to [Railway](https://railway.app).

1. Push your repository to GitHub
2. Connect your repository to Railway
3. Set environment variables as needed
4. Deploy

### Vercel

The project includes a `vercel.json` configuration for deployment to [Vercel](https://vercel.com).

1. Install Vercel CLI: `npm install -g vercel`
2. Run: `vercel`
3. Follow the prompts to deploy

## Project Structure

```
BgRemoveServer/
├── main.py              # FastAPI application and main endpoints
├── test.py              # Test utilities
├── requirements.txt     # Python dependencies
├── railway.json         # Railway deployment config
├── vercel.json          # Vercel deployment config
├── processed_images/    # Output directory for processed images
└── README.md            # This file
```

## Dependencies

- **FastAPI** - Modern web framework for APIs
- **Hypercorn** - ASGI web server
- **rembg** - Background removal using AI models
- **Pillow** - Image processing
- **ONNX Runtime** - Model inference engine
- **python-multipart** - Multipart form data handling

## Error Handling

The API returns meaningful error messages:

- **403 Forbidden** - Invalid or missing API key
- **400 Bad Request** - Invalid image file
- **404 Not Found** - File not found in download endpoint

## Performance Considerations

- Image processing time depends on image size and server resources
- Processed images are saved as PNG files in the `processed_images/` directory
- Consider implementing cleanup routines for old processed images in production
- The ONNX Runtime will download AI models on first use (~350MB)

## Security Recommendations

For production deployment:

1. **Use strong, unique API keys** instead of the default ones
2. **Enable HTTPS** for all communications
3. **Implement rate limiting** to prevent abuse
4. **Set up proper logging and monitoring**
5. **Regularly update dependencies** for security patches
6. **Implement periodic cleanup** of the `processed_images/` directory
7. **Use environment variables** for sensitive configuration

## Testing

Run the test suite:

```bash
python test.py
```

## Troubleshooting

**Issue: "ONNX model download fails"**

- Ensure your internet connection is stable
- Check available disk space (at least 1GB)

**Issue: "Memory errors during processing"**

- Images are being processed in memory; reduce image size or increase RAM
- Process large batches sequentially rather than in parallel

**Issue: "API key not working"**

- Verify the exact API key matches the one in `main.py`
- Ensure the `Authorization` header is properly set

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please submit pull requests or open issues for bugs and feature requests.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Built with ❤️ using FastAPI and rembg**
