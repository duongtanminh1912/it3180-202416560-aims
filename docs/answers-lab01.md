# Lab 01 — Thiết lập và refactor

MSSV: 202416560. Ngày thực hiện: 2026-11-05 (Asia/Ho_Chi_Minh).

- Working directory là các file đang làm việc; staging area (index) giữ nội dung dự kiến cho commit tiếp theo; local repository (.git) lưu object, commit và refs.
- `git config --global` thường lưu ở ~/.gitconfig hoặc $XDG_CONFIG_HOME/git/config, áp dụng cho người dùng. `--local` lưu .git/config, chỉ áp dụng repo hiện tại và ưu tiên hơn global. Bài này chỉ cấu hình local.
- `git mv` chuyển file và stage việc chuyển. Git lưu snapshot, nhận diện rename bằng độ giống nhau khi diff/log, không lưu một object rename riêng. Commit chuyển file độc lập giữ khả năng xem xét rõ ràng; `git log --follow -- aims/cart.py` theo lịch sử trước rename.
- release/lab01 được tạo từ master sau khi PR refactor và tài liệu đã merged, làm baseline để đối chiếu; những sửa đổi sau phải qua PR, không chỉnh baseline để thêm bằng chứng.
- Làm một mình vẫn dùng PR để xem diff, kiểm thử, ghi lý do và giữ dấu tích hợp. Không có partner nên chưa thực hiện review độc lập hay approval.

## Hoàn tác thực tế

Đã thêm dòng TEMP vào README rồi `git restore README.md`; diff trở về sạch. Đã stage file tạm, `git restore --staged docs/amend-practice.txt` để đưa khỏi index nhưng giữ working file. Đã commit file tạm, ghi SHA cũ, `git commit --amend -m ...` trên commit chưa push và ghi SHA mới, sau đó xóa file tạm bằng commit riêng. Không sửa lịch sử đã công bố. Xem log thực tế trong docs/evidence/lab01.log.

## Kiểm chứng

Mã ban đầu ở thư mục gốc chạy bằng Python 3.12 in tổng 63.89 $. Refactor dùng git mv, commit chuyển file và sửa import riêng; chạy lại vẫn cùng tổng. Lỗi giới hạn `>` được cố ý giữ đến Lab 03.
