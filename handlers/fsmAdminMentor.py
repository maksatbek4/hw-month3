from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import ADMINS,bot
from aiogram.dispatcher import FSMContext


class FSMmentor(StatesGroup):
    id=State()
    name=State()
    nap=State()
    age=State()
    group=State()

async def FSMstart(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMmentor.id.state
        await message.answer('здравствуйте')

async def id(message: types.Message, state:FSMContext):
    try:
        async with state.proxy() as a:
            a['id'] = int(message.text)

            await FSMmentor.next()
            await message.answer("как вас зовут")

    except:
        await bot.send_message(message.from_user.id, "id состоит из цифр")


async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['name'] = (message.text)

        await FSMmentor.next()
        await bot.send_message(message.from_user.id,'какое у вас направление ? ')


async def nap(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['nap'] = (message.text)

        await FSMmentor.next()
        await bot.send_message(message.from_user.id, 'сколько лет? ')


async def age(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['age'] = (message.text)

        await FSMmentor.next()
        await bot.send_message(message.from_user.id, 'c какой вы группы? ')

async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['group'] = message.text
        await bot.send_message(message.from_user.id, f" - {a['id']},\n,"
                               f"- {a['name']},\n, - {a['nap']},\n, - {a['age']},\n"
                               f"- {a['group']},\n")

        await FSMmentor.next()
        await message.answer("всё ли правильно?" )

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':

        await state.finish()
        await bot.send_message(message.from_user.id, "Регистрация завершена")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Не получилось!')

def register_handlers_fsm_anketa(dp: Dispatcher):

    dp.register_message_handler(FSMstart, commands=['anketa'])
    dp.register_message_handler(id, state=FSMmentor.id)
    dp.register_message_handler(name, state=FSMmentor.name)
    dp.register_message_handler(age, state=FSMmentor.age)
    dp.register_message_handler(group, state=FSMmentor.group)



























