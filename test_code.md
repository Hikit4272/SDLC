# **Тестування лабораторної роботи**

## **Опис тестування**
Програма була протестована на коректність роботи декоратора `count_calls`, функції `my_function` та функції `print_stats`. Мета тестування — перевірити, чи коректно підраховується кількість викликів функції та чи правильно виводиться інформація.

## **Сценарій тестування**
1. Виклик функції `my_function` п'ять разів.
2. Виконання `print_stats` для перевірки підрахунку викликів.
3. Аналіз отриманого виводу.

## **Очікуваний результат**
```
Функція працює
Функція працює
Функція працює
Функція працює
Функція працює
Функція була викликана 5 разів
```

## **Фактичний результат**
```
Функція працює
Функція працює
Функція працює
Функція працює
Функція працює
Функція була викликана 5 разів
```

## **Висновки**
- Програма успішно підраховує виклики `my_function`.
- Декоратор `count_calls` працює коректно, зберігаючи кількість викликів.
- Функція `print_stats` правильно відображає кількість викликів.
- Тестування підтвердило правильність роботи коду.



