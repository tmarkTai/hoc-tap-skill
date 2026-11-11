# Skill "Học tập" cho Claude — Biến buổi học thành Ebook & Thư viện web

> Chép bài → Claude dựng **ebook HTML đẹp, đúng thương hiệu của bạn** → đăng lên **thư viện bài học** với
> tên miền riêng (ví dụ `learn.tencongty.com`).

**Tải nhanh:** [⬇️ hoc-tap.zip](hoc-tap.zip) — file để cài vào Claude.

---

## Mục lục

1. [Skill này làm được gì](#1-skill-này-làm-được-gì)
2. [Cần chuẩn bị gì](#2-cần-chuẩn-bị-gì)
3. [Cần tải gì về máy](#3-cần-tải-gì-về-máy)
4. [Cài skill vào Claude (5 phút)](#4-cài-skill-vào-claude-5-phút)
5. [Kết nối thêm (connectors)](#5-kết-nối-thêm-connectors)
6. [Thiết lập thương hiệu — bắt buộc lần đầu](#6-thiết-lập-thương-hiệu--bắt-buộc-lần-đầu)
7. [Cách dùng hằng ngày](#7-cách-dùng-hằng-ngày)
8. [Thư viện web + tên miền riêng](#8-thư-viện-web--tên-miền-riêng)
9. [Lỗi thường gặp](#9-lỗi-thường-gặp)
10. [Cấu trúc repo](#10-cấu-trúc-repo)

---

## 1. Skill này làm được gì

| Pha | Bạn làm | Claude làm |
|---|---|---|
| **0 · Thương hiệu** (1 lần) | Trả lời vài câu: tên, logo, 3 màu, tên miền | Lập Hồ sơ thương hiệu + dựng **bản mẫu ebook** để bạn duyệt |
| **1 · Ghi nhận** | Chép bài, gửi ảnh bảng/slide, dán transcript | Ghi nhận ngắn gọn, hỏi lại chỗ mơ hồ — **chưa dựng gì** |
| **2 · Xuất ebook** | Nói "xong rồi, xuất file" | Dựng **1 file HTML**: bìa, tab chương, sơ đồ vẽ tay, checklist hành động, nút nền Sáng/Tối, trang kết (CTA nếu là sản phẩm của bạn) |
| **3 · Lên web** | Nói "đăng lên web" | Đưa bài vào thư viện trên Netlify, **giữ nguyên các bài cũ** |

Nguyên tắc cứng: nội dung **trung thành 100% với người dạy**, không bịa số liệu, không gắn CTA bán hàng
lên nội dung của diễn giả bên ngoài.

---

## 2. Cần chuẩn bị gì

| Hạng mục | Bắt buộc? | Ghi chú |
|---|---|---|
| Tài khoản **Claude** (claude.ai) | ✔ | Gói **Pro / Max / Team / Enterprise** khuyến nghị (gói Free dùng được skill nhưng giới hạn lượt, ebook dài dễ hết lượt) |
| Bật **Code execution and file creation** (*Create and edit files*) | ✔ | Skill cần quyền này để dựng file HTML |
| Bật **Skills** | ✔ | Team/Enterprise: chủ tổ chức (Owner) phải bật ở *Organization settings* |
| Tài khoản **Netlify** (miễn phí) | Cho Pha 3 | [app.netlify.com/signup](https://app.netlify.com/signup) — đăng ký bằng Google/GitHub |
| **Tên miền** riêng | Tùy chọn | Không có vẫn dùng được địa chỉ miễn phí `ten-ban.netlify.app` |
| Logo PNG nền trong suốt (2 bản: cho nền tối & nền sáng) | Tùy chọn | Không có logo → Claude dùng tên thương hiệu dạng chữ |
| Mã màu thương hiệu (hex) | Tùy chọn | Không có → chọn 1 trong 4 bảng màu gợi ý |

---

## 3. Cần tải gì về máy

| Phần mềm | Bắt buộc? | Tải ở đâu | Để làm gì |
|---|---|---|---|
| **Trình duyệt** (Chrome, Edge, Safari) | ✔ | — | Dùng claude.ai, mở file ebook |
| **Claude Desktop** (Mac/Windows) | Khuyến nghị | [claude.ai/download](https://claude.ai/download) | Dùng chế độ Cowork: Claude đọc/ghi file trong thư mục máy bạn (ví dụ tự lưu ebook vào Downloads) |
| **Google Chrome + tiện ích Claude in Chrome** | Tùy chọn | Chrome Web Store → tìm "Claude" | Đọc phụ đề/transcript YouTube của buổi học |
| **Claude Code** (cho dân kỹ thuật) | Tùy chọn | [docs.claude.com](https://docs.claude.com/en/docs/claude-code/overview) | Dùng skill trong terminal |

Không cần cài Python, Node hay font — Claude chạy mọi thứ trong môi trường của nó. Font chữ (Be Vietnam Pro,
Caveat) tải từ Google Fonts khi người đọc mở ebook.

---

## 4. Cài skill vào Claude (5 phút)

### Bước 1 — Tải file

Bấm [**hoc-tap.zip**](hoc-tap.zip) → nút **Download raw file** (biểu tượng ⬇ góc phải). **Không giải nén.**

### Bước 2 — Bật quyền

1. Vào **claude.ai** → ảnh đại diện góc trái dưới → **Settings** → **Capabilities**.
2. Bật **Code execution and file creation** (bản giao diện mới gọi là **Create and edit files**).

### Bước 3 — Tải skill lên

1. Vào **Customize** → **Skills**.
2. Bấm **+** → **+ Create skill** → **Upload a skill**.
3. Chọn file `hoc-tap.zip` vừa tải.
4. Bật công tắc của skill **hoc-tap**.

> Claude Desktop dùng chung tài khoản claude.ai — cài một lần là dùng được ở web, Desktop và app điện thoại.

### Bước 4 — Kiểm tra

Mở cuộc trò chuyện mới, gõ: **`học tập`** → Claude phải hỏi bạn về **thương hiệu** (Pha 0). Thấy vậy là cài đúng.

### Cách khác — Claude Code

```bash
curl -L -o hoc-tap.zip https://github.com/tmarkTai/hoc-tap-skill/raw/main/hoc-tap.zip
mkdir -p ~/.claude/skills && unzip -o hoc-tap.zip -d ~/.claude/skills/
```

### (Khuyến nghị) Tạo Project riêng

Trên claude.ai tạo **Project** tên "Học tập" và luôn chép bài trong Project đó. Claude sẽ lưu **Hồ sơ thương
hiệu** và **sổ ghi chép từng khóa** vào Project → phiên sau không phải khai báo lại.

---

## 5. Kết nối thêm (connectors)

Vào **Settings → Connectors** (hoặc **Customize → Connectors**) → **Browse connectors**.

| Connector | Cần khi | Cách kết nối |
|---|---|---|
| **Netlify** | Pha 3 — đăng bài lên thư viện tự động | Tìm "Netlify" → **Connect** → đăng nhập Netlify → **Authorize** |
| **Claude in Chrome** | Lấy transcript YouTube | Cài tiện ích trên Chrome, đăng nhập cùng tài khoản Claude |
| **Google Drive** | Đọc tài liệu văn bản (Docs, PDF) trên Drive | Tìm "Google Drive" → Connect. *Lưu ý: không đọc được file ghi âm* |

Không kết nối Netlify vẫn đăng web được — Claude sẽ đưa file zip và hướng dẫn **kéo-thả thủ công** (mục 8).

---

## 6. Thiết lập thương hiệu — bắt buộc lần đầu

Skill **không dựng ebook nào** khi chưa có Hồ sơ thương hiệu. Lần đầu gõ `học tập`, Claude hỏi:

1. Tên thương hiệu, khẩu hiệu
2. Tên người biên soạn + chức danh (hiện trên bìa ebook)
3. Logo nền tối + logo nền sáng (kéo ảnh vào chat)
4. 3 màu: **nền chủ đạo · màu nhấn 1 · màu nhấn 2** — hoặc chọn bảng gợi ý
5. Tên trợ lý & cách xưng hô (ví dụ trợ lý "Híp", xưng "em", gọi "anh")
6. Tên miền thư viện (hoặc "chưa có")
7. Sản phẩm muốn gắn lời mời cuối ebook (hoặc "để sau")

Claude dựng **bản mẫu ebook** theo thương hiệu → bạn duyệt → mới bắt đầu chép bài.
Muốn đổi sau này: gõ **"cập nhật thương hiệu cho skill học tập"**.

**Cho cả team dùng chung một thương hiệu:** giải nén zip → điền `hoc-tap/assets/brand.json` theo mẫu
`brand.example.json`, đặt `"configured": true`, bỏ logo vào cùng thư mục → nén lại thư mục `hoc-tap` thành
zip → gửi cho team cài. Không ai phải trả lời Pha 0 nữa.

---

## 7. Cách dùng hằng ngày

```
Bạn:    học tập — nay mình học workshop "Quản trị dòng tiền" của thầy B
Claude: Dạ, mời anh chép tới đâu gửi tới đó…
Bạn:    [dán ghi chép] [gửi ảnh bảng] [dán transcript]
Claude: Đã ghi nhận… (hỏi lại chỗ mơ hồ: hiểu A hay B?)
Bạn:    xong rồi, xuất file
Claude: [giao Ebook_Quan_Tri_Dong_Tien_<Brand>.html]
Bạn:    ok, đăng lên web
Claude: Đã đăng: https://learn.tencongty.com/quan-tri-dong-tien/
```

**Câu lệnh hay dùng**

| Muốn | Gõ |
|---|---|
| Bắt đầu buổi mới | `học tập` · `nay mình học…` |
| Xuất ebook | `xong rồi` · `xuất file đi` |
| Thêm buổi 2 vào cùng ebook | `buổi 2 của khóa X` (Claude gộp thành chương mới trong cùng 1 file) |
| Đăng / cập nhật web | `đăng lên web` · `update bài lên thư viện` |
| Đổi thương hiệu | `cập nhật thương hiệu cho skill học tập` |

**Mẹo:** ảnh bảng chụp thẳng, đủ sáng; gửi transcript dạng text là nhanh nhất; file ghi âm thì tải thẳng lên
chat (Claude tự bóc lời nếu môi trường cho phép, khoảng 15–20 phút cho 1 giờ audio).

---

## 8. Thư viện web + tên miền riêng

Chi tiết từng bước có ảnh minh họa chữ: **[docs/ten-mien-netlify.md](docs/ten-mien-netlify.md)**. Tóm tắt:

1. **Tạo tài khoản Netlify** miễn phí, kết nối connector Netlify trong Claude.
2. Lần đầu gõ **"đăng lên web"** → Claude hỏi tên site (ví dụ `learn-tencongty`) → tạo site + trang chủ
   "Thư viện bài học" → web chạy ngay ở `https://learn-tencongty.netlify.app`.
3. **Gắn tên miền** (làm tay 1 lần, ~5 phút):
   - Netlify → site → **Domain management** → **Add a domain** → nhập `learn.tencongty.com` → **Verify** → **Add domain**.
   - Vào nơi bạn mua tên miền (Mắt Bão, PA Việt Nam, Tenten, iNET, GoDaddy, Squarespace, Cloudflare…)
     → **Quản lý DNS** → thêm bản ghi:

     | Loại | Host / Tên | Giá trị / Trỏ tới | TTL |
     |---|---|---|---|
     | `CNAME` | `learn` | `learn-tencongty.netlify.app` | mặc định |

   - Chờ 5–60 phút → Netlify tự cấp **HTTPS** miễn phí.
4. Báo Claude tên miền đã chạy → Claude lưu vào Hồ sơ thương hiệu, các lần sau đăng thẳng.

**Không có connector Netlify?** Giữ một thư mục `thu-vien/` trên máy. Mỗi bài mới Claude đưa bạn thư mục bài
+ trang chủ đã cập nhật → bỏ vào `thu-vien/` → kéo **cả thư mục** vào ô *Drag and drop* ở tab **Deploys** của site.

---

## 9. Lỗi thường gặp

Xem đầy đủ: **[docs/loi-thuong-gap.md](docs/loi-thuong-gap.md)**.

| Hiện tượng | Cách xử lý |
|---|---|
| Upload zip báo lỗi | Đúng file `hoc-tap.zip` từ repo, **không giải nén rồi nén lại sai cấp** (trong zip phải là thư mục `hoc-tap/` chứa `SKILL.md`) |
| Gõ "học tập" mà Claude không dùng skill | Kiểm tra công tắc skill đã bật + đã bật *Code execution*; thử gõ "dùng skill hoc-tap" |
| Claude không tạo được file | Chưa bật *Code execution and file creation* |
| Đăng web báo không có Netlify | Chưa kết nối connector Netlify, hoặc chưa bật nó trong cuộc trò chuyện (biểu tượng ⚙/🔌 dưới ô chat) |
| Tên miền không vào được | DNS chưa cập nhật (chờ tới 1 giờ); Cloudflare phải để đám mây **xám**; kiểm tra Host chỉ ghi `learn`, không ghi cả tên miền |
| Ebook thiếu font đẹp | Font tải từ Google Fonts — cần có mạng khi mở file |

---

## 10. Cấu trúc repo

```
README.md                   ← hướng dẫn này
hoc-tap.zip                 ← file cài vào Claude. Giải nén ra thư mục hoc-tap/:
  hoc-tap/SKILL.md            quy trình 4 pha
  hoc-tap/references/         brand-setup · design-system · cta-playbook · publish-web · transcribe
  hoc-tap/assets/             ebook-template.html · brand.example.json · library-starter/ · web-publish/
docs/
  ten-mien-netlify.md       ← hướng dẫn chi tiết Netlify + tên miền
  loi-thuong-gap.md
```

**Cập nhật skill:** tải `hoc-tap.zip` mới → Customize → Skills → xoá bản cũ → upload bản mới.
