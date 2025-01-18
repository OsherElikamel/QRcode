import qrcode  
from datetime import datetime  
import io  

def generate_qr():
    
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=2,  
    )

    qr.add_data(current_date)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")  
    buffer.seek(0)  
    return buffer  