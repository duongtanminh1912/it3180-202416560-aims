# Changelog

Theo Keep a Changelog; phiên bản tuân theo SemVer. Ngày theo Asia/Ho_Chi_Minh.

## [Unreleased]

### Added
- Sắp giỏ tăng dần theo tên hoặc giá, thay đổi items tại chỗ.

## [1.0.0] - 2026-11-05

### Added
- Mô hình DVD, giỏ hàng, thêm/xóa, tính tổng và hiển thị giỏ.
- Tìm kiếm theo tên (phân biệt hoa thường ở baseline này).
- Tính tổng sau giảm giá với kiểm tra phần trăm 0–100.
- Đóng gói aims, sơ đồ use case, tài liệu và kiểm thử unittest.

### Fixed
- Từ chối DVD thứ 21, giữ giới hạn 20 DVD.
- Công thức giảm giá trả số tiền còn lại, kiểm tra phần trăm ngoài giới hạn.
- Kết hợp xung đột thông báo, sau đó revert phần hiển thị tên DVD để thực hành; giữ thông báo tiếng Việt.
