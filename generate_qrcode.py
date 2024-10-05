# Capturar o texto/link do usuário
user_input = input("Digite o texto ou link para o QR Code: ")

import qrcode as qr
qr = qr.QRCode(
    version = 1,
    error_correction= qr.constants.ERROR_CORRECT_L,
    box_size=30,
    border=2,

)

qr.add_data(user_input)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

# Capturar o nome do arquivo do usuário
file_name = input("Digite o nome do arquivo para salvar o QR Code (sem a extensão .png): ")

# Salvar o QR Code como um arquivo .png com o nome fornecido
img.save(f"{file_name}.png")

print(f"QR Code salvo como {file_name}.png")

# Ao final quando digitar o link ou texto vai gerar um qrcode e exportara ele em formato .png que tambem ira te pedir um nome parar ele gerar 