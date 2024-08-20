import qrcode as qr

link = input("Enter the link for which you want to make a QR code: ")
img_name = link.split(".")[1]

qr_file = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

try:
    qr_file.add_data(link)
    qr_file.make(fit=True)
    img_format = qr_file.make_image(fill_color="blue", back_color="white")
    img_format.save(f"{img_name}_QRcode.png")
    print("Successfully Generated")
except Exception as e:
    print(f"Failed to Generate QR code: {e}")
