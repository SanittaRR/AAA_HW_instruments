Шаги для запуска:
1) Запускаем по отдельности mock тесты на проверку принятия дат правильного типа, и соответствия результата
> Python tests for main.test_get_cases1
> Python tests for main.test_get_cases2
> Python tests for main.test_get_cases3

2) Сохраняем результаты в result

3) Устанавливаем пакет для расчета coverage
> $ pip install -U pytest-cov

4) Проверяем процент покрытия кода тестами
> $ python -m pytest -q issue5/main.py --cov=issue5/what_is_year_now.py

5) Формируем отчет о покрытии в виде директории с html файлами
> $ python -m pytest --cov . --cov-report html


