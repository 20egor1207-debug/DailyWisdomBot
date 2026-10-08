import discord
from discord.ext import commands, tasks
import random

# =========================
# НАСТРОЙКИ БОТА
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# Канал для Daily Wisdom
CHANNEL_ID = 1557036467589611645


# =========================
# DAILY WISDOM
# =========================

messages = [
    "🧠 Маленький прогресс каждый день со временем превращается в большой результат.",
    "💡 Ошибки — это не конец. Это способ понять, что делать лучше.",
    "🚀 Даже самый длинный путь начинается с первого шага.",
    "🌟 Не сравнивай свой прогресс с чужим — у каждого свой путь.",
    "📚 Чем больше ты узнаёшь, тем больше понимаешь, сколько ещё можно узнать.",
    "🔥 Иногда лучший способ начать — просто перестать откладывать.",
    "🎯 Цель становится ближе с каждым маленьким действием.",
    "💭 Хорошая идея ничего не стоит, пока ты не начнёшь её реализовывать.",
    "🌍 Мир огромен — всегда есть чему научиться.",
    "⚡ Неудача — это опыт, который можно использовать в следующий раз.",
    "🛠️ Навык появляется не сразу. Его создают практика и время.",
    "🌱 Даже маленькие изменения могут привести к большим результатам.",
    "🧩 Если что-то не получается с первого раза — попробуй другой подход.",
    "💪 Иногда нужно просто продолжать, даже когда результат пока не виден.",
    "🔎 Любопытство — один из лучших способов находить новые идеи.",
    "🎮 Даже в игре победа начинается с понимания правил.",
    "🧠 Самый сильный инструмент — способность учиться.",
    "🚀 Не жди идеального момента — его может не быть.",
    "✨ Каждый день даёт возможность узнать что-то новое.",
    "💡 Иногда простой ответ оказывается самым правильным.",
    "🏆 Большие достижения складываются из маленьких побед.",
    "🌌 Всегда оставляй место для новых идей и возможностей.",
    "🔥 Не бойся начинать заново — теперь у тебя есть опыт.",
    "📖 Знания становятся полезными, когда ты применяешь их на практике.",
    "☀️ Сегодня — хороший день, чтобы сделать хотя бы один шаг вперёд."
]


# =========================
# FACTS
# =========================

facts = [
    "🐙 У осьминога три сердца.",
    "🌍 Земля немного сплюснута у полюсов.",
    "🦈 Акулы появились на Земле раньше деревьев.",
    "🐝 Пчёлы могут различать человеческие лица.",
    "🌌 В космосе звук не распространяется так, как в воздухе.",
    "🦋 Бабочки чувствуют вкус ногами.",
    "🌊 Океаны покрывают большую часть поверхности Земли.",
    "🧠 Человеческий мозг состоит примерно из 86 миллиардов нейронов."
]


# =========================
# 8 BALL
# =========================

eightball_answers = [
    "✅ Да!",
    "❌ Нет!",
    "🤔 Возможно.",
    "🔮 Скорее всего!",
    "😐 Не уверен.",
    "🔥 Определённо!",
    "✨ Всё возможно!",
    "🎯 Шансы довольно высоки!",
    "💀 Лучше не спрашивай...",
    "🧠 Думаю, что да."
]


# =========================
# БОТ ЗАПУЩЕН
# =========================

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")

    if not daily_wisdom.is_running():
        daily_wisdom.start()


# =========================
# АВТОМАТИЧЕСКАЯ МУДРОСТЬ
# =========================

@tasks.loop(hours=24)
async def daily_wisdom():

    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        message = random.choice(messages)

        await channel.send(
            f"🧠 **Daily Wisdom**\n\n{message}"
        )


# =========================
# !PING
# =========================

@bot.command()
async def ping(ctx):

    await ctx.send("🏓 Pong!")

# =========================
# !FACT
# =========================

@bot.command()
async def fact(ctx):

    fact_text = random.choice(facts)

    await ctx.send(
        f"🧠 **Случайный факт**\n\n{fact_text}"
    )


# =========================
# !WISDOM
# =========================

@bot.command()
async def wisdom(ctx):

    wisdom_text = random.choice(messages)

    await ctx.send(
        f"💡 **Мудрость дня**\n\n{wisdom_text}"
    )


# =========================
# !HELPER
# =========================

@bot.command()
async def helpme(ctx):

    embed = discord.Embed(
        title="🤖 Daily Wisdom — Команды",
        description="Вот список доступных команд:"
    )

    embed.add_field(
        name="🏓 !ping",
        value="Проверить, работает ли бот.",
        inline=False
    )

    embed.add_field(
        name="🧠 !fact",
        value="Получить случайный факт.",
        inline=False
    )

    embed.add_field(
        name="💡 !wisdom",
        value="Получить случайную мудрость.",
        inline=False
    )

    embed.add_field(
        name="🏠 !server",
        value="Информация о сервере.",
        inline=False
    )

    embed.add_field(
        name="👤 !user",
        value="Информация о пользователе.",
        inline=False
    )

    embed.add_field(
        name="🎱 !8ball вопрос",
        value="Задать вопрос магическому шару.",
        inline=False
    )

    await ctx.send(embed=embed)


# =========================
# !SERVER
# =========================
@bot.command()
async def server(ctx):

    guild = ctx.guild

    embed = discord.Embed(
        title=f"🏠 {guild.name}",
        description="Информация о сервере"
    )

    embed.add_field(
        name="👥 Участников",
        value=str(guild.member_count),
        inline=True
    )

    embed.add_field(
        name="🆔 ID сервера",
        value=str(guild.id),
        inline=True
    )

    embed.add_field(
        name="📅 Создан",
        value=guild.created_at.strftime("%d.%m.%Y"),
        inline=True
    )

    await ctx.send(embed=embed)


# =========================
# !USER
# =========================
@bot.command()
async def user(ctx):

    embed = discord.Embed(
        title="👤 Информация о пользователе"
    )

    embed.add_field(
        name="👤 Имя",
        value=ctx.author.name,
        inline=False
    )

    embed.add_field(
        name="🆔 ID",
        value=str(ctx.author.id),
        inline=False
    )

    embed.add_field(
        name="📅 Аккаунт создан",
        value=ctx.author.created_at.strftime("%d.%m.%Y"),
        inline=False
    )

    await ctx.send(embed=embed)


# =========================
# !8BALL
# =========================

@bot.command(name="8ball")
async def eightball(ctx, *, question=None):

    if not question:
        await ctx.send(
            "🎱 Напиши вопрос после команды!\n"
            "Например: `!8ball Я сегодня выиграю?`"
        )
        return

    answer = random.choice(eightball_answers)

    await ctx.send(
        f"🎱 **Вопрос:** {question}\n\n"
        f"🔮 **Ответ:** {answer}"
    )


# =========================
# ЗАПУСК БОТА
# =========================

bot.run("???")