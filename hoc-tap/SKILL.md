---
name: hoc-tap
description: 'Quy trình "Học tập → Ebook → Lên web": biến ghi chép, ảnh bảng/slide, record hoặc transcript một buổi học, workshop, hội thảo thành EBOOK HTML một file theo nhận diện thương hiệu của người dùng, rồi đăng lên thư viện bài học riêng (Netlify + tên miền). DÙNG khi người dùng nói "học tập", "skill học tập", "nay mình học...", "ghi lại bài học", gửi ảnh whiteboard/slide/record/transcript buổi học, nói "hệ thống lại buổi học", "đóng gói thành ebook", "làm tài liệu tặng khách", "đăng lên web", "đưa bài lên thư viện", hoặc "thiết lập thương hiệu cho skill học tập". Lần đầu dùng phải chạy PHA 0 thiết lập thương hiệu trước khi dựng bất kỳ ebook nào.'
---

# Skill "Học tập" — Học · Đóng gói Ebook · Đăng lên thư viện

## Skill này để làm gì

Người dùng đi học / dự workshop rất nhiều. Skill này biến ghi chép của họ thành **một cuốn ebook HTML hoàn
chỉnh** mang thương hiệu của họ — không phải biên bản lớp học. Ebook phục vụ ba việc cùng lúc:

1. **Học** — ôn lại và nhớ được
2. **Đóng gói** — thành tài sản tri thức để gửi đi, đào tạo lại đội ngũ
3. **Chuyển đổi** — làm **quà tặng có giá trị thật**; cuối ebook có thể có CTA dẫn vào sản phẩm của chính họ

Bốn pha: **PHA 0** thiết lập thương hiệu (một lần) → **PHA 1** ghi nhận notes → **PHA 2** xuất ebook →
**PHA 3** đăng lên thư viện web.

## Xưng hô & ngôn ngữ

- Lấy **tên trợ lý** và **cách xưng hô** trong Hồ sơ thương hiệu (`assistant_name`, `xung_ho`).
  Chưa có hồ sơ → xưng "em", gọi người dùng "anh/chị" cho tới khi họ chọn.
- Trao đổi bằng **tiếng Việt**; thuật ngữ quan trọng để **song ngữ VN/EN**. Ngắn gọn, đi thẳng vào việc.

---

## PHA 0 — THIẾT LẬP THƯƠNG HIỆU (bắt buộc trước khi dựng template)

**Không dựng ebook nào khi chưa có Hồ sơ thương hiệu.** Đây là luật của skill: template phải chuẩn thương
hiệu người dùng trước, rồi mới tới bài học và trang thư viện.

### Bước 0.1 — Tìm hồ sơ đã có (theo thứ tự)

1. File `assets/brand.json` (nếu có) trong skill với `"configured": true` → dùng luôn (team đã điền sẵn trước
   khi nén zip; logo nằm cùng thư mục `assets/`).
2. Tài liệu **`hoc-tap-brand.md`** trong Project (claude.ai Projects) hoặc trong thư mục làm việc.
3. Bộ nhớ (memory) có ghi hồ sơ thương hiệu cho skill này.
4. Không thấy → chạy Bước 0.2.

Người dùng nói "đổi thương hiệu", "cập nhật logo/màu" → chạy lại 0.2 và ghi đè hồ sơ.

### Bước 0.2 — Hỏi và lập hồ sơ

Đọc **`references/brand-setup.md`**. Hỏi gọn trong **một lượt** (AskUserQuestion nếu có, không thì liệt kê
câu hỏi đánh số):

- Tên thương hiệu / công ty · khẩu hiệu (tagline) · tên người biên soạn và chức danh
- Logo: bản cho nền tối + bản cho nền sáng (PNG/SVG). Không có logo → dùng chữ (wordmark)
- 3 màu: **nền chủ đạo**, **màu nhấn 1** (số chương, vạch), **màu nhấn 2** (câu chốt, CTA) — hoặc chọn một
  bảng màu gợi ý trong `brand-setup.md`
- Tên trợ lý + xưng hô
- Tên miền thư viện (ví dụ `learn.tencongty.com`) hoặc "chưa có" — được phép để trống, điền sau
- Sản phẩm/chương trình của họ có muốn gắn CTA bán hàng không (có thể trả lời "để sau")

### Bước 0.3 — Lưu và dựng bản mẫu

