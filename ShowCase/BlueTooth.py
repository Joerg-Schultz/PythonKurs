# https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-server.py

# https://stackoverflow.com/questions/34599703/rfcomm-bluetooth-permission-denied-error-raspberry-pi
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

print("Connected. Type something...")
while True:
    data = input()
    print("Data: ", data)
    if not data:
        break
    data += "\n"
    message = str.encode(data)
    client_sock.send(message)

# try:
#     while True:
#         data = client_sock.recv(1024)
#         if not data:
#             break
#         print("Received", data)
# except OSError:
#     pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")