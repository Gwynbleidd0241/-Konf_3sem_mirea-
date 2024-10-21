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

Результат:

![image](https://github.com/user-attachments/assets/e06d9993-c93d-4081-95ec-1c5880a2ee4e)<br>

Для визуализации напишем код на Python:<br>

![image](https://github.com/user-attachments/assets/de22e87f-cb3c-4ba0-b82a-b60048ccd475)<br>

В результате получим:<br>

![image](https://github.com/user-attachments/assets/625ca26f-fb23-4ca9-a1d4-4e2d2eb4a8d0)<br>

## Задание 1
