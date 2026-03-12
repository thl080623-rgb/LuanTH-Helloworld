from odoo import models, fields

class IdeaBox(models.Model):
    _name = 'idea.box' # Tên kỹ thuật của model (định danh trong database)
    _description = 'Hộp Ý Tưởng'
    # Kế thừa tính năng nhắn tin (chatter) và hoạt động (activities) của Odoo
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name' # Xác định trường nào sẽ làm đại diện khi được link từ model khác

    # --- CÁC TRƯỜNG DỮ LIỆU (FIELDS) ---
    # tracking=True: Giúp lưu lại lịch sử thay đổi của trường này trong phần Chatter bên dưới
    name = fields.Char(string='Tên ý tưởng', required=True, tracking=True)
    description = fields.Text(string='Mô tả chi tiết', tracking=True)
    
    # Lựa chọn trạng thái của ý tưởng
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('submitted', 'Đã gửi'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối')
    ], string='Trạng thái', default='draft', tracking=True)
    
    # Quan hệ Many2one: Một ý tưởng gắn với 1 user
    create_uid = fields.Many2one('res.users', string='Người tạo', readonly=True)
    # Quan hệ Many2many: Một ý tưởng có thể gán cho nhiều người theo dõi/xử lý
    assigned_to = fields.Many2many(
        'res.users', 
        'idea_assigned_users_rel', # Tên bảng trung gian trong database
        'idea_id', 'user_id', 
        string='Người được gán', 
        tracking=True
    )
    approver_id = fields.Many2one('res.users', string='Người phê duyệt', readonly=True)
    
    rejection_reason = fields.Text(string='Lý do từ chối')
    approval_notes = fields.Text(string='Ghi chú phê duyệt')
    
    # Thời gian Datetime
    submitted_date = fields.Datetime(string='Ngày gửi', tracking=True)
    approved_date = fields.Datetime(string='Ngày phê duyệt', readonly=True)

    # --- CÁC HÀM XỬ LÝ LOGIC (METHODS) ---

    def submit(self):
        """Hàm chuyển trạng thái từ Nháp -> Đã gửi"""
        for record in self:
            if record.state != 'draft':
                raise ValueError('Chỉ có thể gửi ý tưởng ở trạng thái nháp!')
            record.write({
                'state': 'submitted',
                'submitted_date': fields.Datetime.now(), # Lưu thời gian hiện tại
            })
            # Gửi thông báo tự động vào phần Chatter
            record.message_post(body='<p>Ý tưởng đã được gửi để phê duyệt</p>')

    def approve(self):
        """Hàm phê duyệt ý tưởng"""
        for record in self:
            if record.state != 'submitted':
                raise ValueError('Chỉ có thể duyệt ý tưởng ở trạng thái đã gửi!')
            record.write({
                'state': 'approved',
                'approved_date': fields.Datetime.now(),
                'approver_id': self.env.user.id, # Lấy ID người đang thực hiện bấm nút
            })
            record.message_post(body='<p>Ý tưởng đã được duyệt</p>')

    def reject(self):
        """Hàm từ chối ý tưởng"""
        for record in self:
            if record.state != 'submitted':
                raise ValueError('Chỉ có thể từ chối ý tưởng ở trạng thái đã gửi!')
            # Kiểm tra bắt buộc nhập lý do khi từ chối
            if not record.rejection_reason:
                raise ValueError('Vui lòng nhập lý do từ chối!')
            record.write({
                'state': 'rejected',
                'approver_id': self.env.user.id,
            })
            record.message_post(body='<p>Ý tưởng đã bị từ chối</p>')