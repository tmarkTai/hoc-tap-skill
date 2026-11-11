# Thư viện bài học trên Netlify + tên miền riêng

Làm một lần, dùng mãi. Tổng thời gian ~15 phút (chưa tính thời gian chờ DNS).

## A. Tạo tài khoản & kết nối

1. Vào [app.netlify.com/signup](https://app.netlify.com/signup) → đăng ký bằng Google hoặc GitHub (gói **Free** là đủ:
   100 GB băng thông/tháng, HTTPS miễn phí).
2. Trong Claude: **Settings → Connectors → Browse connectors** → tìm **Netlify** → **Connect** → đăng nhập →
   **Authorize**.
3. Trong cuộc trò chuyện, bấm biểu tượng công cụ dưới ô chat để chắc chắn Netlify đang **bật**.

## B. Tạo thư viện (Claude làm)

Gõ: **"đăng lên web"** (hoặc "tạo thư viện bài học").
Claude sẽ:
1. Hỏi tên site — chỉ chữ thường, số, gạch nối, ví dụ `learn-tencongty`.
2. Tạo site trên Netlify, dựng trang chủ **Thư viện bài học** theo màu thương hiệu.
3. Đăng bài đầu tiên → báo link `https://learn-tencongty.netlify.app/<ten-bai>/`.

Từ lần sau, mỗi bài mới chỉ **thêm** vào thư viện; các bài cũ giữ nguyên.

## C. Gắn tên miền riêng

Bạn cần sở hữu một tên miền (ví dụ `tencongty.com`). Nên dùng **tên miền con** như `learn.tencongty.com`
để không ảnh hưởng website chính.

### C1. Trên Netlify

1. app.netlify.com → chọn site → **Domain management** (hoặc *Site configuration → Domain management*).
2. **Add a domain** → nhập `learn.tencongty.com` → **Verify** → **Add domain**.
3. Netlify hiện cảnh báo "Awaiting External DNS" kèm giá trị CNAME — đó là `<ten-site>.netlify.app`.

### C2. Tại nơi quản lý DNS

Thêm **một** bản ghi:

| Loại | Host / Name | Value / Target | TTL |
|---|---|---|---|
| CNAME | `learn` | `learn-tencongty.netlify.app` | Auto / 3600 |

Đường đi theo nhà cung cấp:

| Nhà cung cấp | Vào đâu |
|---|---|
| **Mắt Bão** | Quản lý dịch vụ → Tên miền → Quản lý DNS |
| **PA Việt Nam** | Quản lý tên miền → Cấu hình DNS / Bản ghi |
| **Tenten / iNET / Nhân Hòa** | Quản lý tên miền → Quản lý bản ghi DNS |
| **GoDaddy** | My Products → Domain → **DNS** → Add New Record |
| **Squarespace Domains** | Domains → chọn tên miền → **DNS** → Custom records → Add record |
| **Cloudflare** | DNS → Records → Add record — **bấm tắt đám mây cam thành xám (DNS only)** |
| **Namecheap** | Domain List → Manage → **Advanced DNS** → Add new record |

Lưu ý:
- Ô Host chỉ ghi `learn`, **không** ghi `learn.tencongty.com` (nhiều nơi tự nối thêm tên miền).
- Một số nơi yêu cầu Value có dấu chấm cuối: `learn-tencongty.netlify.app.`
- Đã có bản ghi `learn` khác (A hoặc CNAME) → xoá bản cũ trước.

### C3. Chờ & kiểm tra

- Thường 5–30 phút, tối đa vài giờ. Kiểm tra tại [dnschecker.org](https://dnschecker.org) (chọn CNAME).
- Netlify tự cấp chứng chỉ **HTTPS (Let's Encrypt)**. Nếu sau 1 giờ vẫn chưa có: Domain management →
  **HTTPS** → **Verify DNS configuration** → **Provision certificate**.
- Xong → nói với Claude: *"tên miền learn.tencongty.com đã chạy"* để Claude lưu vào Hồ sơ thương hiệu.

### Muốn dùng tên miền chính (không có `learn.`)

Dùng tên miền gốc `tencongty.com` sẽ đè lên website chính — chỉ làm khi tên miền đó dành riêng cho thư viện.
Netlify sẽ hướng dẫn trỏ bản ghi **A** về load balancer của họ hoặc đổi nameserver sang Netlify DNS.

## D. Đăng thủ công (không có connector)

1. Trên máy tạo thư mục `thu-vien/`.
2. Mỗi lần Claude giao: thư mục bài `<slug>/` + `index.html` trang chủ mới → chép vào `thu-vien/` (thay file cũ).
3. app.netlify.com → site → tab **Deploys** → kéo **cả thư mục `thu-vien/`** vào ô *Drag and drop*.

⚠️ Kéo riêng một bài sẽ **xoá mọi bài khác** — Netlify thay toàn bộ site mỗi lần deploy.
