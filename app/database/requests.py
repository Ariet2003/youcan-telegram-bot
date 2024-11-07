from typing import Optional
from sqlalchemy.orm import selectinload
from sqlalchemy import or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import async_session
from app.database.models import User, Admin, Question, Notification
from app.users.user import userKeyboards as kb
from bot_instance import bot
from sqlalchemy import select, delete
from datetime import datetime
from sqlalchemy import update
import pytz

# We get the current time in the required time zone
def get_current_time():
    tz = pytz.timezone('Asia/Bishkek')
    return datetime.now(tz)

# Request to check if a user is in the database, if not, then add
async def set_user(telegram_id: str, username: str, name: str, identifier: str, language: str, phone_number: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if not user:
            session.add(User(
                telegram_id=telegram_id,
                username=username,
                name=name,
                identifier=identifier,
                language=language,
                phone_number=phone_number,
                created_at=get_current_time(),
                updated_at=get_current_time()
            ))
            await session.commit()


# Request to check if you are an administrator
async def check_admin(telegram_id: str) -> bool:
    async with async_session() as session:
        result = await session.execute(
            select(Admin).where(Admin.telegram_id == telegram_id)
        )
        admin = result.scalar_one_or_none()

        return admin is not None

# Request to check if you are a user
async def check_user(telegram_id: str) -> bool:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        return user is not None

# Request to check if an admin is in the database, if not, then add
async def set_admin(telegram_id: str, username: str) -> None:
    async with async_session() as session:
        admin = await session.scalar(select(Admin).where(Admin.telegram_id == telegram_id))

        if not admin:
            new_admin = Admin(
                telegram_id=telegram_id,
                username=username,
                created_at=get_current_time(),
                updated_at=get_current_time()
            )
            session.add(new_admin)
            await session.commit()

# Request to get user language
async def get_user_language(telegram_id: str) -> Optional[str]:
    async with async_session() as session:
        result = await session.execute(
            select(User.language).where(User.telegram_id == telegram_id)
        )
        language = result.scalar_one_or_none()

        return language

# Request to get user name
async def get_user_name(telegram_id: str) -> Optional[str]:
    async with async_session() as session:
        result = await session.execute(
            select(User.name).where(User.telegram_id == telegram_id)
        )
        name = result.scalar_one_or_none()

        return name

# Write analogy questions to the DB
async def write_question(user_id: int, subject_id: int, content: str, option_a: str, option_b: str, option_v: str, option_g: str, correct_option: str, status: str = "pending") -> bool:
    async with async_session() as session:
        async with session.begin():
            # Проверка существования вопроса с такими же текстом и вариантами ответов
            existing_question = await session.execute(
                select(Question)
                .where(
                    Question.content == content,
                    Question.option_a == option_a,
                    Question.option_b == option_b,
                    Question.option_v == option_v,
                    Question.option_g == option_g
                )
            )
            # Если вопрос найден, возвращаем False
            if existing_question.scalars().first():
                return False

            # Создаем новый вопрос, так как аналогичного не найдено
            new_question = Question(
                user_id=user_id,
                subject_id=subject_id,
                content=content,
                option_a=option_a,
                option_b=option_b,
                option_v=option_v,
                option_g=option_g,
                correct_option=correct_option,
                status=status,
                created_at=get_current_time()
            )
            session.add(new_question)
            await session.commit()

            # Возвращаем True, чтобы показать, что вопрос был успешно добавлен
            return True

# Update the number of rubies the user has
async def add_rubies(telegram_id: str, rubies_amount: int):
    async with async_session() as session:
        async with session.begin():
            await session.execute(
                update(User)
                .where(User.telegram_id == telegram_id)
                .values(rubies=User.rubies + rubies_amount)
            )
            await session.commit()


# Request to get and review the oldest pending question for a specific subject_id (by largest question_id)
async def get_and_review_oldest_pending_question(subject_id: int) -> Optional[dict]:
    async with async_session() as session:
        # Начинаем транзакцию
        async with session.begin():
            # Запрос для получения самого большого question_id с статусом 'pending' и указанным subject_id
            result = await session.execute(
                select(Question)
                .filter(Question.status == 'pending', Question.subject_id == subject_id)
                .order_by(Question.question_id.desc())  # Сортировка по question_id в убывающем порядке
            )
            question = result.scalars().first()

            if question:
                # После завершения транзакции продолжаем выполнять запросы вне контекста транзакции
                async with async_session() as session:
                    # Обновляем статус вопроса на 'under review'
                    await session.execute(
                        update(Question)
                        .where(Question.question_id == question.question_id)
                        .values(status='under review')
                    )
                    await session.commit()

                return {
                    'question_id': question.question_id,
                    'question_text': question.content,
                    'option_a': question.option_a,
                    'option_b': question.option_b,
                    'option_v': question.option_v,
                    'option_g': question.option_g,
                    'correct_option': question.correct_option
                }

    return None  # Если нет вопросов со статусом 'pending' и указанным subject_id



# General function to update the status of a question
async def update_question_status(question_id: int, status: str) -> bool:
    try:
        async with async_session() as session:
            async with session.begin():
                await session.execute(
                    update(Question)
                    .where(Question.question_id == question_id)
                    .values(status=status)
                )
                await session.commit()
        return True
    except Exception as e:
        return False


# Update subscription_status to True, return False if already True
async def activate_subscription(telegram_id: str) -> bool:
    async with async_session() as session:
        async with session.begin():
            user = await session.execute(
                select(User).where(User.telegram_id == telegram_id)
            )
            user = user.scalars().first()

            if user and user.subscription_status:
                return False

            result = await session.execute(
                update(User)
                .where(User.telegram_id == telegram_id)
                .values(subscription_status=True)
            )
            await session.commit()
            return result.rowcount > 0


# Функция для отправки уведомлений всем пользователям, кроме администраторов
async def send_notification_to_all_users(text_notification: str, photo_id: str = None):
    notification = Notification(
        text=text_notification,
        photo_id=photo_id,
        total_users=0,
        sent_count=0,
        updated_at=get_current_time(),
        created_at=get_current_time()
    )

    async with async_session() as session:
        async with session.begin():
            user_result = await session.execute(select(User.telegram_id))
            all_users = set(user_result.scalars().all())

            admin_result = await session.execute(select(Admin.telegram_id))
            admins = set(admin_result.scalars().all())

            users_to_notify = all_users - admins

            notification.total_users = len(users_to_notify)

            session.add(notification)
            await session.flush()

            for telegram_id in users_to_notify:
                try:
                    await bot.send_photo(
                        chat_id=telegram_id,
                        photo=photo_id,
                        caption=text_notification,
                        reply_markup=kb.to_user_account_kb
                    )

                    notification.sent_count += 1
                except Exception as e:
                    print(f"Не удалось отправить сообщение пользователю {telegram_id}: {e}")

            session.add(notification)
            await session.commit()

async def get_last_50_notifications():
    try:
        async with async_session() as session:
            # Получаем последние 50 уведомлений
            result = await session.execute(
                select(Notification)
                .order_by(Notification.created_at.desc())  # Сортируем по дате создания
                .limit(50)  # Ограничиваем 50 последними записями
            )

            # Извлекаем уведомления
            notifications = result.scalars().all()

            # Формируем красивое отображение уведомлений с эмодзи
            formatted_notifications = ""
            for notification in notifications:
                # Обрезаем текст уведомления до 40 символов
                text_preview = notification.text[:40] + "..." if len(notification.text) > 40 else notification.text

                formatted_notifications += f"📩: {text_preview}\n"
                formatted_notifications += f"👥: {notification.total_users} | ✅: {notification.sent_count} | ⏰: {notification.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                formatted_notifications += "-" * 65 + "\n"

            return formatted_notifications

    except Exception as e:
        print(f"Ошибка при получении уведомлений: {e}")
        return None