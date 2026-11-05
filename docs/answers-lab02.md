# Lab 02 — Feature/topic và PR

- Fetch và merge master trước PR giúp phát hiện conflict, kiểm thử với thay đổi mới, giảm rủi ro lúc tích hợp. Hai nhánh feature/cart-print và feature/search-by-title được tạo từ cùng baseline; nhánh search đã fetch + merge master trước PR.
- Không rebase nhánh master/release hoặc nhánh đã chia sẻ khi chưa có đồng thuận: rebase thay SHA, làm lịch sử người khác phân kỳ. Nhánh cá nhân chưa push phù hợp hơn.
- feature/* chứa chức năng sản phẩm; topic/* thường dùng cho tài liệu, cấu hình hoặc thay đổi chuyên biệt. Đây là quy ước, Git xử lý chúng như nhau.

| Kiểu | SHA/lịch sử | Truy vết và revert |
|---|---|---|
| Merge commit | Giữ SHA commit nguồn, thêm commit hai cha | Giữ cấu trúc nhánh/PR, revert merge bằng -m 1 |
| Squash | Tạo commit mới chứa tổng diff, không giữ ancestry từng commit nguồn | Dễ revert cả tính năng, lịch sử chi tiết còn trong PR |
| Rebase merge | Viết lại SHA trên đầu nhánh đích, lịch sử thẳng | Từng commit được giữ nội dung; revert theo từng commit, không có merge commit |

- Dismiss stale approvals làm approval cũ mất sau push mới để reviewer xem lại thay đổi. Làm một mình cấu hình 0 approval, bắt buộc PR, enforce_admins, không force push/deletion; không tự approve.
- GitHub private ban đầu trả 403 cho protection; sau khi người dùng cho phép chuyển công khai đã thiết lập protection. Đã thử push một commit mới thực sự từ topic/protection-probe vào master và xác nhận server từ chối; commit tạm giữ trên nhánh riêng.
- Chưa có reviewer thật: chuỗi Request changes → sửa → re-request → Approve chưa thực hiện.
- Trước PR tài liệu này đã có ít nhất 5 PR merged: refactor, template, cart-print (merge), search (squash), use-case (rebase). SHA và URL thực tế có trong evidence/lab02.log.
