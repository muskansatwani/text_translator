import qrcode

# Generate the QR code for the link
qr = qrcode.QRCode()
qr.add_data("https://c6d945aa0b2a2a2fa1.gradio.live")
qr.make(fit=True)
qr_code_image = qr.make_image(fill_color="black", back_color="white")
qr_code_image.save("qr_code1.png")
