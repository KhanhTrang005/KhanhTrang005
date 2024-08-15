
nguoichoi = input("Người chơi: ")
nguoimay = input("Người máy: ")
a = "kéo"
b = "búa"
c = "bao"

if nguoichoi == nguoimay:
    print("Hòa")
if nguoichoi == a and nguoimay == b:
        print("Kết quả máy thắng")
elif nguoichoi == a and nguoimay == c:
        print("Kết quả người chơi thắng")
if nguoichoi == b and nguoimay == a:
        print("Kết quả người chơi thắng")
elif nguoichoi == b and nguoimay == c:
        print("Kết quả máy thắng")
if nguoichoi == c and nguoimay == a:
        print("Kết quả máy thắng")
elif nguoichoi == c and nguoimay == b:
        print("Kết quả người chơi thắng")

 
    
    

    

