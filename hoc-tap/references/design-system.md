# Design System — Ebook "Học tập"

Đọc file này trước khi code. Mục tiêu: ebook trông như **một cuốn sách được biên tập tử tế**, KHÔNG có "mùi
template AI". Khung code chuẩn ở `assets/ebook-template.html`. Màu mặc định dưới đây là bảng **Navy – Đỏ – Vàng**; đổi theo Hồ sơ thương hiệu (xem `brand-setup.md` mục 2).

## 0. Nguyên tắc trên hết

**Tránh**: gradient tím/cầu vồng · hộp bo góc lớn xếp đều tăm tắp · mọi thứ căn giữa · emoji rắc khắp nơi ·
box màu chồng box · font Inter · card nào cũng glow · fade-in từng khối.

**Nên**: căn trái có nhịp · nền giấy kẻ ô mờ · bảng kẻ dòng thay card màu · trích dẫn bằng vạch trái + chữ
lớn · dùng nền/viền tiết chế · sơ đồ vẽ tay bằng SVG hoặc ảnh bảng gốc.

## 1. Tokens

```css
:root{
  --navy-900:#060f22; --navy-800:#0a1a38; --line:#1d3763; --line-2:#16294c;
  --red:#e11d2a; --red-soft:#ff3b47;
  --gold:#f4b423; --gold-soft:#ffd15c;
  --white:#f2f6ff; --muted:#9fb2d4; --muted-2:#6f83a8;
  --card:#0b1a39; --card-2:#0d2047; --aqua:#4a9ae0; --green:#5fcf8a;
  --paper:rgba(255,255,255,.028);
  --hand:'Caveat','Bradley Hand','Noteworthy','Segoe Script',cursive;
}
```

**Nền trang** — giấy kẻ ô mờ, chi tiết tạo cảm giác "bảng học":
```css
body{background:
  linear-gradient(var(--paper) 1px,transparent 1px) 0 0/100% 30px,
  linear-gradient(90deg,var(--paper) 1px,transparent 1px) 0 0/30px 100%,
  radial-gradient(1100px 520px at 82% -8%,#122a52 0%,transparent 62%),
  var(--navy-900);}
```

Quy tắc màu: **đỏ** cho số chương, vạch nhấn, cảnh báo. **Gold** cho câu chốt, CTA, điểm nhấn. **muted** cho
diễn giải. **aqua** chỉ khi tái hiện nét mực xanh của thầy. **green** cho "Quả"/kết quả.

## 2. Font

- Thân bài: **Be Vietnam Pro**. KHÔNG dùng Inter. Body 16.5px, line-height 1.75 (đọc dài).
- Chữ viết tay: **Caveat** + **fallback macOS bắt buộc** — thiếu fallback thì rơi về serif rất xấu.

```html
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">
```
Trong SVG: `font-family="Caveat, Bradley Hand, Noteworthy, Segoe Script, cursive"`.

## 3. Logo

Logo lấy từ Hồ sơ thương hiệu (bản nền tối + bản nền sáng). Chuyển sang data URI:
```bash
python3 -c "import base64;print('data:image/png;base64,'+base64.b64encode(open('logo-dark.png','rb').read()).decode())"
```
Không có logo → dùng `.wordmark` (tên thương hiệu dạng chữ) có sẵn trong template.
```css
.mlogo{background-image:url("data:image/png;base64,...");background-repeat:no-repeat;
  background-position:left center;background-size:contain;}
```

## 4. Component ebook

**`#progress`** — fixed 3px đỏ đặc, KHÔNG gradient.

**`.chapbar`** — thanh chương sticky `top:0`, `backdrop-filter:blur(10px)`. Mỗi nút có `.d` (nhãn nhỏ viết
hoa: "Chương 2 · 21/08") + tên chương. Nút đang mở: chữ trắng, `border-bottom` đỏ. Nút trang CTA cuối
(`.cta`) dùng vạch **gold** để phân biệt.

**`.panel-ch`** — `display:none`, thêm `.on` để hiện. JS toggle + `window.scrollTo(0,0)`.

**`.chap-open`** — mở chương: số lớn viết tay (`font-size:56px`, màu đỏ) → `h2` `clamp(27px,4.6vw,42px)` có
một cụm `<em>` tô gold → đoạn dẫn nhập.

**`nav.toc`** — sticky `top:74px` (dưới chapbar), link kẻ vạch trái, active đổi vạch sang đỏ.

**`.sh`** — đầu phần: `border-top:2px solid var(--red)` + nhãn nhỏ viết hoa + `h3`.

**Bảng kẻ dòng** — dùng thay card cho mọi danh sách có cấu trúc: `border-bottom:1px solid var(--line-2)`,
`td.n` là số thứ tự đỏ đậm, `tr.hi` nhấn nền đỏ nhạt.

**`blockquote`** — vạch trái gold 3px, chữ 20px (`.big` thì `clamp(21px,3vw,28px)`). `.red` cho luận điểm mạnh.

**`.wow`** — hộp công thức: nền radial gold mờ, viền gold, căn giữa, các vế tô màu khác nhau
(`.p1` trắng · `.p2` đỏ · `.res` gradient gold).

