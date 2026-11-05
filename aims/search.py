def search_by_category(items, category):
    """Khớp chính xác category, không phân biệt hoa thường."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Tìm theo chuỗi con; phân biệt hoa thường ở baseline Lab 02."""
    return [dvd for dvd in items if keyword in dvd.title]
