def search_by_title(items, keyword):
    """Tìm theo chuỗi con; phân biệt hoa thường ở baseline Lab 02."""
    return [dvd for dvd in items if keyword in dvd.title]
