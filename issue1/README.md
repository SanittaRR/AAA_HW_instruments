Шаги для запуска:
1) В файле main.py запускаем "Run Doctest encode"
Проверяется работа тестов и использование директивы
2) Передаем в result
> python -m doctest issue1/*.py > issue1/result

3) В терминале запускаем 
> $ python -m doctest -o NORMALIZE_WHITESPACE -v issue1/*.py

Для проверки использования флагов.
4) Передаем в result 
> $ python -m doctest -o NORMALIZE_WHITESPACE -v issue1/*.py > issue1/result