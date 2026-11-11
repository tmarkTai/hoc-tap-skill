# PHA 3 — Đăng ebook lên thư viện web (Netlify)

Đọc hết trước khi deploy. Thông tin site lấy từ Hồ sơ thương hiệu (`library.*`).

## Mô hình

| Mục | Giá trị |
|---|---|
| Trang chủ | "Thư viện bài học" — liệt kê các bài, bài mới lên đầu (bài ghim `pinned_slug` luôn trên cùng) |
| Mỗi bài | thư mục con `/<slug>/index.html` (+ tư liệu đi kèm) |
| Tên miền | `library.domain` trong hồ sơ, ví dụ `learn.tencongty.com`; chưa có → `<site>.netlify.app` |
| Nút về thư viện | mỗi bài có link "← Thư viện" về trang chủ |

## ⚠️ Bẫy lớn nhất: deploy = THAY TOÀN BỘ site

Sandbox mỗi phiên chat đều trống — không có mã nguồn các bài cũ. Deploy một thư mục chỉ có bài mới →
**trang Thư viện và mọi bài khác bị xoá**.

**Cách giải:** deploy bộ build nhỏ `assets/web-publish/`. Netlify chạy `build.sh` trên máy chủ của họ
(có internet): **wget sao chép nguyên trạng site đang chạy**, rồi `publish.py` chỉ thêm/thay đúng bài mới.
Build lỗi → site cũ giữ nguyên.

## Chuẩn bị bản web của ebook (khác bản gửi chat)

- Tư liệu nặng (ghi âm, PDF) để **file riêng**, link bằng đường dẫn tuyệt đối `/<slug>/ten-file.m4a`.
- Thêm link `← Thư viện` về `https://<domain>/` ở footer.
- Bài đã có trên web → web_fetch bản đang chạy để soi, gộp chỉnh sửa trước khi đẩy.
- `slug`: chữ thường không dấu, gạch nối (`quan-tri-dong-tien`).

## Thư mục deploy

```
learnup/
  netlify.toml  build.sh  publish.py       ← copy từ assets/web-publish/
  lesson.json                              ← từ lesson.example.json, điền site_url + slug + thẻ bài
  lesson/index.html  lesson/<tư liệu>      ← trang bài
  library-starter/index.html               ← CHỈ ở lần đầu (first_deploy: true)
```

## Lần đầu (site chưa có gì)

1. Chưa có site → hỏi người dùng tên site rồi gọi Netlify `create-new-project` (name dạng `learn-tencongty`).
   **Không bao giờ tự tạo site mới khi chưa hỏi.** Lưu `siteId` + tên site vào hồ sơ thương hiệu.
2. Dựng `library-starter/index.html` từ `assets/library-starter/index.html`: thay `{{BRAND_NAME}}`,
   `{{LIBRARY_TITLE}}`, `{{BRAND_TAGLINE}}`, màu `:root` và logo theo hồ sơ. Giữ nguyên dòng
   `<!-- LESSONS -->` — `publish.py` chèn thẻ bài ngay sau dòng này.
3. `lesson.json` đặt `"first_deploy": true`. `build.sh` sẽ dùng trang khởi tạo thay vì sao chép.
   An toàn: nếu site đã có nội dung thì build tự dừng, không ghi đè.
4. Deploy (bước dưới). Lần sau **bỏ** `first_deploy` và thư mục `library-starter/`.
5. Nhắc người dùng gắn tên miền (hướng dẫn ở `docs/ten-mien-netlify.md` trong repo, tóm tắt ở cuối file này).

## Deploy

1. Gọi Netlify `deploy-site` với `siteId` → nhận lệnh `npx -y @netlify/mcp@latest --site-id … --proxy-path "…"`.
   Token proxy hết hạn nhanh: **mỗi lần deploy gọi lại tool lấy lệnh mới**.
2. Chạy trong thư mục deploy:
   `cd learnup && timeout 600 npx -y @netlify/mcp@latest … 2>&1 | grep -v "npm " | tail -6`
3. Kiểm tra: `get-deploy-for-site` với deployId → đọc `summary.messages`: số file thay đổi phải đúng dự kiến
   (ví dụ "2 new files uploaded … <slug>/index.html"). Số file lớn bất thường → kiểm lại ngay.
   web_fetch có thể trả bản cache cũ vài phút — đừng kết luận lỗi chỉ vì thế.
4. Báo người dùng: link bài, những gì đã thêm, các trang khác giữ nguyên.

## Cách thủ công (không có Netlify connector)

Người dùng giữ một thư mục `thu-vien/` trên máy = toàn bộ site (index.html + các thư mục bài).
Mỗi bài mới: giao zip `<slug>/` + file `index.html` trang chủ đã chèn thẻ bài → người dùng giải nén vào
`thu-vien/` → kéo **cả thư mục** `thu-vien/` vào ô "Drag and drop" ở tab **Deploys** của site trên
app.netlify.com. Nhắc rõ: kéo cả thư mục, không kéo riêng bài mới.

## Lưu ý nội dung khi đăng công khai

- Buổi riêng tư, ghi âm có giọng học viên, slide gốc của diễn giả → nhắc xin phép diễn giả trước.
- Bỏ các chữ "nội bộ", thông tin chuyển khoản/QR nếu chưa được xác nhận cho bản public.

## Tóm tắt gắn tên miền

Netlify → site → **Domain management** → **Add a domain** → nhập `learn.tencongty.com` → Verify → Add.
Tại nơi quản lý DNS của tên miền: thêm bản ghi **CNAME**, Host `learn`, Value `<site>.netlify.app`.
Chờ 5–60 phút → Netlify tự cấp HTTPS (Let's Encrypt). Cloudflare: để đám mây **xám** (DNS only).
