def tao_ghi_chu():
    danh_sach_cong_viec = []
    
    print("ỨNG DỤNG GHI CHÚ CÔNG VIỆC TRONG NGÀY")
    print("Hãy nhập tên công việc:")
    print("Để kết thúc hãy bấm enter)")
    
    while True:
        cong_viec = input("Nhập công việc: ").strip()
        
        if cong_viec.lower() == 'xong' or cong_viec == "":
            break
            
        danh_sach_cong_viec.append(cong_viec)
    
    if not danh_sach_cong_viec:
        print("\nHãy nhập lại công việc")
        return
    
    print("DANH SÁCH CÔNG VIỆC CỦA BẠN")
    danh_sach_da_danh_so = []
    
    for so_thu_tu, cong_viec in enumerate(danh_sach_cong_viec, start=1):
        dong_cong_viec = f"{so_thu_tu}. {cong_viec}"
        danh_sach_da_danh_so.append(dong_cong_viec)
        print(dong_cong_viec)

    with open("C:/Users/Admin/Desktop/todo_list.txt", "w", encoding="utf-8") as file:
        for dong in danh_sach_da_danh_so:
            file.write(dong + "\n")
        print("đã xuất file danh sách công việc")
        
tao_ghi_chu()