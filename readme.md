# Аналіз алгоритмів DFS та BFS на графі метро Києва

## Опис проекту

Цей проект використовує алгоритми пошуку в глибину (DFS) і пошуку в ширину (BFS) для знаходження шляхів у графі метро Києва. Граф представлено як неорієнтований граф, де вершини відповідають станціям метро, а ребра – лініям метро між станціями.

## Алгоритми

### Пошук у глибину (DFS)

- **Опис**: Алгоритм DFS заглиблюється у вузли, перш ніж повертатися назад. Він може знайти шляхи, які не є найкоротшими, оскільки він спочатку досліджує один напрямок до кінця, перш ніж перейти до іншого.
- **Переваги**: Простота реалізації та мале використання пам'яті, якщо граф має невелику глибину.
- **Недоліки**: Може виявитися неефективним для графів з великою глибиною або для знаходження найкоротшого шляху.

### Пошук у ширину (BFS)

- **Опис**: Алгоритм BFS досліджує всі сусідні вузли на кожному рівні, гарантуючи, що буде знайдено найкоротший шлях до цільової вершини.
- **Переваги**: Завжди знаходить найкоротший шлях, що робить його ідеальним для використання у випадках, коли важливий час.
- **Недоліки**: Може вимагати більше пам'яті для зберігання всіх вузлів на рівні, особливо в широких графах.

## Результати виконання

Для тестування алгоритмів були вибрані станції "Akademmistechko" і "Chervony Khutir":

- **Шлях DFS**: ['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir']
- **Шлях BFS**: ['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir']

### Висновки

- **DFS** може призвести до знаходження довших і менш оптимальних шляхів, оскільки він фокусується на заглибленні в один напрямок.
- **BFS** завжди знаходить найкоротший шлях, що робить його більш підходящим для графів, де важлива оптимізація маршруту.
- Обидва алгоритми (DFS і BFS) виявили єдиний шлях між вибраними станціями, оскільки в схемі київського метро завжди існує тільки один шлях між будь-якими двома станціями.
- Це підкреслює, що в даному випадку вибір алгоритму не впливає на результат, оскільки обидва алгоритми забезпечують однакові результати.



