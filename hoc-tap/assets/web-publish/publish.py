"""Thêm/cập nhật 1 bài học vào thư viện khi build trên Netlify.
Đọc lesson.json + thư mục lesson/ (index.html và file tư liệu).
Lỗi bất kỳ -> raise -> build fail -> site cũ giữ nguyên."""
import json, os, shutil, html, re, sys

L = json.load(open('lesson.json', encoding='utf-8'))
slug = L['slug']
if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', slug):
    raise SystemExit('slug phải là chữ thường không dấu, gạch nối: %r' % slug)
dst = os.path.join('dist', slug)
is_new = not os.path.exists(os.path.join(dst, 'index.html'))

# 1) Chép trang bài học + tư liệu (ghi đè bản cũ của đúng bài này)
if not os.path.exists(os.path.join('lesson', 'index.html')):
    raise SystemExit('Thiếu lesson/index.html')
os.makedirs(dst, exist_ok=True)
for f in os.listdir('lesson'):
    shutil.copy(os.path.join('lesson', f), os.path.join(dst, f))
print(('Thêm mới' if is_new else 'Cập nhật'), 'bài', slug)

# 2) Thẻ bài trên trang chủ: chỉ thêm khi chưa có
idx_p = 'dist/index.html'
idx = open(idx_p, encoding='utf-8').read()
if f'/{slug}/' in idx:
    print('Trang chủ đã có thẻ bài này — giữ nguyên'); sys.exit(0)

c = L['card']
e = lambda s: html.escape(s or '', quote=True)
MARK = '<!-- LESSONS -->'

if MARK in idx:
    # Cách chuẩn: trang chủ dựng từ library-starter, chèn thẻ ngay sau dấu mốc (bài mới lên đầu)
    card = (f'\n<a class="card" href="/{slug}/">'
            f'<span class="tag">{e(c.get("tag"))}</span>'
            f'<h3>{e(c["title"])}</h3>'
            f'<p>{e(c.get("desc"))}</p>'
            f'<span class="meta">{e(c.get("author"))}{" · " if c.get("author") and c.get("date") else ""}{e(c.get("date"))}</span>'
            f'</a>')
    idx = idx.replace(MARK, MARK + card, 1)
else:
    # Trang chủ cũ không có dấu mốc: nhân bản một thẻ đang có (card_template) rồi thay chữ
    T = L.get('card_template')
    if not T:
        raise SystemExit('Trang chủ không có <!-- LESSONS --> và lesson.json không có card_template')
    m = next(re.finditer(r'<a\b[^>]*href="[^"]*/' + re.escape(T['slug']) + r'/?"[^>]*>.*?</a>', idx, re.S), None)
    if not m:
        raise SystemExit('Không tìm thấy thẻ mẫu /%s/ trên trang chủ' % T['slug'])
    card = m.group(0)
    card = re.sub(r'(href="[^"]*/)' + re.escape(T['slug']) + r'(/?")', r'\g<1>' + slug + r'\2', card)
    for key in ('tag', 'title', 'desc', 'author', 'date'):
        old, new = T[key], c[key]
        for o, n in ((old, new), (html.escape(old, quote=False), html.escape(new, quote=False)),
                     (html.escape(old), html.escape(new))):
            if o in card:
                card = card.replace(o, n); break
        else:
            raise SystemExit('Thẻ mẫu không chứa "%s" (%s) — cập nhật card_template' % (old, key))
    idx = idx[:m.start()] + card + '\n' + idx[m.start():]

open(idx_p, 'w', encoding='utf-8').write(idx)
print('Đã thêm thẻ bài mới lên trang chủ')
