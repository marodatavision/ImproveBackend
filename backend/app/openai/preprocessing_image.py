import base64
from PIL import Image
from io import BytesIO
from mimetypes import guess_type

# Funktion zum Resizen und Base64-Kodieren des Bildes
def prepare_image_for_api(image_path, max_size=(512, 512)):
    # Bild öffnen und auf die Maximalgröße skalieren
    img = Image.open(image_path)
    img.thumbnail(max_size)
    
    # Bild in den Speicher schreiben
    buffer = BytesIO()
    img.save(buffer, format=img.format)
    
    # Base64-Kodierung des Bildes
    mime_type, _ = guess_type(image_path)
    base64_encoded_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return f"data:{mime_type};base64,{base64_encoded_image}"
