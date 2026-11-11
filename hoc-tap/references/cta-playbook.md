# Playbook — Trang CTA cuối ebook (chuyển đổi bán hàng)

Phần này biến ebook từ tài liệu học thành **công cụ bán hàng tự động**. Đọc kỹ trước khi viết trang cuối.

## Nguyên lý

Ebook là **quà tặng có giá trị thật**. Người đọc nhận được kiến thức dùng được ngay — rồi mới tới lời mời.
Các chương đầu **tạo tin tưởng**; trang cuối **kích hoạt nhu cầu**.

Không bán vội. Không nhét CTA vào giữa chương. Người đọc phải thấy giá trị trước.

## Cấu trúc ba lớp

### Lớp 1 — Bắc cầu cảm xúc

Một đoạn ngắn nối từ nội dung sang lời mời, **dùng chính câu chốt trong bài** để bắc cầu. Không bịa cảm xúc,
không dọa dẫm.

> "Ba chương vừa rồi cho bạn đủ bản đồ. Nhưng bản đồ không đưa ai tới đích. Thứ đưa người ta tới đích là
> môi trường có người kèm, có số liệu, có đội đi cùng — đúng như câu ở chương 1: *con người là sản phẩm của
> môi trường*."

Công thức: **[tóm tắt giá trị đã trao] + [khoảng trống còn lại] + [câu chốt trong bài làm bản lề]**.

### Lớp 2 — Bằng chứng

Nhúng **slide chương trình do người dùng cung cấp** trong `.deck`. Thứ tự trình bày theo mạch thuyết phục, KHÔNG
theo thứ tự được gửi:

1. **Lộ trình / phương pháp** — cho thấy có hệ thống
2. **Bậc thang kết quả** — cho thấy đi tới đâu
3. **Giá trị & chi phí** — cho thấy đáng tiền
4. **Bước vào miễn phí** — hạ rào cản
5. **Mốc thưởng** — tạo động lực dài hạn

Mỗi slide kèm `.cap`: tiêu đề gold + một câu tóm tắt, để người đọc lướt nhanh không cần phóng to ảnh.

### Lớp 3 — Lời mời cụ thể

Khối `.cta` với ba việc theo thứ tự **miễn phí → cam kết thấp → cam kết chính**:

```
1. [Miễn phí, 2 phút]     Đăng ký nhận tài liệu / tham gia cộng đồng
2. [Tự làm, 1 buổi]       Làm bài tập đầu tiên trong ebook và chia sẻ kết quả
3. [Cam kết chính]        Tham gia chương trình — phí X, nhận Y, điều kiện Z (số do chủ sản phẩm cung cấp)
```

Rồi khối `.bigcta`: tên chương trình · link đăng ký · **cú pháp chuyển khoản đầy đủ** · cách xác nhận.

## ⚠️ Quy tắc đạo đức — BẮT BUỘC

- Chỉ làm CTA cho **sản phẩm của chính người dùng / công ty người dùng**. Không làm CTA hộ bên thứ ba.
- **Mọi con số phải do người dùng cung cấp**: giá, cọc, quyền lợi, mốc thưởng, tỷ lệ hoàn.
  **Không suy đoán, không làm tròn, không tự thêm ưu đãi.** Nghe không rõ → hỏi lại trong chat.
- Cam kết kiểu "hoàn cọc 100%", "thu nhập X triệu" **phải ghi kèm đủ điều kiện** — không cắt vế điều kiện
  cho lời văn gọn hơn. Đây là ranh giới giữa marketing và hứa hão.
- **QR thanh toán**: chỉ giữ khi người dùng xác nhận. Nếu ebook gửi ra ngoài mà có QR, hỏi người dùng một lần trước khi dựng.
- Phân biệt rõ **ai là người mua gì**: đừng nhầm sản phẩm người đọc tham gia với sản phẩm họ được quyền bán
  lại sau này. Sai chỗ này là sai toàn bộ lời mời. *(Ví dụ lỗi hay gặp: nhầm chương trình học viên tham gia với gói
  sản phẩm mà học viên được quyền bán lại.)*

## Checklist trước khi giao trang CTA

- [ ] Ba chương trước có đủ giá trị đứng độc lập, không đọc như quảng cáo trá hình?
- [ ] Mọi con số đều do người dùng cung cấp, không có số nào trợ lý tự suy ra?
- [ ] Cam kết nào cũng có điều kiện kèm theo?
- [ ] Slide sắp theo mạch thuyết phục, mỗi slide có caption?
- [ ] Ba việc đi từ miễn phí → cam kết chính?
- [ ] Link và cú pháp chuyển khoản chính xác từng ký tự?
- [ ] Không còn ghi chú hậu trường nào lọt vào trang cuối?
