# GitHub — việc còn thiếu và trạng thái

- Repository công khai theo sự cho phép của người dùng: https://github.com/duongtanminh1912/it3180-202416560-aims.
- Đã làm: Issue lỗi giới hạn #7, Issue tìm kiếm #20; các PR thật ở pull-request-index.md; Releases 1.0.0/1.0.1/1.1.0; bảo vệ master và release/*; CI trên master và hai dòng release đang bảo trì, required check unit-tests và phép thử merge PR lỗi bị chặn.
- **Chưa làm**: review độc lập Request changes → sửa → re-request → Approve. Chưa có partner được chỉ định, không tự mời collaborator và không tự approve. Khi có partner, yêu cầu review trên PR mới và tăng required approval từ 0 lên 1 theo quy định nhóm.
- **Không có phần đang bị chặn bởi quyền GitHub**. HTTP 403 protection ban đầu ở repo riêng tư đã giải quyết bằng chuyển công khai theo lựa chọn người dùng. Lỗi repository disabled khi GitHub chuyển visibility chỉ tạm thời, lần kiểm tra tiếp theo hoạt động.
- Issue #7 đã tự đóng sau PR #8 vào master. Issue #20 vẫn mở khi kiểm tra sau PR #22 dù closingIssuesReferences nhận đúng liên kết; đã đóng thủ công sau xác minh patch ở ba dòng. Không tuyên bố Issue #20 tự đóng.
- Workflow chỉ thêm vào các dòng release đang bảo trì (lab04/lab05); lab01–03 giữ baseline lịch sử. Tags không thay đổi. Các log sau baseline được thêm trên master qua topic/PR.
- Snapshot JSON và chỉ mục không chứa PR báo cáo cuối vì được chụp trước commit/PR chứa chúng; xem danh sách PR trực tiếp để có trạng thái mới nhất.
