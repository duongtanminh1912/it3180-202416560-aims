# Audit hotfix

FIX_SHA: `e8a185b82f140029cd2cfc4dcba9ac79cca2b743`

Issue: https://github.com/duongtanminh1912/it3180-202416560-aims/issues/20

Commit fix chỉ chứa aims/search.py và tests/test_search.py; commit kế tiếp chỉ version và CHANGELOG. Diff v1.0.0 → v1.0.1 đúng 4 file. Cherry-pick -x lên master và release/lab05, không merge release ngược master. Master giữ 1.1.0.

| Ref | Version | Tìm lion | Sort/category |
|---|---|---|---|
| v1.0.0 | 1.0.0 | [] (lỗi đã tái hiện) | Không |
| v1.0.1 | 1.0.1 | The Lion King | Không |
| v1.1.0 | 1.1.0 | The Lion King | Có |
| master | 1.1.0 | The Lion King | Có |

Kết quả unittest, ancestry tags, patch equivalence và URL PR thật: evidence/lab05-hotfix.log. `tag --contains` không thể dùng thay kiểm tra patch cherry-picked.
