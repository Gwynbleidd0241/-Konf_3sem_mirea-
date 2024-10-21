# Практическое задание №4

## Задание 0

Работа с утилитой Make.
Изучить основы языка утилиты таке. Распаковать в созданный каталог make.zip, если у вас в в системе нет таке. Создать приведенный ниже Makefile и проверить его работоспособность.
```
dress: trousers shoes jacket
  @echo "All done. Let's go outside!"
jacket: pullover
  @echo "Putting on jacket."
pullover: shirt
  @echo "Putting on pullover."
shirt:
  @echo "Putting on shirt."
trousers: underpants
  @echo "Putting on trousers."
underpants:
  @echo "Putting on underpants."
shoes: socks
  @echo "Putting on shoes."
socks: pullover
  @echo "Putting on socks."
```
Визуализировать файл civgraph.txt.
