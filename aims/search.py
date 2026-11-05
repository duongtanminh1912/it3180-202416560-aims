def search_by_category(items, category):
    """Khớp chính xác category, không phân biệt hoa thường."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Tìm theo chuỗi con, không phân biệt hoa thường."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
