from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Header, __version__
from time import time
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import rembg
from PIL import Image
import io
import uuid
import os

app = FastAPI()

ALLOWED_ORIGINS = ["*","https://bgremoveserver-production.up.railway.app/"]

# Enable CORS with specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Authorization", "Content-Type"],
)

# List of allowed API keys (Store securely in environment variables in production)
API_KEYS = {"key1", "key2", "key3"}  # Add multiple API keys here

# # Middleware function to check API key
def verify_api_key(Authorization: str = Header(None)):
    if Authorization not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return Authorization


@app.post("/remove-background/")
async def remove_background(
    file: UploadFile = File(...),
    Authorization: str = Depends(verify_api_key)  # API key check
):
    try:
        # Read image bytes and open it
        image_bytes = await file.read()
        input_image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

        # Process image with rembg
        output_image = rembg.remove(input_image)

        # Save processed image
        output_filename = f"processed_images/{uuid.uuid4()}.png"
        output_image.save(output_filename, format="PNG")

        return {"filename": output_filename.split("/")[-1]}
    
    except Exception as e:
        return {"error": str(e)}

@app.get("/download/{filename}")
async def download_image(
    filename: str,
    # Authorization: str = Depends(verify_api_key)  # API key check
):
    file_path = f"processed_images/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/png", filename=filename)
    return {"error": "File not found"}
@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}