1. Ghi hồ sơ theo mẫu `assets/brand.example.json` thành **`hoc-tap-brand.md`** (khối JSON bên trong):
   ưu tiên lưu vào Project (`project_write`), không có Project thì giao file cho người dùng và dặn họ
   đưa vào Project knowledge hoặc dán lại ở lần sau.
2. Dựng **`Mau_Ebook_<Brand>.html`** từ `assets/ebook-template.html`: thay placeholder `{{...}}`, đổi hex
   màu trong `:root` theo hồ sơ (xem `references/design-system.md` mục 1 và 8), nhúng logo data URI.
3. Kiểm tra render (mục KIỂM TRA) và **xin người dùng duyệt bản mẫu**. Duyệt xong mới sang PHA 1/2.

---

## PHA 1 — GHI NHẬN (lắng nghe, chưa dựng gì)

Chào một câu ngắn, mời người dùng chép bài tự nhiên, chép tới đâu gửi tới đó. Với **mỗi mẩu notes**:

1. **Ghi nhận ngắn gọn** — xác nhận đã nắm, diễn giải lại 1–2 câu. KHÔNG bình luận dài, KHÔNG dựng HTML,
   KHÔNG mở rộng kiến thức.
2. **Ảnh whiteboard/slide**: đọc kỹ chữ viết tay, sơ đồ, mũi tên, **màu mực** (màu người dạy dùng thường có
   dụng ý). Chữ khó đọc → nêu cách hiểu và mời người dùng chỉnh.
3. **Đánh dấu riêng**: câu chốt · công thức/framework · ví dụ · con số cụ thể · bài tập sau buổi · thuật ngữ đắt.
4. **Câu gõ vội bị thiếu/ngược nghĩa**: KHÔNG tự sửa im lặng — nêu 2 cách hiểu (A)/(B), hỏi chọn, nhưng
   **không chặn dòng chảy**: vẫn mời chép tiếp, treo câu hỏi lại.
5. Kết mỗi lần bằng "Mời anh/chị chép tiếp, em vẫn đợi." (theo xưng hô trong hồ sơ).

Buổi dài hoặc sẽ gửi thêm tư liệu sau → **lưu notes vào Project/memory** để phiên sau làm tiếp.

### Tín hiệu chuyển PHA 2

"buổi học kết thúc", "xong rồi", "xuất file đi", "triển luôn", "hết rồi". Câu na ná cũng là tín hiệu.

---

## PHA 2 — XUẤT EBOOK

Chưa rõ thì hỏi nhanh **một lần**: mục đích (tự học / tặng khách / đào tạo) · có CTA bán hàng không.
Đã nói rõ trước đó thì làm luôn.

### Bốn nguyên tắc bắt buộc

**1. Viết cho NGƯỜI ĐỌC, không phải cho người ghi chép.** Giọng "bạn". Không "thầy nói rằng…", không
"buổi này mình học được…".

**2. KHÔNG đưa chuyện hậu trường vào ebook.** Bỏ hết: "ghi chú của trợ lý", "chỗ này em hiệu đính",
"cần xác nhận", mục "phần còn để mở". Mọi thắc mắc **hỏi trong chat**. Ebook chỉ chứa nội dung hoàn chỉnh.

**3. Mỗi chương khép bằng CTA HÀNH ĐỘNG.** Khối `.cta`: tiêu đề mệnh lệnh · 3–4 việc làm được ngay trong
tuần có checkbox · mỗi việc kèm một **câu hỏi tự soi** in nghiêng.

**4. Trang cuối:** có sản phẩm của chính người dùng → **trang CTA chuyển đổi** (đọc `references/cta-playbook.md`).
Không có → trang Kết gồm 3 việc làm ngay + bộ câu chốt cả khóa.

### Cấu trúc ebook chuẩn

```
BÌA          → tên ebook · phụ đề · người dạy · người biên soạn · dành cho ai (logo thương hiệu)
THANH CHƯƠNG → sticky, chuyển Chương 1 · 2 · … · Kết + nút đổi nền Sáng/Tối (KHÔNG dùng file rời)
CHƯƠNG n     → mở chương (số lớn viết tay + tiêu đề + dẫn nhập) → TOC dính bên trái
               → các phần nội dung → CTA checklist cuối chương → nút "Chương tiếp theo →"
TRANG KẾT    → bắc cầu cảm xúc → (bằng chứng/slide) → 3 việc làm ngay → khối CTA lớn hoặc câu chốt
FOOTER       → logo + người biên soạn + 1 dòng nguồn gốc tài liệu
```

