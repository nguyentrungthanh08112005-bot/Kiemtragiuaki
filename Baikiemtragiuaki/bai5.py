import matplotlib.pyplot as plt

def quan_ly_kho_hang():
    kho_hang = {
        'Balo': 150, 
        'Tui xach': 80, 
        'Vali': 120
    }

    print("THỐNG KÊ TỒN KHO")
    print(f"Dữ liệu ban đầu: {kho_hang}")

    try:
        so_luong_vi = int(input("\nNhập số lượng nhập kho cho 'Vi da': "))
        kho_hang['Vi da'] = so_luong_vi
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên cho số lượng. Mặc định gán là 0.")
        kho_hang['Vi da'] = 0

    if 'Balo' in kho_hang:
        kho_hang['Balo'] = max(0, kho_hang['Balo'] - 30)
        print("Đã xuất kho 30 Balo.")

    print(f"Dữ liệu sau khi cập nhật: {kho_hang}")

    labels = list(kho_hang.keys())
    values = list(kho_hang.values())
    
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    plt.figure(figsize=(8, 6))
    plt.pie(
        values, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140,  
        colors=colors,
        shadow=True
    )

    plt.title("Tỷ Trọng Các Mặt Hàng Trong Kho")
    plt.axis('equal') 

    print("\nĐang hiển thị biểu đồ...")
    plt.show()

quan_ly_kho_hang()