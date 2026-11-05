# Checklist nộp bài IT3180 — 202416560

Ngày thực hiện: 2026-11-05, Asia/Ho_Chi_Minh. Các link là kết quả GitHub thực tế; log không giả lập.

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| Kiểm tra môi trường, danh tính local, bảo toàn mã khởi đầu | Đã làm | evidence/final-audit.log; lịch sử root commit |
| Lab 01: khởi tạo, mã gốc, restore/staged/amend, git mv/import riêng, PR, release | Đã làm | answers-lab01.md; PR #1; evidence/lab01.log |
| Lab 02: template, hai nhánh cùng baseline, 3 kiểu merge, use case, >=5 PR | Đã làm | PR #1–6; answers-lab02.md; evidence/lab02.log |
| Push commit mới vào master bị chặn | Đã làm | GH006 trong evidence/lab02.log; topic/protection-probe |
| Review độc lập Request changes/sửa/re-request/Approve | Chưa làm | Chưa có partner; không tự approve |
| Lab 03: Issue, test FAIL/PASS, sửa off-by-one, discount PR vào feature | Đã làm | Issue #7; PR #8–10; lab03-limit-*.log |
| Conflict thật, giải quyết kết hợp, revert merge -m 1 | Đã làm | PR #11–13; evidence/lab03-conflict.log; answers-lab03.md |
| Reset soft/mixed/hard riêng, reflog và rescue | Đã làm | evidence/lab03.log; rescue/reset-* local |
| Lab 04: chuẩn bị version/tài liệu trước baseline, annotated tags, release | Đã làm | PR #15; Releases; evidence/lab04.log |
| Sort sau baseline, audit trước hotfix, worktree/archive 1.0.0 | Đã làm | PR #16–17; asset aims-mini-1.0.0.tar.gz tại Release |
| Lab 05: category, version 1.1.0/tài liệu trước release/lab05 | Đã làm | PR #18–19; docs/answers-lab05.md trong baseline |
| Hotfix từ release/lab04, FIX_SHA, tách commit version | Đã làm | PR #21; hotfix-audit.md |
| Diff v1.0.0..v1.0.1 đúng bốn file, không sort/category | Đã làm | evidence/lab05-hotfix.log; final-audit.log |
| Cherry-pick -x đúng FIX_SHA lên master/lab05, không hạ version | Đã làm | PR #22–23; log grep/cherry/tag --contains |
| Issue đã đóng | Đã làm | #7 tự đóng; #20 đóng thủ công sau xác minh, xem github-todo.md |
| Ma trận v1.0.0/v1.0.1/v1.1.0/master | Đã làm | 6/7/10/10 test PASS; worktree logs |
| Bảo vệ master/release/*, 0 approval solo, stale/admin/no force/no deletion | Đã làm | API protection trong evidence/lab05-ci.log và final-audit.log |
| CI Python 3.12, PR master/release/**, push master | Đã làm | .github/workflows/ci.yml; PR workflow thực tế trong pull-request-index.md |
| Workflow qua PR riêng vào hai dòng release bảo trì | Đã làm | PR CI release/lab04 và release/lab05; tags không đổi |
| Required check sau khi job chạy, CI lỗi và merge bị từ chối | Đã làm | [PR demo](https://github.com/duongtanminh1912/it3180-202416560-aims/pull/30); evidence/ci-demo-failed-job.log; lab05-ci.log |
| Mã lỗi demo không merge | Đã làm | PR demo CLOSED, mergedAt null; master test PASS |
| README, 5 answers, github-todo, checklist, log qua PR | Đã làm | PR chứa tài liệu này; CI bắt buộc PASS trước merge |

Snapshot có 25 PR merged trước PR báo cáo cuối. Toàn bộ yêu cầu có thể làm một mình đã có bằng chứng; không tuyên bố hoàn thành review độc lập. Người dùng cần chỉ định partner nếu môn học bắt buộc chu trình review thật.
