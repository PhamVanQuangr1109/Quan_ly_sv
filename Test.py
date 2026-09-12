danh_sach_sv = []

while True:
    print("\n-----------------------------------------------")
    print("  Chào mừng bạn đến với app quản lý sinh viên!")
    print("-----------------------------------------------")
    print("Vui lòng chọn chức năng mà bạn mong muốn:")
    print("1. Thêm sinh viên mới")
    print("2. Xem thông tin sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tạo bảng xếp hạng sinh viên")
    print("0. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    # CHỨC NĂNG 1: THÊM SINH VIÊN MỚI
    if choice == '1':
        print("\n--- THÊM SINH VIÊN MỚI ---")
        mssv = input("Nhập MSSV: ").strip()
        ten_sv = input("Nhập tên sinh viên: ").strip()
        tuoi = int(input("Nhập tuổi sinh viên: "))
        diem_toan = float(input("Nhập điểm toán: "))
        diem_ly = float(input("Nhập điểm lý: "))
        diem_hoa = float(input("Nhập điểm hóa: "))

        dtb = (diem_toan + diem_ly + diem_hoa) / 3
        if dtb > 8:
            xep_loai = 'Giỏi'
        elif dtb >= 6:
            xep_loai = 'Khá'
        else:
            xep_loai = 'Trung bình'

        sv = [mssv, ten_sv, tuoi, diem_toan, diem_ly, diem_hoa, xep_loai]
        danh_sach_sv.append(sv)
        print("Thêm sv thành công")

    # CHỨC NĂNG 2: XEM THÔNG TIN SINH VIÊN
    elif choice == '2':
        print("\n-----------------------------------------------------------------------------------------")
        print(f"{'MSSV':<8} | {'Họ và tên':<20} | {'Tuổi':<5} | {'Toán':<5} | {'Lý':<5} | {'Hóa':<5} | {'Phân loại':<10}")
        print("-----------------------------------------------------------------------------------------")
        if not danh_sach_sv:
            print("Chưa có sinh viên nào trong danh sách!")
        else:
            for sv in danh_sach_sv:
                print(f"{sv[0]:<8} | {sv[1]:<20} | {sv[2]:<5} | {sv[3]:<5.1f} | {sv[4]:<5.1f} | {sv[5]:<5.1f} | {sv[6]:<10}")
        print("-----------------------------------------------------------------------------------------")

    # CHỨC NĂNG 3: XÓA SINH VIÊN
    elif choice == '3':
        print("\n--- XÓA SINH VIÊN ---")
        if not danh_sach_sv:
            print("Danh sách hiện đang trống!")
        else:
            mssv_xoa = input("Nhập MSSV của sinh viên cần xóa: ").strip()
            da_xoa = False
            for sv in danh_sach_sv:
                if sv[0] == mssv_xoa:
                    danh_sach_sv.remove(sv)
                    print(f"Đã xóa sinh viên {sv[1]} (MSSV: {mssv_xoa}) thành công!")
                    da_xoa = True
                    break
            if not da_xoa:
                print(f"Không tìm thấy sinh viên nào có MSSV: {mssv_xoa}")

    # CHỨC NĂNG 4: BẢNG XẾP HẠNG
    elif choice == '4':
        print("\n-------------------------------- BẢNG XẾP HẠNG SINH VIÊN --------------------------------")
        if not danh_sach_sv:
            print("Chưa có sinh viên nào để xếp hạng!")
        else:
            ds_xep_hang = sorted(danh_sach_sv, key=lambda sv: sv[3] + sv[4] + sv[5], reverse=True)
            print(f"{'Hạng':<5} | {'MSSV':<8} | {'Họ và tên':<20} | {'Tổng điểm':<10} | {'ĐTB':<6} | {'Phân loại':<10}")
            print("-----------------------------------------------------------------------------------------")
            for i, sv in enumerate(ds_xep_hang, 1):
                tong_diem = sv[3] + sv[4] + sv[5]
                dtb = tong_diem / 3
                print(f"{i:<5} | {sv[0]:<8} | {sv[1]:<20} | {tong_diem:<10.1f} | {dtb:<6.1f} | {sv[6]:<10}")
        print("-----------------------------------------------------------------------------------------")

    # CHỨC NĂNG 0: THOÁT
    elif choice == '0':
        print("\nXin chào, và hẹn gặp lại.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 4!")