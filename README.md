Проект является чат-ботом, одновременно работающий на платформах Discord
и Twitch и связывающий чаты в них. Основные функции: 
1. link. Позволяет связать аккаунты twitch и discord путем указывания ника 
2. help. Дает помощь по конкретной команде 
3. ban, mute, kick. Ну тут понятно. Последняя используется только в discord 
4. afk и его виды(sleep, study, work и т.д.). Связаны между дискордом и твичем
5. weather, time и похожие команды, завязанные на месте на карте. Его можно указывать прямо в команде либо через location set. При втором случае оно сохранится впредь.
6. Напоминания, имеют разные формы, такие как напоминание себе через время, напоминание в лс и т.д. 
7. Перевод + транслитерация
8. Я не знаю, нужно ли создавать заявку и платить, для получения доступа к API OpenAI, но если там все нормально, то доступ через бота к chatGPT и Dalle-2

Из основного все. Будут еще дополнительные команды и пассивные функции, но их додумать надо по ходу работы. 
Библиотеки: discord, twitchio, sys, sqlite3
(По ходу работы дополнится)
