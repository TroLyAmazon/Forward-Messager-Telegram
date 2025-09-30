# Telegram Message Forwarder 🚀

Forward tin nhắn từ link Telegram (ví dụ: `https://t.me/channel/123`) đến nhiều group hoặc channel khác, giữ nguyên:

- ✅ Emoji
- ✅ Caption
- ✅ Hình ảnh, video
- ✅ Định dạng chữ (bold, italic, link...)

### ⚙️ Công nghệ

- [Telethon](https://github.com/LonamiWebs/Telethon) – client API cho Telegram
- Python 3.8+
- `.env` để bảo mật API key

---

## 📦 Cài đặt

### 1. Cài thư viện

```bash
pip install telethon python-dotenv
```

### 2. Tạo app Telegram

Truy cập: https://my.telegram.org

- Chọn **API Development Tools**
- Tạo app và ghi lại:
  - `API_ID`
  - `API_HASH`

---

## 🛠 Cấu trúc file

```text
project/
│
├── forward_telethon.py       # Script chính
├── .env                      # Chứa API_ID, API_HASH
├── groups.json               # Danh sách group/channel đích
```

### 📄 `.env` ví dụ

```env
API_ID=1234567
API_HASH=abcd1234efgh5678
SESSION_NAME=forward_session
```

### 📄 `groups.json` ví dụ

```json
[
    -1001234567890,
    -1009876543210
]
```

---

## ▶️ Chạy script

```bash
python forward_telethon.py
```

Sau đó nhập:

```text
https://t.me/tenkenh/123
```

> Lần đầu sẽ yêu cầu đăng nhập số điện thoại và nhập mã Telegram (lưu session vào file `.session` để dùng lại sau)

---

## 🔁 Gửi lại tin nhắn như thế nào?

Script sử dụng:


✔️ Giữ nguyên mọi nội dung và định dạng như tin nhắn gốc

---

## ⚠️ Lưu ý

- Tin nhắn phải **tồn tại**
- Channel gốc phải **public**
- Tài khoản Telegram của bạn phải **xem được** channel và tin đó
- Group đích phải cho phép bạn gửi tin

---

## 📌 Kế hoạch mở rộng

- [ ] Forward realtime khi có tin nhắn mới
- [ ] Giao diện web (Flask)
- [ ] Tích hợp thành Telegram bot (nhận lệnh `/forward <link>`)

---

## 📜 Giấy phép

MIT License

---

## 🙌 Credits

- [Telethon](https://github.com/LonamiWebs/Telethon)
