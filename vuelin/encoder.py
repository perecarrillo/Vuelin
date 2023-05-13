from PIL import Image
from io import BytesIO

def stringToBool(msg) -> bool:
    if msg == "0": return False
    else: return True

def stringToInt(msg) -> int:
    return int(msg)

def jpgToByteArray(msg):
    return bytearray(msg.tobytes())

def ByteArrayToJpg(msg):
    return Image.frombytes("RGB", (476, 588), msg)

def stringToArray(msg):
    return msg.split(";")