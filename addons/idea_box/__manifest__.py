{
    'name': 'Idea Box', # Tên hiển thị của ứng dụng trên giao diện Odoo.
    'version': '1.0', # Phiên bản hiện tại của module.
    'category': 'Tools', # Danh mục ứng dụng (ở đây phân loại vào nhóm Công cụ/Tools).
    'author': 'T4tek', # Tên cá nhân, đội ngũ hoặc công ty phát triển module này.
    'summary': 'Quản lý ý tưởng sáng tạo của nhân viên', # Câu mô tả ngắn gọn, xuất hiện ngay dưới tên app.
    'description': 'Nền tảng quản lý và chia sẻ ý tưởng sáng tạo trong công ty', # Mô tả chi tiết các tính năng của module.
    
    # 'depends': Danh sách các module có sẵn của Odoo bắt buộc phải cài trước.
    # - base: module lõi mặc định.
    # - mail: để dùng tính năng theo dõi (chatter), gửi email hoặc bình luận.
    # - web: để sử dụng các tính năng giao diện web cơ bản.
    'depends': ['base', 'mail', 'web'], 
    
    # 'data': Danh sách các file cấu trúc dữ liệu, phân quyền và giao diện sẽ được load khi cài đặt.
    # Lưu ý: Thứ tự các file ở đây rất quan trọng, hệ thống sẽ đọc từ trên xuống dưới.
    'data': [
        'security/groups.xml', # Nơi tạo ra các nhóm người dùng (VD: User, Manager).
        'security/ir.model.access.csv', # Cấp quyền Thêm, Sửa, Xóa, Xem cho các nhóm trên.
        'security/idea_rules.xml', # Phân quyền cấp dòng dữ liệu (VD: Nhân viên chỉ thấy ý tưởng của mình).
        'views/idea_box_views.xml', # Nơi định nghĩa giao diện (Form view, Tree/List view) - chính là để tạo ra giao diện như bức ảnh bạn vừa gửi ở trên.
    ],
    
    'web_icon': 'idea_box/static/description/icon.svg', # Đường dẫn trỏ tới file ảnh icon của ứng dụng.
    'assets': {}, # Nơi chứa các cấu hình nhúng file CSS hoặc JavaScript tùy chỉnh (hiện tại đang để trống).
    'license': 'LGPL-3', # Giấy phép bản quyền mã nguồn (Odoo thường dùng chuẩn LGPL-3).
    
    'installable': True, # Khai báo True để hệ thống cho phép người dùng click nút "Cài đặt" (Install).
    'application': True, # Đặt là True thì module sẽ hiển thị như một Ứng dụng độc lập, to rõ trên màn hình chính (App Dashboard).
    'auto_install': False, # Đặt là False để tránh việc module tự động cài đặt ngầm vào hệ thống.
}