**MỘT FILE DUY NHẤT** cho cả chuỗi nhiều buổi (file rời thì link tương đối gãy khi mở từ chat).
Tên file: `Ebook_<ChuDe>_<Brand>.html`.

### Nguyên tắc NỘI DUNG (bất di bất dịch)

1. **Nội dung lõi = 100% ý người dạy.** Hệ thống hóa, viết lại mạch lạc — nhưng **không tự thêm** kiến thức
   ngoài. Giữ nguyên ví dụ, công thức, câu chốt, thuật ngữ gốc và **mọi con số cụ thể**.
2. **Muốn bổ sung kiến thức ngoài → hỏi duyệt trước** bằng một menu có nguồn. Người dùng gật mục nào mới đưa vào.
3. Nguồn phải **thật** — không chắc thì nói "cần kiểm chứng", không bịa tác giả/năm.
4. **Hiệu đính tên riêng nghe sai** từ record (thương hiệu, tên người, thuật ngữ nước ngoài — ví dụ
   "Philip Cotler" → **Philip Kotler**) và **báo trong chat**, không ghi vào ebook. Sửa tên riêng và chính tả
   thì được, **không sửa ý**. Hồ sơ thương hiệu có thể có bảng `ten_rieng` để dùng.

### Đạo đức khi làm CTA — BẮT BUỘC

- **Nội dung của diễn giả bên ngoài**: ghi rõ nguồn tác giả trên bìa và footer, **không gắn CTA bán hàng**
  lên nội dung người khác; trang Kết thay bằng câu tự chấm + câu chốt. Nội dung pháp lý/thuế/tài chính thêm
  dòng "tham khảo, kiểm tra với chuyên gia".
- Chỉ làm CTA cho **sản phẩm của chính người dùng / công ty họ**.
- **Mọi con số do người dùng cung cấp** — giá, cọc, quyền lợi, mốc thưởng. Không suy đoán, không làm tròn,
  không tự thêm ưu đãi.
- **QR / thông tin chuyển khoản**: chỉ đưa vào khi người dùng xác nhận; ebook gửi ra ngoài có QR → hỏi một lần.
- Cam kết kiểu "hoàn cọc", "thu nhập X" **phải ghi đủ điều kiện kèm theo**.

### Chuỗi nhiều buổi

- Một file cho cả chuỗi, tab chuyển chương; ID neo có tiền tố chương (`#c2-s1`).
- Chương ≥ 2 mở bằng đoạn **nối mạch từ chương trước**.
- Giữ nguyên design tokens qua các chương.
- **Sổ chuỗi** trong Project/memory (`project_khoa_<ten>.md`): thông tin khóa · trạng thái từng buổi · câu hỏi
  đang treo · quyết định format đã chốt. **Đầu mỗi buổi mới, đọc sổ này trước.**

---

## Cách DỰNG FILE

File HTML đơn, tự chứa: inline CSS + JS, logo và ảnh nhúng data URI. **Đọc `references/design-system.md`
trước khi code** và bám khung `assets/ebook-template.html` (đã có đủ component, JS tab chương, nút đổi nền).

### Nút đổi nền Sáng / Tối — bắt buộc

Ba điểm dễ sai nhất:
- Selector tab chương phải là `.chapbar button:not(.themebtn)`.
- Mọi màu chữ trắng viết `color:var(--white)`, không `color:#fff`.
- `.fg-wrap` (khung sơ đồ SVG) **giữ nền tối ở cả hai theme**.

### Trông phải THẬT, không "mùi AI"

**Tránh**: gradient tím/cầu vồng · hộp bo góc lớn xếp đều · mọi thứ căn giữa · emoji rắc khắp nơi · box
chồng box · font Inter · card nào cũng glow · fade-in từng khối.
**Nên**: căn trái có nhịp · nền giấy kẻ ô mờ · bảng kẻ dòng thay card màu · trích dẫn vạch trái chữ lớn ·
sơ đồ vẽ tay bằng SVG.

### Hình ảnh

1. **Ảnh chụp bảng người dạy vẽ, nếu đủ nét** → dùng thẳng (chân thực nhất).
2. **Vẽ lại bằng SVG nét tay** khi ảnh mờ — giữ đúng bố cục, màu mực, cách viết tắt; chú giải ở `figcaption`.

