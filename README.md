# AIMS-mini — IT3180

MSSV **202416560** · Tài khoản **duongtanminh1912** · Nhánh chính **master**.

Repository: https://github.com/duongtanminh1912/it3180-202416560-aims

Ứng dụng Python >= 3.10, chỉ thư viện chuẩn, dùng unittest. Đã kiểm chứng bằng Python 3.12.16 local và Python 3.12 trên GitHub Actions.

## Cài đặt và chạy

```sh
git clone https://github.com/duongtanminh1912/it3180-202416560-aims.git
cd it3180-202416560-aims
python3.12 -m venv .venv
source .venv/bin/activate
python main.py
python -m unittest discover -s tests -v
```

Không có dependency cần pip install. Nếu dùng Python khác >= 3.10, thay python3.12 bằng executable tương ứng. Demo in `AIMS-mini v1.1.0`, ba DVD và `Total cost: 63.89 $`.

## Chức năng

DigitalVideoDisc có title/category/director/length/cost và giá trị mặc định. Cart tối đa 20 DVD; add_dvd trả bool, remove_dvd trả bool, total_cost, print_cart, total_cost_with_discount(percent) kiểm tra [0,100]. sort_by_title và sort_by_cost sắp tăng dần, sửa items tại chỗ; tên dùng thứ tự chuỗi Python, giá bằng nhau giữ thứ tự cũ. search_by_title tìm chuỗi con không phân biệt hoa thường; search_by_category khớp chính xác category không phân biệt hoa thường.

## Xem baseline

| Bài/phiên bản | Nhánh/tag | Kết quả kiểm chứng |
|---|---|---|
| Lab 01 | release/lab01 / v0.1.0 | Demo 63.89; chưa có unittest |
| Lab 02 | release/lab02 / v0.2.0 | Demo, giỏ rỗng, tìm tên; chưa có unittest |
| Lab 03 | release/lab03 / v0.3.0 | 4 test PASS |
| Lab 04 baseline | v1.0.0 | 6 test PASS; chưa sort/category; lỗi tìm lion còn tồn tại |
| Bảo trì 1.0.x | release/lab04 / v1.0.1 | 7 test PASS; sửa tìm lion, không lẫn tính năng 1.1 |
| Lab 05 | release/lab05 / v1.1.0 | 10 test PASS |
| Phát triển | master (1.1.0) | 10 test PASS |

Tag giữ nguyên snapshot; release/lab04 và release/lab05 đã nhận workflow qua PR sau phát hành nên đầu nhánh mới hơn tag. Dùng tag để tái lập bản phát hành:

```sh
git fetch origin --tags
git worktree add --detach ../aims-v1.0.0 v1.0.0
cd ../aims-v1.0.0
python3.12 main.py
python3.12 -m unittest discover -s tests -v
```

Thay tag để xem baseline khác, dùng đường dẫn worktree mới. Hai baseline đầu chưa có tests, không xem việc chạy 0 test là PASS kiểm thử chức năng. Lỗi cố ý nằm trong lịch sử, không sửa lại tag.

## Tài liệu và bằng chứng

- [Câu trả lời Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md), [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md), [Lab 05](docs/answers-lab05.md).
- [Use case](docs/use-case.md), [CHANGELOG](CHANGELOG.md), [audit hotfix](docs/hotfix-audit.md).
- [Checklist nộp bài](docs/submission-checklist.md), [việc GitHub còn thiếu](docs/github-todo.md), [chỉ mục PR](docs/pull-request-index.md), [log thực tế](docs/evidence/).
- [Issues](https://github.com/duongtanminh1912/it3180-202416560-aims/issues?q=is%3Aissue), [Releases](https://github.com/duongtanminh1912/it3180-202416560-aims/releases), [Actions](https://github.com/duongtanminh1912/it3180-202416560-aims/actions).

## Quy trình đã kiểm chứng

Master và release/* bắt buộc PR, 0 approval khi làm một mình, dismiss stale approvals, enforce admin, không force push/deletion. Required check unit-tests được đặt sau job chạy thật. Push trực tiếp với commit mới bị GitHub từ chối. Workflow dùng Actions chính thức pin SHA của [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) và [setup-python v7.1.0](https://github.com/actions/setup-python/releases/tag/v7.1.0), đã xác minh qua API.

PR demo CI lỗi: https://github.com/duongtanminh1912/it3180-202416560-aims/pull/30; đã fail, bị từ chối merge và đóng, không tích hợp mã lỗi. Review độc lập Request changes → sửa → re-request → Approve chưa thực hiện vì chưa có partner; không tự approve.