**`.duo`** — hai vế so sánh trong một khung viền chung, ngăn bằng đường kẻ dọc. `.pos`/`.neg` cho đúng/sai.

**`.chain`** — chuỗi logic, mỗi dòng mũi tên `▸` gold, ngăn bằng dotted.

**`.steps`** — dải bước ngang, ô ngăn bằng `gap:1px`, tên bước dùng font viết tay.

**`.panel`** — viền mảnh, bo 4px, nhãn `.pt` chữ nhỏ viết hoa. Chỉ dùng cho ví dụ/case cụ thể, **đừng lạm dụng**.

### ⭐ `.cta` — CTA cuối chương (component quan trọng nhất)

```css
.cta{border:1px solid rgba(244,180,35,.4);border-radius:6px;
  background:linear-gradient(160deg,rgba(244,180,35,.07),rgba(11,26,57,.8));padding:30px 30px 26px;margin:44px 0 10px;}
.todo li{position:relative;padding:12px 0 12px 42px;border-bottom:1px solid rgba(255,255,255,.07);}
.todo li:before{content:"";position:absolute;left:6px;top:16px;width:16px;height:16px;
  border:1.5px solid var(--gold);border-radius:3px;}          /* ô checkbox */
.todo li span.q{display:block;font-size:13.5px;color:var(--muted-2);margin-top:3px;font-style:italic;}
```
Nội dung: nhãn "Việc của bạn sau chương N" → tiêu đề mệnh lệnh → 3–4 việc có checkbox → mỗi việc kèm
**câu hỏi tự soi** in nghiêng.

### ⭐ `.bigcta` — khối chốt bán hàng cuối ebook

Viền gold đậm hơn (`.5`), nền gradient gold, căn giữa. Gồm: tên chương trình (chữ lớn) → **link đăng ký viết
bằng font tay 30px, gạch chân gold** → dòng hướng dẫn: bước miễn phí trước, rồi cọc, **cú pháp chuyển khoản**,
cách xác nhận.

**`.deck`** — gallery slide chương trình: mỗi `figure` gồm `.shot` (viền mảnh, `overflow:hidden`) + `.cap`
(tiêu đề gold + tóm tắt). `loading="lazy"` cho ảnh.

**`.navrow`** — hàng nút chuyển chương cuối mỗi chương: "← Quay lại" và "Chương tiếp theo →".

## 5. Sơ đồ SVG nét tay

- Khung `.fg-wrap`: nền kẻ ô 26px đậm hơn nền trang + viền mảnh.
- Nét: `stroke-linecap/linejoin:round`, điểm gãy **lệch nhẹ**. Vẽ **đúp đường**: nét chính `3.4`, nét phụ
  `1.5` lệch 3–5px `opacity:.38` — giống bút dạ đi hai lần.
- Đường phân chia = **path lượn sóng**, không dùng `<line>`.
- Ngoặc `{` `}` gom nhóm: path cong (`C`), như thầy khoanh trên bảng.
- **Giữ đúng màu mực** thầy dùng, giải thích ý nghĩa màu trong `figcaption`.
- Giữ **cách viết tắt của thầy** trong hình, chú giải đầy đủ ở caption.
- **Kiểm tra chồng chữ**: nhãn cạnh nhau rất dễ đè lên nhau — xoay bằng
  `transform="rotate(-90 x y)"` hoặc dời ra chỗ trống.

## 6. JS tối thiểu

- Progress bar theo scroll.
- Tab chương: toggle `.on` + `scrollTo(0,0)`.
- TOC active bằng `IntersectionObserver`, `rootMargin:'-25% 0px -60% 0px'`.
- **KHÔNG localStorage/sessionStorage.** Không thư viện ngoài.

## 7. Responsive

Grid về 1 cột ở màn hẹp; ẩn TOC dưới 980px; `h1` dùng `clamp()`; `.chapbar .in` cho `overflow-x:auto`.
Kiểm tra ~1280px và ~414px.

---

## 8. ⭐ THEME SÁNG / TỐI — bắt buộc có

Mọi ebook phải có **nút đổi nền** để người đọc chọn. Mặc định là **nền tối**; nền sáng dành cho
người đọc lâu, đọc ngoài sáng, hoặc in ra giấy.

### 8.1 Nút toggle

Đặt ở **góc phải thanh chương** (`.chapbar`) — sticky nên luôn với tới được. Không đặt ở bìa vì cuộn xuống
là mất.

```css
.themebtn{margin-left:auto;align-self:center;flex:none;display:inline-flex;align-items:center;gap:8px;
  background:none;border:1px solid var(--line-2);border-radius:999px;color:var(--muted);
  font-family:inherit;font-size:12px;font-weight:600;padding:7px 14px;cursor:pointer;transition:.18s;white-space:nowrap;}
.themebtn:hover{color:var(--white);border-color:var(--muted-2);}
@media(max-width:640px){.themebtn .tx{display:none;} .themebtn{padding:7px 10px;}}
```
```html
<button class="themebtn" id="themebtn" type="button" aria-label="Đổi nền sáng tối">
  <span class="ic">☀</span><span class="tx">Nền sáng</span></button>
```
```js
var tb=document.getElementById('themebtn'), light=false;
tb.addEventListener('click', function(){
  light=!light;
  document.documentElement.setAttribute('data-theme', light?'light':'dark');
  tb.querySelector('.ic').textContent = light?'☾':'☀';
  tb.querySelector('.tx').textContent = light?'Nền tối':'Nền sáng';
});
```
**KHÔNG lưu lựa chọn vào localStorage** — dùng biến JS, mặc định tối mỗi lần mở.

