def tinh_bmi():
    print("PHẦN MỀM ĐO CHỈ SỐ BMI")
    
    try:
        can_nang = float(input("Nhập cân nặng (kg): "))
        chieu_cao = float(input("Nhập chiều cao (m): "))

        bmi = can_nang / (chieu_cao ** 2)

        if bmi < 18.5:
            loai = "Gầy, trơ xương"
        elif 18.5 <= bmi <= 24.9:
            loai = "Bình thường"
        else:
            loai = "béo, rất béo"

        print(f"\nChỉ số BMI của bạn là: {bmi:.2f}")
        print(f"Phân loại: {loai}")

    except ValueError:
        print("\nLỗi: Vui lòng chỉ nhập số và tránh kí tự lạ (ví dụ: 60 hoặc 1.7), không nhập chữ.")
        
    except ZeroDivisionError:
        print("\nLỗi: Chiều cao không thể bằng 0. Vui lòng kiểm tra lại.")
        
    except Exception as e:
        print(f"\nĐã xảy ra lỗi không xác định: {e}")

tinh_bmi()