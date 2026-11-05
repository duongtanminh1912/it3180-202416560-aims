# Lab 05 — Hotfix và bảo trì nhiều phiên bản

- Hotfix tạo từ release/lab04 để chỉ sửa nền 1.0.x; tạo từ master sẽ lẫn sort/category của dòng 1.1.0. Không merge release ngược master.
- Commit sửa search và regression test tách khỏi commit version/CHANGELOG để cherry-pick đúng patch lên các dòng khác, không hạ version master xuống 1.0.1.
- `git cherry-pick -x FIX_SHA` tạo commit mới, ghi nguồn patch trong message. Merge toàn hotfix có thể mang version/changelog của dòng cũ và quan hệ lịch sử không mong muốn.
- Nếu v1.1.0 đã công bố thì sửa lỗi bằng v1.1.1; không đổi tag v1.1.0. Trong bài release/lab05 chưa gắn tag nên có thể đưa fix qua PR trước tag v1.1.0.
- Release-first: sửa ở dòng phát hành bị ảnh hưởng rồi forward-port lên master/dòng mới. Upstream-first: sửa master rồi backport dòng cũ. Chọn theo nguồn lỗi, phụ thuộc và mức khẩn cấp; cả hai cần ma trận phiên bản và regression test.
- Phát hiện sót patch trên release/lab05 bằng tìm nguồn cherry-pick trong log, so patch bằng git cherry, và chạy test tìm “lion” trên từng worktree. Cần kiểm tra cả hành vi và version.
- `git cherry -v master release/lab04`: dấu “-” là patch có tương đương trên upstream; “+” chưa có patch tương đương (ví dụ commit version 1.0.1). Với commit merge, patch-id không đủ thay thế audit nội dung.
- `git tag --contains FIX_SHA` chỉ xét ancestry: tag chứa commit nguồn; tag có cherry-pick tương đương nhưng SHA khác có thể không xuất hiện. Không thể từ thiếu tên tag mà kết luận thiếu patch.
- GitHub Actions dùng Python 3.12, chạy unittest cho PR vào master/release/** và push master. Required check chỉ cấu hình sau khi job thật đã chạy. PR demo phá tổng phải fail và đóng, không merge; chỉ kết luận chặn merge khi đã kiểm tra rule và thực sự thử merge.

SHA, PR, ma trận kiểm thử và log phát sinh sau baseline được thêm bằng topic/PR tiếp theo trong docs/evidence và docs/hotfix-audit.md, không sửa tag đã phát hành. Review độc lập chưa có partner nên chưa thực hiện.