Nén ảnh: JPEG 1400–1500px, quality 84–88; **slide có QR để quality 92**.

---

## KIỂM TRA trước khi giao

Render bằng Playwright/Chromium (nếu môi trường có), chụp: bìa · từng sơ đồ · một CTA · một section dày
chữ · bản mobile 414px. Soát: tiếng Việt có dấu · logo rõ · không chữ chồng nhau trong SVG · bảng không tràn ·
ảnh không lỗi · tab chương chạy đúng · **bật nền sáng soát lại**: không chữ trắng trên nền trắng, logo đổi
bản nền sáng, đổi nền không mất chương đang mở. Rà `grep -o 'color:#fff[;}]' file.html` phải rỗng.

Môi trường chặn Google Fonts → ảnh QA hiện font thay thế, không phải lỗi; nói rõ với người dùng.

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1280,"height":940})
    pg.goto("file:///duong/dan/ebook.html"); pg.wait_for_timeout(1200)
    pg.click(".chapbar button[data-p='c2']"); pg.wait_for_timeout(500)
    pg.screenshot(path="check.png"); b.close()
```

---

## Khi người dùng gửi RECORD / transcript

Đọc **`references/transcribe.md`**. Tóm tắt: dán text vào chat là tốt nhất · link YouTube → dùng Claude in
Chrome đọc phụ đề · file ghi âm → bóc lời bằng `faster-whisper` nếu môi trường cho phép · link Google Drive
âm thanh / NotebookLM thường không đọc tự động được → nói thật, nhờ người dùng tải file lên hoặc dán text.
Bản chép lời nhiễu: chỉ đưa ý chắc chắn; con số/tên nghe không rõ → hỏi trong chat.

---

## GIAO HÀNG

1. Giao file HTML (SendUserFile / present_files / tải về) kèm một câu tóm tắt.
2. Có kết nối máy tính (Cowork) → lưu thêm vào thư mục người dùng chọn (mặc định `~/Downloads`).
3. Sau khi giao, **hỏi các điểm còn treo** trong chat.
4. Người dùng duyệt → **PHA 3**.

### Khối "Tư liệu gốc" (ghi âm + slide) — khi người dùng muốn kèm

- Đặt **ngay dưới bìa**, nút ở bìa là link neo `href="#tu-lieu"`.
- **Bản gửi chat (1 file):** `<audio controls src="data:audio/mp4;base64,…">`, PDF là
  `<a download href="data:application/pdf;base64,…">`. Không giải mã base64 bằng JS lúc mở trang (điện thoại đơ).
  Nén ghi âm: `ffmpeg -ac 1 -ar 22050 -c:a aac -b:a 24k`.
- **Bản web:** tư liệu là file riêng trong `/<slug>/`.
- Buổi riêng tư / có giọng học viên → nhắc xin phép diễn giả trước khi đăng công khai.

---

## PHA 3 — ĐĂNG LÊN THƯ VIỆN WEB

Thư viện = một site Netlify: trang chủ liệt kê bài, mỗi bài một trang con `/<slug>/`. Tên miền lấy từ hồ sơ
(`library.domain`). **Đọc `references/publish-web.md` trước khi deploy.** Ba điều bắt buộc:

- **Không bao giờ deploy một thư mục chỉ chứa bài mới** — deploy Netlify thay toàn bộ site, sẽ xoá thư viện và
  các bài khác. Dùng bộ build `assets/web-publish/`: Netlify tự sao chép site đang chạy rồi chỉ thêm/thay bài này.
- Bài đã có trên web → lấy bản đang chạy làm gốc, gộp chỉnh sửa, không ghi đè mù.
- Kiểm tra `summary` của deploy: số file thay đổi phải đúng dự kiến.

Chưa có site → làm **lần khởi tạo** theo `publish-web.md` mục "Lần đầu". Không có Netlify connector → giao zip
thư mục bài + hướng dẫn kéo thả (mục "Cách thủ công").

---

## Tóm tắt 1 dòng

Chưa có hồ sơ thương hiệu → PHA 0 trước → lắng nghe chép hết bài (PHA 1) → ebook một file, trung thành 100%
ý người dạy, viết cho người đọc, mỗi chương có CTA hành động (PHA 2) → kiểm tra render → giao file → hỏi điểm
treo trong chat → đăng lên thư viện (PHA 3).
