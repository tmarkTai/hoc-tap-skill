# PHA 0 — Thiết lập thương hiệu

Mục tiêu: trước khi làm bất kỳ ebook nào, có **một Hồ sơ thương hiệu** và **một bản mẫu ebook đã duyệt**.
Mọi ebook và trang thư viện về sau đều dựng từ hồ sơ này.

## 1. Câu hỏi (hỏi trong một lượt)

| # | Hỏi | Bắt buộc | Ghi chú |
|---|---|---|---|
| 1 | Tên thương hiệu / công ty | ✔ | Hiện ở bìa, footer, tiêu đề tab |
| 2 | Khẩu hiệu (tagline) | | Dòng nhỏ ở footer |
| 3 | Người biên soạn + chức danh | ✔ | Ô "Biên soạn & hệ thống hóa" trên bìa |
| 4 | Logo nền tối + logo nền sáng | | PNG nền trong suốt / SVG. Thiếu bản nền sáng → dùng chung một bản nếu đủ tương phản, không thì dùng chữ |
| 5 | Ba màu thương hiệu | ✔ | Nền chủ đạo · Nhấn 1 · Nhấn 2 (mã hex) — hoặc chọn bảng gợi ý ở mục 3 |
| 6 | Tên trợ lý + xưng hô | | Ví dụ "Híp", xưng "em", gọi "anh" |
| 7 | Tên miền thư viện | | `learn.tencongty.com` hoặc "chưa có" (dùng tạm `xxx.netlify.app`) |
| 8 | Sản phẩm muốn gắn CTA | | Tên chương trình + link đăng ký; có thể "để sau" |

Người dùng gửi logo dạng ảnh trong chat → lưu file, chuyển data URI. Gửi ảnh chụp bộ nhận diện → đọc mã màu
từ đó và xác nhận lại hex với họ.

## 2. Ánh xạ màu vào template

Template giữ tên biến lịch sử; ý nghĩa thật như sau:

| Biến CSS | Vai trò | Lấy từ |
|---|---|---|
| `--navy-900` | nền trang (theme tối) | màu nền chủ đạo — **phải đủ tối** (độ sáng < 15%). Màu nền thương hiệu sáng → tự pha tối xuống |
| `--navy-800`, `--card`, `--card-2` | nền phụ | nền chủ đạo sáng hơn 4–10% |
| `--line`, `--line-2` | đường kẻ | nền chủ đạo sáng hơn 15–25% |
| `--red`, `--red-soft` | **nhấn 1**: số chương, vạch đầu phần, tab đang mở | màu nhấn 1 |
| `--gold`, `--gold-soft` | **nhấn 2**: câu chốt, CTA, công thức | màu nhấn 2 |
| `--white`, `--muted`, `--muted-2` | chữ | giữ mặc định, chỉ chỉnh tông nếu nền đổi hẳn sắc |

Theme sáng (`:root[data-theme="light"]`): nền kem `#fdfcf9`, chữ đậm, và **pha tối màu nhấn** cho tới khi
tương phản ≥ 4.5:1 trên nền kem (kiểm bằng công thức WCAG). Đổi màu xong nhớ đổi cả các `rgba(...)` gold/red
cứng trong CSS (viền `.cta`, `.bigcta`, `.wow`, `tr.hi`) sang màu mới.

## 3. Bảng màu gợi ý (khi người dùng chưa có)

| Tên | Nền | Nhấn 1 | Nhấn 2 | Hợp với |
|---|---|---|---|---|
| Navy – Đỏ – Vàng | `#060f22` | `#e11d2a` | `#f4b423` | đào tạo, kinh doanh |
| Rêu – Cam đất | `#0d1a14` | `#e0673a` | `#d9c27a` | lifestyle, F&B |
| Than – Xanh ngọc | `#0c1116` | `#16b3a3` | `#f2c14e` | công nghệ, AI |
| Mận – Hồng san hô | `#1a0d16` | `#ff5a6e` | `#f6c28b` | làm đẹp, nữ |

## 4. Lưu hồ sơ

Mẫu ở `assets/brand.example.json`. Lưu thành tài liệu `hoc-tap-brand.md`:

````
# Hồ sơ thương hiệu — skill Học tập
```json
{ ...nội dung brand.json đã điền, "configured": true ... }
```
Logo: (data URI dài để ở file riêng hoặc đính kèm Project)
````

Thứ tự nơi lưu: Project knowledge (`project_write`) → thư mục người dùng (Cowork) → giao file cho họ tự giữ.
Logo data URI dài → lưu file ảnh riêng cạnh hồ sơ, không nhét vào memory.

## 5. Bản mẫu cần duyệt

Dựng `Mau_Ebook_<Brand>.html` từ `assets/ebook-template.html`, thay mọi `{{...}}`:

| Placeholder | Giá trị |
|---|---|
| `{{BRAND_NAME}}` | tên thương hiệu |
| `{{BRAND_TAGLINE}}` | khẩu hiệu (trống → xoá dòng) |
| `{{EDITOR_NAME}}` / `{{EDITOR_TITLE}}` | người biên soạn / chức danh |
| `{{LOGO_DARK}}` / `{{LOGO_LIGHT}}` | data URI logo. Không có logo → xoá `.mlogo`, giữ `.wordmark` |
| `{{LIBRARY_URL}}` | `https://<domain>/` hoặc xoá link "← Thư viện" nếu chưa có |

Sau khi dựng: kiểm tra render cả hai theme → giao file → "Anh/chị xem bản mẫu thương hiệu này, ổn thì mình
bắt đầu chép bài nhé." Chưa duyệt thì sửa tiếp, chưa sang PHA 1.
