import re
import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import MessageIdInvalidError

# Load .env
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "forward_session")

# Load danh sách group/channel đích
with open("groups.json", "r", encoding="utf-8") as f:
    group_ids = json.load(f)

def extract_chat_and_msg_id(link):
    match = re.match(r"https://t\.me/([^/]+)/(\d+)", link)
    if match:
        return match.group(1), int(match.group(2))
    return None, None

async def main():
    input_link = input("🔗 Nhập link tin nhắn Telegram (VD: https://t.me/snpforward/7): ").strip()
    chat_username, message_id = extract_chat_and_msg_id(input_link)

    if not chat_username or not message_id:
        print("❌ Link không hợp lệ")
        return

    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        try:
            # Test lấy tin nhắn (không cần lấy nội dung)
            await client.get_messages(chat_username, ids=message_id)

            for group_id in group_ids:
                try:
                    # Forward nguyên gốc: giữ emoji, định dạng, ảnh, caption
                    await client.forward_messages(
                        entity=group_id,
                        messages=message_id,
                        from_peer=chat_username
                    )
                    print(f"✅ Forward tới {group_id} thành công")
                except Exception as e:
                    print(f"⚠️ Lỗi gửi tới {group_id}: {e}")

        except MessageIdInvalidError:
            print("❌ Không tìm thấy tin nhắn")
        except Exception as e:
            print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
