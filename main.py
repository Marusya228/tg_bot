from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN = "5932068156:AAGVKlAxkakaG6amo8cf7dFPQCODZiBFNtQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

CHANNEL_ID = "@IvSUonTheRun"

async def on_startup(_):
    print("Всё готово, босс")

def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        caption_text = 'Привет, студент!\n\nУверены, что время учебы, научных открытий, творческих поисков, спортивных достижений, дружбы и любви - оставит в судьбе каждого из вас неизгладимый след. И ИвГУ предоставляет для этого все возможности.\nМы рады тому, что ты стал частью нашей дружной семьи с замечательными традициями, богатой историей и интересной студенческой жизнью, поэтому специально для тебя в этом чат-боте собрана информация, которая поможет быстрее освоиться и узнать про все возможности университета.\n\nЧем я могу тебе помочь?'
        photo_url = 'https://ibb.co/QMLZm95'
        await bot.send_photo(message.chat.id, photo=photo_url, caption=caption_text, reply_markup = keyboard)

    else: 
        await bot.send_message(message.from_user.id, 'Для работы с ботом нужно быть подписанным на канал "ИвГУ | На бегу"')
        await bot.send_message(message.from_user.id, 'https://t.me/IvSUonTheRun')

keyboard = ReplyKeyboardMarkup(row_width= 1)
but_1 = KeyboardButton(text='Информация об университете')
but_2 = KeyboardButton(text='Навигация по университету')
but_3 = KeyboardButton(text='Электронно-пропускная система ИвГУ')
but_4 = KeyboardButton(text='Дополнительное образование')
but_5 = KeyboardButton(text='Наука')
but_6 = KeyboardButton(text='Стипендии и меры социальной поддержки')
but_7 = KeyboardButton(text='Студенческие объединения')
but_8 = KeyboardButton(text='Центр "Карьера"')
but_9 = KeyboardButton(text='Служба психологической поддержки')
but_10 = KeyboardButton(text='Информация для иностранных студентов')
but_11 = KeyboardButton(text='Общежития')
but_12 = KeyboardButton(text='Заказ справок')
but_13 = KeyboardButton(text='Медицинский кабинет')

keyboard.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10, but_11, but_12, but_13)
        

