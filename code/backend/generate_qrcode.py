import qrcode
import io
import sys

def generate_qr_png(url):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=20,  # Size of each box in the QR code grid
        border=0,  # Thickness of the border
    )
    
    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an in-memory bytes buffer to store the PNG
    buffer = io.BytesIO()

    # Generate QR code as a PNG image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the buffer in PNG format
    img.save(buffer, format="PNG")
    
    # Get the PNG data from the buffer
    png_data = buffer.getvalue()
    
    # Save PNG data to a file (optional)
    with open("qrcode.png", "wb") as f:
        f.write(png_data)
    
    print("QR code PNG generated!")
    return png_data

# Example usage:
url = sys.argv[1]
generate_qr_png(url)
