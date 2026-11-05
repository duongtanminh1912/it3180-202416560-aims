# Lab 03 — Bugfix, conflict và hoàn tác

- Merge base là tổ tiên chung tốt nhất của hai commit, dùng làm gốc so sánh ba chiều khi merge.
- Test phải FAIL trước fix để chứng minh nó bắt đúng lỗi hiện có; PASS sau fix giúp chứng minh sửa lỗi. Test giỏ 20 DVD và test giảm 100 còn 80 đã chạy trước/sau, không giả lập kết quả.
- Bugfix tạo từ feature phải PR vào feature vì nó phụ thuộc thay đổi chưa có trên master; PR thẳng master có thể mang theo tính năng chưa sẵn sàng. Sau đó mới PR feature/discount đã sửa vào master.
- Reset dịch chuyển HEAD/nhánh: --soft giữ index và working tree; --mixed reset index, giữ working tree; --hard reset cả index và working tree, làm mất thay đổi tracked chưa lưu. Mỗi ví dụ dùng commit tạm riêng, lưu SHA và tạo rescue/reset-*; không reset commit bài lab.
- Revert tạo commit đảo thay đổi, không viết lại lịch sử. Master/release dùng revert vì đã chia sẻ và phải đi qua PR.
- `git revert -m 1 833c51bef5a92c4418ff420b6347015cf4e30ea3` chọn cha thứ nhất làm mainline; đảo phần thay đổi merge so với master trước merge. Thông báo sau revert trở lại “Đã thêm đĩa vào giỏ hàng”.
- Reflog là lịch sử cập nhật refs trong repo local, không tự push; có hạn giữ và chịu garbage collection. Cần tạo rescue branch trước khi object không còn reachable bị dọn.
- Conflict thật xuất hiện khi hai nhánh cùng baseline sửa cùng dòng thêm DVD. Merge master vào feature/show-added-title sau khi nhánh Việt hóa đã merged, rồi kết hợp thành `Đã thêm đĩa '<title>' vào giỏ hàng`, chạy test và commit giải quyết. SHA merge PR thực tế: `833c51bef5a92c4418ff420b6347015cf4e30ea3`.
- Cách khác trên nhánh riêng: fetch, `git rebase origin/master`, sửa conflict, git add, git rebase --continue; dùng --abort để hủy khi cần. Không rebase nhánh đã chia sẻ khi chưa được đồng thuận.

Issue giới hạn: https://github.com/duongtanminh1912/it3180-202416560-aims/issues/7. Đã kiểm tra state sau merge default branch. Nhật ký thực tế: evidence/lab03.log và lab03-limit-*.log.
