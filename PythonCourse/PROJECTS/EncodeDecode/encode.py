from pydub import AudioSegment

zeroSound = AudioSegment.from_file("C:/Work/Code/PythonCourse/homework/my_extraworks/EncodeDecode/beep-01a.wav", format="wav")
oneSound = AudioSegment.from_file("C:/Work/Code/PythonCourse/homework/my_extraworks/EncodeDecode/beep-02.wav", format="wav")

message = input("Enter a message: ")

res = ''.join(format(ord(i), '08b') for i in message)

overlay = zeroSound

for x in res:
    if x == "0":
        overlay = overlay + zeroSound
        
        
    if x == "1":
        overlay = overlay + oneSound


overlay.export(out_f = "C:\Work\Code\PythonCourse\homework\my_extraworks\EncodeDecode\overlay.wav", format = "wav")