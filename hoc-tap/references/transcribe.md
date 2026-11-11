# Khi người dùng gửi RECORD / transcript

Thứ tự ưu tiên — chọn cách nhanh nhất có thể, nói thật khi không làm được, đừng loay hoay.

1. **Dán thẳng text vào chat** → tốt nhất, dùng luôn.
2. **File .txt / .docx / .pdf transcript** tải lên chat → đọc trực tiếp.
3. **Link YouTube** → WebFetch thường bị chặn. Dùng **Claude in Chrome** (nếu đã cài):
   `tabs_context_mcp` → `navigate` tới video → mở "Hiện bản chép lời" → `get_page_text`.
   Livestream vừa kết thúc thường **chưa có phụ đề** — báo người dùng, đừng chờ.
4. **Link Google Drive / NotebookLM** chứa âm thanh → connector chỉ đọc văn bản, Google chặn truy cập tự động.
   Nhờ người dùng tải file về rồi gửi lên, hoặc dán text.
5. **File trên máy** (bản Cowork / Desktop): xin quyền thư mục `~/Downloads` hoặc `~/Desktop`
   (`~/Documents` hay bị từ chối). Nhanh nhất: nhờ người dùng kéo file vào Downloads.

## Bóc lời file ghi âm (nâng cao — khi môi trường có Python + ffmpeg)

```bash
pip install faster-whisper --break-system-packages   # nếu chưa có
```

- Model: Whisper **small** là đủ cho tiếng Việt rõ giọng; `medium` chính xác hơn nhưng chậm gấp ~2,5 lần.
  Nếu huggingface bị chặn, thử nguồn model khác mà mạng cho phép (ví dụ gói npm đóng gói model CTranslate2)
  và **đối chiếu checksum** trước khi dùng.
- Thư viện `av` có thể lệch phiên bản → giải mã bằng ffmpeg ra mảng float32 rồi truyền mảng:

```python
import subprocess, numpy as np
from faster_whisper import WhisperModel
raw = subprocess.run(["ffmpeg","-i","buoi-hoc.m4a","-f","s16le","-ac","1","-ar","16000","-"],
                     capture_output=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
model = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio, language="vi", beam_size=1, vad_filter=True,
                           initial_prompt="Tên diễn giả, tên thương hiệu, thuật ngữ chủ đề")
open("transcript.txt","w").write("\n".join(s.text.strip() for s in segs))
```

- Tốc độ tham khảo: ~3–4× thời gian thực trên 1 CPU (1 giờ audio ≈ 15–20 phút). Chạy nền bằng
  `setsid nohup python3 bocloi.py > log.txt 2>&1 &` và theo dõi file output.
- Bản chép lời luôn nhiễu: chỉ đưa vào ebook ý chắc chắn; con số/tên nghe không rõ → hỏi trong chat.
