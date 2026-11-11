#!/usr/bin/env bash
# Chạy TRÊN NETLIFY (không chạy ở sandbox). Sao chép nguyên trạng site đang chạy,
# rồi chỉ thêm/thay đúng bài học trong lesson/ — các bài khác giữ nguyên.
set -euo pipefail
SITE=$(python3 -c "import json;print(json.load(open('lesson.json'))['site_url'].rstrip('/'))")
FIRST=$(python3 -c "import json;print(bool(json.load(open('lesson.json')).get('first_deploy')))")
HOST=${SITE#*://}; HOST=${HOST%%/*}
echo "Site: $SITE (host $HOST) · first_deploy=$FIRST"

rm -rf dist && mkdir -p dist
( cd dist && wget -q -r -l 2 -np -nH -e robots=off --domains="$HOST" --reject-regex '\?' "$SITE/" ) || true

if [ "$FIRST" = "True" ]; then
  if [ -s dist/index.html ] && grep -q 'class="card"' dist/index.html; then
    echo "Site đã có bài — bỏ first_deploy trong lesson.json rồi deploy lại. Dừng để giữ site cũ."; exit 1
  fi
  [ -s library-starter/index.html ] || { echo "Thiếu library-starter/index.html"; exit 1; }
  rm -rf dist && mkdir -p dist && cp -r library-starter/. dist/
  echo "Khởi tạo thư viện từ library-starter/"
else
  [ -s dist/index.html ] || { echo "Không tải được trang chủ $SITE — dừng để giữ site cũ"; exit 1; }
  echo "Đã sao chép site hiện tại:"; find dist -type f | sed 's/^/  /'
fi

python3 publish.py
mkdir -p dist/_src && cp dist/index.html dist/_src/index.html.txt
