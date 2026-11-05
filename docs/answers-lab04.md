# Lab 04 — Release flow và baseline

- SemVer MAJOR.MINOR.PATCH: tăng MAJOR khi thay API không tương thích; MINOR khi thêm tính năng tương thích; PATCH khi sửa lỗi tương thích. Với 0.y.z API chưa ổn định. Bài chọn 1.0.0 để đánh dấu baseline chức năng ổn định, không phải cứ Lab 04 là phải thành 0.4.0.
- Tag là tên trỏ commit, annotated tag thêm metadata/message, không di chuyển tag đã công bố. Release branch là ref có thể tiến qua các PR bảo trì. GitHub Release là mô tả và asset gắn tag, khác cả hai.
- Chuẩn bị version, CHANGELOG và tài liệu trên master qua PR trước rồi tạo release/lab04 để baseline có đủ nội dung đã được kiểm tra.
- Không merge release ngược master vì có commit version và thay đổi bảo trì riêng dòng; chuyển commit fix cần thiết bằng cherry-pick -x qua PR.
- `git log A..B` liệt kê commit reachable từ B nhưng không reachable từ A. `git diff A B` so nội dung snapshot hai đầu, không liệt kê tập commit. Trước hotfix, master..release/lab04 rỗng; release/lab04..master có các commit phát triển tiếp.
- Detached HEAD nghĩa là HEAD trỏ trực tiếp commit, không bám nhánh; commit mới có thể mất tên tham chiếu nếu không tạo branch. Worktree là working directory bổ sung chia sẻ object database; worktree có thể checkout branch hoặc detached HEAD. Dùng worktree --detach tại tag để kiểm tra baseline mà không đổi working tree chính.
- Bốn annotated tag được tạo sau khi baseline đã chốt: v0.1.0, v0.2.0, v0.3.0, v1.0.0. Không di chuyển tag.
- Audit worktree sẽ chạy main, unittest, kiểm tra version/file/CHANGELOG, git archive. Vì bằng chứng phát sinh sau baseline, được bổ sung bằng PR tiếp theo trước hotfix, không sửa tag/baseline để đưa log vào.