⚠️ Selector chọn tab chương phải loại nút này ra:
`document.querySelectorAll(".chapbar button:not(.themebtn)")` — không thì bấm đổi nền sẽ làm mất chương.

### 8.2 Palette sáng

Nền **kem ấm `#fdfcf9`**, không dùng trắng lóa `#ffffff` — đọc dài đỡ mỏi mắt và hợp chất "giấy in sách".

```css
:root[data-theme="light"]{
  --navy-900:#fdfcf9; --navy-800:#f4f6fa;
  --line:#c9d2e2; --line-2:#e3e8f1;
  --red:#c9151f; --red-soft:#d81f2b;
  --gold:#c08c07; --gold-soft:#8a6206;      /* gold nhạt không đọc được trên nền sáng */
  --white:#16233d; --muted:#55637f; --muted-2:#8090aa;
  --card:#ffffff; --card-2:#f7f9fd; --aqua:#2f7cc0; --green:#2f9c62;
  --paper:rgba(20,35,70,.035);
  --bg-panel:rgba(247,249,253,.9); --bg-cta:rgba(255,255,255,.92); --bg-bar:rgba(253,252,249,.96);
  --bg-step:#ffffff; --bg-shot:#f2f2ea; --sep:rgba(20,35,70,.09); --dot:rgba(20,35,70,.14);
}
:root[data-theme="light"] .mlogo{background-image:url("...logo-nen-sang...");}  /* đổi sang logo bản nền sáng */
```

Kiểm chứng tương phản (WCAG AA cần ≥ 4.5:1 cho chữ thường):
chữ chính **15.2:1** · chữ vàng **5.3:1** · chữ phụ **5.9:1**.

### 8.3 Token phụ — phải có từ đầu

Đừng hardcode màu nền vào component, nếu không lúc làm theme sáng sẽ phải sửa khắp nơi. Khai báo sẵn
trong `:root`:

```css
--bg-panel: /* nền .panel */    --bg-cta:  /* nền .cta, .bigcta */
--bg-bar:   /* nền .chapbar */  --bg-step: /* nền ô .steps */
--bg-shot:  /* nền khung ảnh */ --sep:     /* đường kẻ .todo li */
--dot:      /* đường dotted .chain */
```

### 8.4 ⚠️ Lỗi hay gặp: `color:#fff` hardcode

Ở theme sáng, `--white` đổi thành **màu chữ đậm** `#16233d`. Nên **mọi chỗ dùng màu chữ trắng phải viết
`color:var(--white)`**, không được viết `color:#fff`. Quên chỗ nào là chỗ đó **chữ trắng trên nền trắng**,
mất hẳn nội dung.

Rà trước khi giao:
```bash
grep -o 'color:#fff[;}]' file.html    # phải ra rỗng
```
Các chỗ hay quên: `.sub b` · `blockquote p` · `strong` · `td b` · `nav.toc a.active` ·
`.chapbar button.on` · `.wow .eq .p1` · `.navrow button:hover`.

### 8.5 Sơ đồ SVG giữ nền tối ở cả hai theme

Nét vẽ tay dùng màu sáng (hồng nhạt, vàng nhạt) — đưa lên nền trắng là mất chữ. Vì vậy **`.fg-wrap` giữ
nền tối `#081533` kể cả ở theme sáng**, chỉ đổi màu viền cho hợp:

```css
:root[data-theme="light"] .fg-wrap{border-color:#1d3763;}
```

Kết quả: sơ đồ trông như **một tấm bảng đen đóng khung trong trang sách trắng** — đọc rõ và thành điểm nhấn.
Ảnh chụp bảng gốc (nền giấy kem) thì hợp cả hai theme, không cần xử lý.

### 8.6 Kiểm tra theme sáng trước khi giao

```python
pg.click("#themebtn"); pg.wait_for_timeout(600)
# dò phần tử chữ quá sáng trên nền sáng
bad = pg.evaluate("""() => {
  const out=[];
  document.querySelectorAll('p,li,td,strong,blockquote p').forEach(e=>{
    const m=getComputedStyle(e).color.match(/\\d+/g); if(!m) return;
    const [r,g,b]=m.map(Number);
    if((0.2126*r+0.7152*g+0.0722*b)/255 > 0.72 && e.textContent.trim().length>3)
      out.push(e.textContent.trim().slice(0,40));
  });
  return out.slice(0,10);
}""")
assert bad == [], bad
```
Và kiểm tra: bấm đổi nền **không làm mất chương đang mở**, logo đổi đúng bản, tab vẫn chuyển được.
