import socket
import time

# Endereço e porta do servidor de socket
HOST = 'localhost'
PORT = 9999

# Criando um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Servidor rodando em {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            # Enviar dados (codificando em UTF-8)
            conn.sendall('Olá, mundo!\n'.encode('utf-8'))
            time.sleep(1)  # Pausa de 1 segundo entre as mensagens