@dp.message_handler(content_types=['text'])
async def test(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        if(message.text == "Информация об университете"):
            keyb2 = InlineKeyboardMarkup(row_width=1)
            butt1 = InlineKeyboardButton("Ректорат", callback_data='rectorat')
            butt2 = InlineKeyboardButton('Институт математики, информационных технологий и естественных наук', callback_data='mat')
            butt3 = InlineKeyboardButton("Институт гуманитарных наук", callback_data='gum')
            butt4 = InlineKeyboardButton("Институт социально-экономических наук", callback_data='soc')
            butt5 = InlineKeyboardButton("Юридический факультет", callback_data='urf')
            keyb2.add(butt1, butt2, butt3, butt4, butt5,)
            await bot.send_message(message.chat.id,text = "Что вас интересует?", reply_markup=keyb2)
        elif (message.text == "Навигация по университету"):
            keyb3 = InlineKeyboardMarkup(row_width=1)
            butt1 = InlineKeyboardButton("1 учебный корпус", callback_data='1')
            butt2 = InlineKeyboardButton("2 учебный корпус", callback_data='2')
            butt3 = InlineKeyboardButton("3 учебный корпус", callback_data='3')
            butt4 = InlineKeyboardButton("6 учебный корпус", callback_data='6')
            butt5 = InlineKeyboardButton("8 учебный корпус", callback_data='8')
            butt6 = InlineKeyboardButton("Виварий", callback_data='viv')
            keyb3.add(butt1, butt2, butt3, butt4, butt5, butt6)
            await bot.send_message(message.chat.id, text='Вы нажали кнопку навигации. Чтобы не потеряться в нашем университете, выберите учебный корпус, который Вас интересует:', reply_markup=keyb3)

        elif (message.text == "Электронно-пропускная система ИвГУ"):
            await bot.send_message(message.chat.id, text = 'Дорогой студент, помни: вход в учебные корпуса и общежития ИвГУ осуществляется строго по электронному пропуску, который тебе выдали на 1 курсе. \n<b>В случае утери электронного пропуска</b>, тебе нужно обратиться в 268 кабинет 3 учебного корпуса ИвГУ (ул. Ермака д.39) для его восстановления.\n\nРежим работы: пн-пт с 9:00 до 16:00\nОбед: с 12:00 до 13:00',parse_mode="html")

        elif (message.text == "Дополнительное образование"):
            caption_text = 'Институт профессионального развития ИвГУ\nПомогаем расти в профессии и открывать для себя новое!\nУ нас есть:\n- 41 программа повышения квалификации;\n- 43 программы профессиональной переподготовки\n- профессиональная подготовка к ОГЭ/ЕГЭ в рамках университетского лицея;\n- обучение иностранным языкам, как детей, так и взрослых, лучшими специалистами, лично посетившимистраны зарубежья.\nПрограммы охватывают все сферы жизни общества. По окончании обучения выдается документустановленного образца.\nДиректор Института: Елена Валерьевна Мельникова, https://ivanovo.ac.ru/about_the_university/employees/523/\nПо всем вопросам просим обращаться на почту: ipr@ivanovo.ac.ru\nТелефон для справок: +7 (4932) 93-94-77\nВК: https://vk.com/iprivgu'
            photo_url = 'https://ibb.co/7V2bn8z'
            await bot.send_photo(message.chat.id, photo=photo_url, caption=caption_text)

        elif (message.text == "Стипендии и меры социальной поддержки"):
            keyb6 = InlineKeyboardMarkup(row_width=1)
            butt1 = InlineKeyboardButton("Государственная академическая стипендия студентам", callback_data='st1')
            butt2 = InlineKeyboardButton('Государственная социальная стипендия студентам', callback_data='st2')
            butt3 = InlineKeyboardButton('Государственные стипендии аспирантам', callback_data='st3')
            butt4 = InlineKeyboardButton('Стипендии Президента Российской Федерации и стипендии Правительства Российской Федерации', callback_data='st4')
            butt5 = InlineKeyboardButton('Именные стипендии', callback_data='st5')
            butt6 = InlineKeyboardButton('Материальная помощь', callback_data='matpom')
            keyb6.add(butt1, butt2, butt3, butt4, butt5, butt6)
            await bot.send_message(message.chat.id, text='Учеба - это тоже работа! И эту работу мы готовы поощрять в виде стипендий. В нашем университете ты можешь получить следующие стипендии. Выбери из существующих, чтобы узнать подробнее', reply_markup=keyb6)

        elif(message.text == "Студенческие объединения"):
            keyb = InlineKeyboardMarkup(row_width=1)
            butt1 = InlineKeyboardButton("КОСС", callback_data='koss')
            butt2 = InlineKeyboardButton('Клуб "Импульс"', callback_data='imp')
            butt3 = InlineKeyboardButton('Клуб "Я горжусь!"', callback_data='gor')
            butt4 = InlineKeyboardButton('Профком', callback_data='prof')
            butt5 = InlineKeyboardButton('РДДМ', callback_data='rddm')
            keyb.add(butt1, butt2, butt3, butt4, butt5)
            await bot.send_message(message.chat.id,text='Выберите интересующее Вас студенческое объединение', reply_markup=keyb)

        elif(message.text == 'Центр "Карьера"'):
            keyb1 = InlineKeyboardMarkup(row_width=1)
            button1 = InlineKeyboardButton("Записаться на 'Карьерные пятницы'", url = 'https://disk.yandex.ru/edit/d/6gTawe2afczVWoCekW96WSPegnqahzm72s0qoIz-cKg6SjZPcXR6OW5YUQ')
            button2 = InlineKeyboardButton("Записаться на экскурсию", url = 'https://forms.yandex.ru/u/64cc95002530c26ecd587898/')
            button3 = InlineKeyboardButton("Стать амбассадором карьеры", url ='https://forms.yandex.ru/u/64cca0cd43f74f7a1d95c278/')
            keyb1.add(button1, button2, button3)
            await bot.send_message(message.chat.id, text='<b>Центр "Карьера" ИвГУ</b> \nЦентр профессиональной ориентации и содействия трудоустройству выпускников "Карьера" ИвГУ - мы знаем о трудоустройстве всё!\n- размещаем вакансии и стажировки\n- проводим групповые и индивидуальные консультации по трудоустройству "Карьерные пятницы"\n- устраиваем экскурсии в компании,\n- проводим ярмарки вакансий и много других карьерных мероприятий\n\nКоробова Ольга Олеговна - начальник Центра профессирнальной ориентации и содействия трудоустройству выпускников ИвГУ "Карьера"\nАдрес: ул.Ермака, 39 (3 корпус ИвГУ), 158 кабинет\nРежим работы: пн–пт 8:30–17:00\nВК: https://vk.com/career.ivsu \nФакультетус: https://facultetus.ru/ivsu\nТелефон: +7 (4932) 32-94-00\nE-mail: career@ivanovo.ac.ru',reply_markup=keyb1, parse_mode= "html")

        elif(message.text == "Служба психологической поддержки"):
            caption_text = 'Студент, раз ты обратился в этот раздел, скорее всего, тебя что-то тревожит. Мы понимаем, что в жизни каждого есть достаточно тем, которые могут беспокоить, и мы готовы помочь разобраться со всеми. \nВ ИвГУ есть <b>Центр психологической поддержки</b>, любой студент может записаться на индивидуальную консультацию, написав на почту, указанную ниже или в личные сообщения сообщества.\nТакже работает телефон доверия, на который можно позвонить и выговориться в трудную минуту. \n\nСообщество ВК: https://vk.com/public220415924 \nПочта: psiholog.ivgu@yandex.ru\nТелефон доверия: +7 (996) 517-74-21 \nАдрес: ул. Ермака, 39, кабинет 276(3-й учебный корпус)'
            photo_url = 'https://ie.wampi.ru/2023/07/24/RISUNOK1.jpg'
            await bot.send_photo(message.chat.id, photo=photo_url, caption=caption_text, parse_mode="html")

        elif(message.text == "Наука"):
            keba = InlineKeyboardMarkup(row_width=1)
            button1 = InlineKeyboardButton("Научно-исследовательская деятельность ИвГУ", url = 'http://ivanovo.ac.ru/about_the_university/science/news/')
            button2 = InlineKeyboardButton('Результаты научной работы студентов', url = 'http://ivanovo.ac.ru/about_the_university/science/students.php')
            button3 = InlineKeyboardButton('Результаты научной работы студентов', url = 'http://ivanovo.ac.ru/about_the_university/science/conferences/conferences_ivsu.php')
            button4 = InlineKeyboardButton('Актуальная информация по научным конференциям ИвГУ', url = 'https://vk.com/tboilivsu')
            button5 = InlineKeyboardButton('Точка кипения на Лидер ID', url = 'https://leader-id.ru/places/6881')
            keba.add(button1,button2,button3,button5,button4)
            await bot.send_message(message.chat.id, text = 'Ивановский государственный университет реализует  фундаментальные и прикладные исследования по 19 научным направлениям. На базе ИвГУ действует 21 научно-образовательное объединение.\nНаши ученые ежегодно проводят интересные конференции и научные мероприятия, получают гранты на исследования и защищают диссертации. На базе ИвГУ сейчас действует три диссертационных совета, более ста молодых ученых учатся в аспирантуре.\nНаше издательство выпускает ряд серьезных научных изданий, имеющих международный статус.\nДля поддержания исследовательских традиций и реализации инновационных идей у нас есть Совет молодых ученых, который активно работает над тем, чтобы научная жизнь была  интересной и разнообразной! Уже со второго курса ты научишься уверенно выступать с докладами, разовьешь в себе проектные компетенции и укрепишь навыки креативной визуализации данных! У тебя также будет возможность получить научную стипендию, поучаствовать в конкурсах на лучшую научную работу и получить гранты Президента и Правительства РФ. Скорее присоединяйся к нашей семье!\nСмирнова Инна Николаевна – проректор по исследовательской и проектной деятельности\nПочта: smirnovain@ivanovo.ac.ru\nШаповалова Анастасия Сергеевна – главный специалист научно-исследовательского управления\nПочта: niu@ivanovo.ac.ru', reply_markup= keba)

        elif(message.text == "Информация для иностранных студентов"):
            keyb12 = InlineKeyboardMarkup(row_width=1)
            button1 = InlineKeyboardButton("Центр русистики и международного образования", callback_data='centr')
            button2 = InlineKeyboardButton("Международный офис", callback_data='ofis')
            button3 = InlineKeyboardButton("Медицинское страхование", callback_data='med')
            keyb12.add(button1, button2, button3)
            await bot.send_message(message.chat.id, text='Привет, мой иностранный друг! Чем я могу тебе помочь?', reply_markup = keyb12)

        elif (message.text == "Общежития"):
            keyb4 = InlineKeyboardMarkup(row_width=1)
            butt1 = InlineKeyboardButton("Жилищный отдел", callback_data='g')
            butt2 = InlineKeyboardButton("Интернет в общежитии", callback_data='i')
            butt3 = InlineKeyboardButton("Оплата за общежитие", callback_data='o')
            keyb4.add(butt1, butt2, butt3)
            await bot.send_message(message.chat.id, text='Ивановский государственный университет располагает тремя благоустроенными общежитиями, находящимися рядом с корпусами университета. Общежития отличаются уровнем комфортности и стоимостью проживания. Выбери кнопку для получения дополнительной информации.'
                                                        '\n'' '
                                                        '\n<b>Общежитие №1</b>\nАдрес: г. Иваново, ул. Тимирязева, д. 23\nКомендант общежития: Коровина Елена Геннадьевна\nТелефон вахты: +7 (4932) 37-47-02'
                                                        '\n'' '
                                                        '\n<b>Общежитие №3</b>\nАдрес: г. Иваново, ул. Смольная, д.48\nКомендант общежития: Рыбакова Татьяна Юрьевна\nТелефон вахты: +7 (4932) 32-10-43'
                                                        '\n'' '
                                                        '\n<b>Общежитие №4</b>\nАдрес: г. Иваново, ул. Мальцева, д.46\nКомендант общежития: Письменский Эдуард Анатольевич\nТелефон вахты: +7 (4932) 37-84-88', reply_markup=keyb4, parse_mode="html")

        elif (message.text == "Заказ справок"):
            await bot.send_message(message.chat.id, text='- Заказ справки об обучении осуществляется через учебные офисы ИвГУ.\n- Заказ справки о доходах производится дистанционно по почте: 259ivgu@mail.ru\nВ письме для заказа правки нужно указать:\n1. ФИО\n2. институт/факультет, на котором вы обучаетесь\n3. Образовательную программу (допустим, 03.04.02 Физика)\n4. Курс\n5. Причина для заказа справки\n6. За какой период интересуют доходы (допустим, за последние 3 месяца)\n7. Количество копий\nСрок обработки запроса от 3-14 рабочих дней. После получения оповещения на почту о готовности справки, Вы можете забрать ее по адресу: ул.Ермака, 39 (3-й корпус ИвГУ), кабинет 266.\nГрафик работы: пн-пт с 9:00 до 16:00.')

        elif (message.text == "Медицинский кабинет"):
            await bot.send_message(message.chat.id, 'Медицинский кабинет \nАдрес: Тимирязева 5 (6 учебный корпус), каб. 126.\nРежим работы: пн-пт с 8:00 до 15:30')
    else: 
        await bot.send_message(message.from_user.id, 'Для работы с ботом нужно быть подписанным на канал "ИвГУ | На бегу"')
        await bot.send_message(message.from_user.id, 'https://t.me/IvSUonTheRun')

@dp.callback_query_handler(lambda c: c.data == 'matpom')
async def matpom(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text = 'В ИвГУ предусмотрено оказание <b>материальной помощи</b> нуждающимся студентам, обучающимся по очной форме обучения за счет средств федерального бюджета. За всеми подробностями получения материальной помощи обращаться в учебный офис/деканат Вашего института/факультета или к старосте Вашей учебной группы.',parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'centr')
async def g(callback: types.CallbackQuery):
    photo_url = 'https://wampi.ru/image/RI7n0YQ'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await  bot.send_message(callback.from_user.id, text='<b>Центр русистики и международного образования</b> - единственный в регионе лицензированное подготовительное отделение, которое готовит иностранных граждан к обучению по основным образовательным программам на русском языке по гослинии. \n\n<b>Ибрагим Ирина Александровна</b> – заведующая Центром русистики и международного образования, кандидат филологических наук, доцент.\nТелефон: 8 (4932) 42-37-09\nПочта: instudent@ivanovo.ac.ru\nАдрес: ул. Ермака, д. 39 (учебный корпус №3), кабинет № 369.', parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'ofis')
async def g(callback: types.CallbackQuery):
    photo_url = 'https://wampi.ru/image/RI7nPcZ'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await  bot.send_message(callback.from_user.id, text='<b>Международный офис</b> ответственен за поддержание контактов с партнерскими организациями ИвГУ за границей, установление новых международных связей, а также иные проекты, имеющие международную научную и культурную направленность.\nСотрудники Международного офиса курируют краткосрочную академическую мобильность студентов и преподавателей, публикуют информацию о возможных зарубежных стажировках в разделе «Конкурсы и гранты», осуществляют подготовку и выдачу Европейского приложения к диплому.\n\nАнисимова Анастасия Павловна -  руководитель международных проектов международного офиса\nТелефон: +7 (4932) 30-16-77\nПочта: intern@list.ru, interrel@ivanovo.ac.ru, travinayu@ivanovo.ac.ru\nАдрес: ул. Ермака, д. 39 (учебный корпус № 3), кабинет № 374.')

@dp.callback_query_handler(lambda c: c.data == 'med')
async def g(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Мы очень переживаем за тебя, поэтому чтоб твоё пребывание в России прошло плодотворно, нужно быть готовым ко всему, в том числе и к возможному обращению в больницу. Поэтому для всех иностранных студентов есть одно важное правило: наличие страхового медицинского полиса, действующего на территории РФ. \nСтраховой медицинский полис нужно в обязательном порядке предоставить в Центр русистики и международного образования (адрес: ул. Ермака, 39, 3 учебный корпус ИвГУ,   кабинет 369). \nЕсли у Вас остались вопросы по приобретению полиса, обращайтесь по этому же адресу. ',parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'g')
async def g(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/9YcsVqc'
    caption_text = '<b>Харитонова Ирина Александровна</b> - главный специалист жилищно-хозяйственной службы.\nТел.: +7 (4932) 37-41-47 (добавочный номер 10-81\nПочта: zhilhs@ivanovo.ac.ru\nГрафик работы:  пн-пт с 10:00 до 15:00 \nОбед: с 12:00 до 13:00\nАдрес: ул. Ермака 39, кабинет 161 (3 корпус ИвГУ)'
    await bot.send_photo(callback.from_user.id,photo=photo_url, caption=caption_text, parse_mode= "html")

@dp.callback_query_handler(lambda c: c.data == 'i')
async def i(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,'Для подключения к сети интернет, нужно обратиться по адресу: ул. Ермака 39 (3 корпус ИвГУ), кабинет 268 или 265. Не забудь прихватить с собой студенческий билет! \nГрафик работы: пн-пт с 10:00 до 15:00 \nОбед: с 12:00 до 13:00')

@dp.callback_query_handler(lambda c: c.data == 'o')
async def o(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/P52yNfJ'
    caption_text = 'Общежитие №1\nОплата за общежитие: 750 руб./мес.\nДополнительные услуги: 888 руб./мес.\nДополнительные услуги: 1020 руб./мес. (для комнат, в которых проводится уборка)\n\nОбщежитие №3\nОплата за общежитие: 380 руб./мес. (3 этаж)\nОплата за общежитие: 610 руб./мес. (2-й, 4-й и 5-й этажи)\n\nОбщежитие №4\nОплата за общежитие: 750 руб./мес.\nДополнительные услуги: 888 руб./мес.'
    await bot.send_photo(callback.from_user.id,photo=photo_url, caption = caption_text)

@dp.callback_query_handler(lambda c: c.data == 'rectorat')
async def rectorat(callback: types.CallbackQuery):
    keyb5 = InlineKeyboardMarkup(row_width=1)
    butt1 = InlineKeyboardButton("Малыгин Алексей Александрович", callback_data='m')
    butt2 = InlineKeyboardButton("Кузьмина Ольга Владимировна", callback_data='k')
    butt3 = InlineKeyboardButton("Смирнова Инна Николаевна", callback_data='sm')
    butt4 = InlineKeyboardButton("Сорокин Никита Дмитриевич", callback_data='s')
    keyb5.add(butt1, butt2, butt3, butt4)
    await bot.send_message(callback.from_user.id, 'Про кого из руководства университета Вы бы хотели узнать поподробнее?', reply_markup=keyb5)

@dp.callback_query_handler(lambda c: c.data == 'mat')
async def rectorat(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'https://wampi.ru/image/RI78ddw')
    await bot.send_message(callback.from_user.id, 'Институт математики, информационных технологий и естественных наук образован 1 сентября 2020 года решением Ученого совета ИвГУ на базе биолого-химического факультета, факультета математики и компьютерных наук, физического факультета и кафедры информационных технологий в экономике и организации производства экономического факультета.\nДиректор института: заведующая кафедрой фундаментальной и прикладной химии,доктор химических наук, профессор Кустова Татьяна Петровна.\nУчебный офис (главный): каб. 320\nТелефон:+7 (4932) 42-13-85\nУчебный офис (дополнительный): каб. 302\nТелефон:+7 (4932) 30-02-42\nТелефон:+7 (4932) 42-13-85\n+7 (4932) 30-02-42\nE-mail: imitns@ivanovo.ac.ru\nАдрес: 153025, г. Иваново, ул. Ермака, д. 37/7, каб. 302, 320 (1-й учебный корпус)')

@dp.callback_query_handler(lambda c: c.data == 'gum')
async def rectorat(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'https://wampi.ru/image/RI78xnc')
    await bot.send_message(callback.from_user.id, 'Институт гуманитарных наук образован 1 сентября 2020 года решением Ученого совета ИвГУ на базе факультета романо-германской филологии, филологического факультета, исторического факультета, кафедры безопасности жизнедеятельности и общемедицинских знаний биолого-химического факультета, а также общеуниверситетских кафедр: кафедры философии, кафедры непрерывного психолого-педагогического образования и кафедры физической культуры.\nДиректор института: доктор филологических наук, доцент кафедры зарубежной филологии Маник Светлана Андреевна.\nТелефон учебного офиса: +7 (4932) 93-85-08, +7 (4932) 93-85-53\nТелефон: +7 (4932) 93-85-11\nE-mail: humanities@ivanovo.ac.ru, maniksa@ivanovo.ac.ru\nАдрес: 153025, г. Иваново, ул. Тимирязева, д. 5а (6-й учебный корпус), каб. 404 и 310 (учебный офис)')

@dp.callback_query_handler(lambda c: c.data == 'soc')
async def rectorat(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'https://wampi.ru/image/RI785JZ')
    await bot.send_message(callback.from_user.id, 'Институт социально-экономических наук образован 1 сентября 2020 года решением Ученого совета ИвГУ на базе экономического факультета, кафедры социологии и управления персоналом и кафедры социальной работы социолого-психологического факультета.\nДиректор института: кандидат экономических наук, доцент Курникова Ирина Валерьевна.\nУчебный офис: каб. 617\nТелефон: +7 (4932) 93-89-03\nE-mail: isen@ivanovo.ac.ru\nАдрес: 153025, Иваново, ул. Тимирязева, д. 5а (6-й учебный корпус), каб. 617-620')

@dp.callback_query_handler(lambda c: c.data == 'urf')
async def rectorat(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'https://wampi.ru/image/RI78zSg')
    await bot.send_message(callback.from_user.id, 'Факультет готовит юристов широкого профиля с фундаментальной базовой подготовкой по таким дисциплинам, как общая теория права, российская и зарубежная история государства и права, конституционное право России и зарубежных стран, гражданское, семейное, административное, финансовое, налоговое, земельное, трудовое, уголовное, уголовно-исполнительное право, гражданский и уголовный процесс, иностранные языки. Начиная с третьего курса студенты могут углубленно изучать дисциплины государственно-правового, гражданско-правового, уголовно-правового, процессуального профилей. В рамках этих направлений студенты проходят производственную практику, пишут курсовые и выпускные квалификационные работы.\n Декан факультета: кандидат юридических наук, доцент кафедры уголовного права и процесса - Соколова Ольга Владимировна.\nТелефон: +7 (4932) 32-77-08\nE-mail: yurfac@ivanovo.ac.ru\nАдрес: 153002, г. Иваново, Посадский пер, д. 8, 8-й уч. корпус, к. 401')

@dp.callback_query_handler(lambda c: c.data == 'm')
async def m(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/2kbbB7d'
    caption_text = '<b>Малыгин Алексей Александрович</b> – ректор, председатель Совета ректоров вузов Ивановской области, руководитель Ивановского научного центра Российской академии образования,кандидат педагогических наук, доцент\nПочта: rector@ivanovo.ac.ru\nТел.: +7 (4932) 32-62-10\nДни приема: Понедельник, пятница 15:00 – 17:00\nЗапись на прием за 2 дня до приема по тел.: +7 (4932) 32-62-10\nАдрес: ул. Ермака, 39. Учебный корпус №3. 3 этаж, 359 кабинет.'
    await bot.send_photo(callback.from_user.id, photo=photo_url, caption=caption_text,parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'k')
async def k(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/hMsYzCd'
    caption_text = '<b>Кузьмина Ольга Владимировна</b> – первый проректор, заведующая кафедрой уголовного права и процесса, кандидат юридических наук, профессор, руководитель научно-образовательного центра «Лаборатория уголовно-правовых исследований», председатель Комиссии по аттестации педагогических кадров\nПочта: kuzminaov@ivanovo.ac.ru \nТел.: +7 (4932) 30-04-57 \nДни приема: Среда 15:00 – 17:00\nЗапись на прием за 2 дня до приема по тел. +7 (4932) 30-04-57\nАдрес: ул. Ермака, 39. Учебный корпус №3. 3 этаж, 360 кабинет.'
    await bot.send_photo(callback.from_user.id, photo=photo_url, caption=caption_text,parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'sm')
async def rectorat(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/qdWChPX'
    caption_text = '<b>Смирнова Инна Николаевна</b> – проректор по исследовательской и проектной деятельности, кандидат социологических наук, доцент, председатель Научно-технического совета\nПочта: smirnovain@ivanovo.ac.ru \nТел.: +7 (4932) 32-66-00\nДни приема: Четверг с 15:00 до 17:00 \nЗапись на прием за 2 дня до приема по тел. +7 (4932) 32-66-00\nАдрес: ул. Ермака, 39. Учебный корпус №3. 3 этаж, 355 кабинет. '
    await bot.send_photo(callback.from_user.id, photo=photo_url, caption=caption_text,parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 's')
async def rectorat(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/xSxDrzR'
    caption_text = '<b>Сорокин Никита Дмитриевич</b> – проректор по молодежной политике и социальному развитию,кандидат исторических наук\nПочта: sorokinnd@ivanovo.ac.ru\nТел.: +7 (4932) 32-61-88\nДни приема: вторник с 15:00 до 17:00\nЗапись на прием за 2 дня до приема по тел.: +7 (4932) 32-61-88\nАдрес: ул. Ермака, 39. Учебный корпус №3. 3 этаж, 357 кабинет'
    await bot.send_photo(callback.from_user.id, photo=photo_url, caption=caption_text, parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'st1')
async def st1(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, '<b>Государственная академическая стипендия</b> назначается студентам, обучающимся на бюджете, не имеющим академических задолженностей и закрывшим предыдущую сессию на 4 и 5. \nТакже в начале семестра у каждого  студента со 2-го курса, который уже получает академическую стипендию, есть шанс получить <b>повышенную академическую стипендию</b> за успехи в учебной, общественной (творческой, спортивной) или научной деятельности. Для этого Вам нужно сформировать портфолио достижений и направить в учебный офис/деканат факультета для конкурсного отбора. Повышенные стипендии утверждаются стипендиальной комиссией на один академический семестр. \nПоэтому, студент, мы желаем Тебе удачи во всех твоих начинаниях и готовы поддержать на всем пути!', parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'st2')
async def st2(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, '<b>Государственная социальная стипендия</b> назначается студентам входящих в категорию лиц: \n- сироты;\n- студенты, потерявшие кормильца;\n- студенты, чьих родителей лишили прав на воспитание;\n- инвалиды;\n- студенты, которые нуждаются в лечении;\n- студенты, пострадавшие от радиации;\n- студенты из малообеспеченных или многодетных семей;\n- ветераны боевых действий.\nДля того, чтобы оформить данный вид стипендии Вам следует обратиться в Социальную защиту населения для оформления справки о возможности получать социальную стипендию. После получения этой справки обратитесь в учебный офис института или деканат факультета для написания заявления на получение соц.стипендии. Важно: прежде чем отправиться в Соц.защиту, позвоните по телефону для записи на прием и уточнения списка документов для оформления справки. И помни, данный вид стипендии назначается на год, после истечения срока, процедуру назначения придется повторить с самого начала.', parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'st3')
async def st3(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,'<b>Государственная стипендия аспирантам</b> назначается студентам, обучающимся на бюджете, не имеющим академических задолженностей и закрывшим предыдущую сессию на 4 и 5. \nДля аспирантов 3 и 4 курса еще одним важным условием для получения государственной стипендии является наличие публикаций индексируемых изданиях.', parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'st4')
async def st4(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,'Данный вид стипендии назначается студентам, у которых не имеется академической задолженности, более 50% оценок составляют «отлично», имеются выдающиеся способности в учебной и научной деятельности (победители олимпиад, творческих конкурсов, авторы открытий,изобретений, научных статей в центральных изданиях).\nДля того чтобы поучаствовать в конкурсном отборе нужно оформить портфолио и направить заявку по формату, указанному на сайте: http://www.fa.ru/org/div/gsr/Pages/scholarships.aspx')

@dp.callback_query_handler(lambda c: c.data == 'st5')
async def st5(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'В ИвГУ предусмотрены <b>именные стипендии</b>, за всеми подробностями обращайтесь в учебный офис института/деканат факультета или же к куратору академической группы.',parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == 'st6')
async def st6(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,'Стипендии обучающимся, назначаемые юридическими лицами или физическими лицами, в том числе направившими их на обучение')

@dp.callback_query_handler(lambda c: c.data == '1')
async def k1(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/tQpfQ1V'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == '2')
async def k2(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/Xp3b0Js'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == '3')
async def k3(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/v1FTqzT'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == '6')
async def k6(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/Vg6M2wp'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == '8')
async def k8(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/jWyTHgq'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == 'viv')
async def viv(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/fpvhqS5'
    await bot.send_photo(callback.from_user.id, photo=photo_url)

@dp.callback_query_handler(lambda c: c.data == 'koss')
async def koss(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/f2LQyT1'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await  bot.send_message(callback.from_user.id, text='Знаешь кто сопровождает тебя на всем пути студенческой жизни, начиная с 1 сентября и заканчивая выдачей диплома? Конечно же <b>КОСС</b>, давай знакомиться.\nРасскажем немного о себе: мы - СемьяКОСС, организуем яркую и интересную студенческую жизнь именно для тебя! Совместно с нами ты можешь раскрыть свои способности и развить умения в направлениях работы:\n- студенческое самоуправление;\n- студенческие медиа;\n- научное;\n- волонтерское;\n- экологическое;\n- адаптационное;\n- досуговое;\n- спортивно-оздоровительное;\n- гражданско-патриотическое;\n- карьерное;\n- промоутерское.\nТы познакомишься с нашими самыми яркими проектами: Медиацентр ИвГУ, Волонтерский центр ИвГУ,ЭкоКлуб, «Привет, студент!», «Терки», МША «Твой выбор», Корпус кураторов.\nМы будем рады видеть каждого из Вас, а также мы всегда готовы помочь и поднять твое настроение. Присоединяйся к нашей семье!\nС любовью, твой КОСС\n\nПредседатель: Нона Закарян https://vk.com/zakaryanona\nВК организации: https://vk.com/koss.ivsu\nАдрес: ул. Тимирязева, 5 (6-ой корпус ИвГУ), кабинет 006.', parse_mode= "html")

@dp.callback_query_handler(lambda c: c.data == 'imp')
async def imp(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/zbJ7xVH'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await  bot.send_message(callback.from_user.id, text='<b>Студенческий спортивный клуб ИвГУ "Импульс"</b> – это группа активных студентов, выпускников и сотрудников, которые стремятся сделать спортдоступным для каждого.\nНаша основная задача – вовлекать всех обучающихся, а также преподавателей и сотрудников в занятия физической культурой и спортом.\nА также мы:\n— освещаем спортивные события университета\n— развиваем спорт в ИвГУ\n— делимся интересными фактами о спорте\n— развиваем Клуб болельщиков ИвГУ\nВысококлассные специалисты, Мастер Спорта России, Чемпионы Мира, Чемпионы России, челны сборной команды страны — все это тренера и спортсмены ССК ИвГУ «Импульс»\nПрисоединиться к спортклубу, болельщикам, спортсменам или задать вопросы ты можешь написав председателю спортклуба:\n\nПредседатель: Хвощевская Полина https://vk.com/khvoshev_polya21\nВК организации:https://vk.com/sport_ivgu\n\nАдрес: ул.Ермака, 39 (3 корпус ИвГУ),465 кабинет\nПочта:sskivsuimpuls@yandex.ru', parse_mode= "html")

@dp.callback_query_handler(lambda c: c.data == 'gor')
async def gor(callback: types.CallbackQuery):
    photo_url = 'https://ibb.co/zFTkPGR'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await bot.send_message(callback.from_user.id, text='\n<b>Клуб «Я горжусь»</b> – это не просто группа людей, а дружная команда инициативных,талантливых, энергичных и разносторонних студентов, которые горят новыми идеями и воплощают их с особым трепетом и любовью.Мы вошли в топ-3 патриотических клубов страны\nВ 2023 году мы одержали победу в конкурсе Росмолодежь. Гранты и взяли 700 000₽ на реализацию собственного форума!Является участниками таких форумов, как Таврида, ПМЭФ, «Твой Ход» и тд.\nТы имеешь активную жизненную позицию и хочешь пробовать себя в чём-то новом? Тогда тебе к нам! Мы подарим тебе яркое и незабываемое студенчество!\n\nВК организации: https://vk.com/improudivsu\nРуководитель клуба: Анастасия Ленец https://vk.com/your_ledenec', parse_mode= "html")

@dp.callback_query_handler(lambda c: c.data == 'prof')
async def prof(callback: types.CallbackQuery):
    caption_text= '<b>Профком обучающихся ИвГУ</b>\nПервичная профсоюзная организация обучающихся ИвГУ — общественная организация, объединяющая на добровольных началах обучающихся Ивановского государственного университета.\nНаша основная задача — защита Ваших прав и интересов.\nЗанимаемся организацией досуга студентов и развиваем их личностные качества (проведение мероприятий,проектная деятельность, медиа, волонтерство, спорт, творчество: вокал, танцы, театр, арт и т.д.)\nТакже для всех членов профсоюза действует скидочная система в магазины…Заинтересован? Тогда скорее пиши в ЛС группы ВК.\n\nПредседатель: Кумирова Ксения Александровна https://vk.com/id399697144\nВК организации: https://vk.com/profcom_ivsu'
    photo_url = 'https://ibb.co/YcGYtMp'
    await bot.send_photo(callback.from_user.id, photo=photo_url, caption=caption_text, parse_mode= "html")

@dp.callback_query_handler(lambda c: c.data == 'rddm')
async def rddm(callback: types.CallbackQuery):
    photo_url = 'https://wampi.ru/image/RI7nckz'
    await bot.send_photo(callback.from_user.id, photo=photo_url)
    await bot.send_message(callback.from_user.id, text='Российское движение детей и молодёжи "Движение Первых"- это единое движение, создающееся совместно с детьми.\nДвижение Первых - это возможность стать лучшей версией себя, достойным наследником великих дел первооткрывателей, основателей и первопроходцев, которых отличает стремление к победе во всех начинаниях и нежелание останавливаться на достигнутом. Быть участником Движения – это выбор сильных и готовых вписать свое имя в историю России.Отличительной чертой РДДМ "Движение Первых" ИвГУ это то, что мы являемся наставниками для детей и учим их чему-то важному и полезному.\n<b>Основные направления деятельности</b>:\n- cодействие профессиональной ориентации школьников;\n- организация досуга детей и молодёжи;\n- формирование возможностей для всестороннего развития и самореализации детей и молодёжи.\nС сентября 2023 стартует проект "Дорогами поколений", целью которого является содействие патриотическому, интеллектуальному и духовному развитию личности юного гражданина России.\n\nВк организации: https://vk.com/movementofthefirstivsu\nВк председателя: Ксения Воронова https://vk.com/ne_do_vas', parse_mode= "html")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)