# Lỗi thường gặp

## Cài đặt

**Upload zip báo "invalid" / "missing SKILL.md"**
Trong zip phải có đúng thư mục `hoc-tap/` và bên trong là `SKILL.md`. Nếu bạn giải nén rồi tự nén lại, hãy nén
**thư mục `hoc-tap`** (không nén các file bên trong, không nén cả repo).

**Không thấy mục Skills**
Bật *Code execution and file creation* trước (Settings → Capabilities). Gói Team/Enterprise: nhờ quản trị viên
bật *Skills* trong Organization settings.

**Gõ "học tập" nhưng Claude trả lời bình thường**
Kiểm tra công tắc skill `hoc-tap` đang bật. Gõ rõ hơn: "dùng skill hoc-tap để ghi lại buổi học".

## Khi làm ebook

**Claude cứ hỏi lại thương hiệu mỗi lần**
Hồ sơ chưa được lưu bền. Cách khắc phục: làm việc trong một **Project** (Claude lưu `hoc-tap-brand.md` vào
Project), hoặc điền sẵn `assets/brand.json` rồi cài lại zip.

**Ebook dài bị cắt giữa chừng / hết lượt**
Chia buổi: xuất từng chương, nói "thêm chương 2 vào ebook". Gói Pro/Max ít bị giới hạn hơn.

**Chữ viết tay hiện thành font có chân**
Máy người đọc không tải được Google Fonts (mất mạng / mạng công ty chặn). Mở lại khi có mạng.

**Không đọc được link Google Drive ghi âm / NotebookLM**
Bình thường — Google chặn đọc tự động. Tải file về rồi kéo vào chat, hoặc dán transcript.

**Link YouTube không lấy được nội dung**
Cài tiện ích **Claude in Chrome**; livestream vừa xong thường chưa có phụ đề, đợi vài giờ.

## Khi đăng web

**"Không có công cụ Netlify"**
Kết nối connector Netlify và bật nó trong cuộc trò chuyện. Hoặc dùng cách thủ công (docs/ten-mien-netlify.md mục D).

**Deploy xong mất các bài cũ**
Chỉ xảy ra khi kéo-thả thủ công một thư mục thiếu bài. Khôi phục: tab **Deploys** → chọn bản deploy trước →
**Publish deploy**.

**Build lỗi "Không tải được trang chủ"**
Site đang lỗi hoặc tên miền chưa chạy. Kiểm tra `site_url` mà Claude dùng (thử `xxx.netlify.app` thay cho tên
miền riêng). Lúc build lỗi, site cũ vẫn giữ nguyên — không mất gì.

**Điện thoại vẫn hiện bản cũ**
Kéo xuống để tải lại, hoặc mở tab ẩn danh.
