# Задание 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета.

![image](https://github.com/user-attachments/assets/0da308e8-8fab-48b6-9a74-4764664d52d3)<br>

![image](https://github.com/user-attachments/assets/434bb2fc-5014-45c3-918d-438d8cf133cc)<br>
Для того, чтобы получить пакет, не используя пакетный менеджер, можно клонировать репозиторий к себе, а затем прописать python setup.py install.

## Задание 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета.

![image](https://github.com/user-attachments/assets/bb666485-1c54-4c82-a6c0-f61b84c43164)<br>

![image](https://github.com/user-attachments/assets/645e54bf-4bed-4fef-8976-ff581e809e06)<br>
Для установки пакета напрямую из репозитория надо клонировать этот репозиторий к себе, а затем прописать команду npm install.

## Задание 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

Скачаем graphviz с помощью Homebrew:<br>

![image](https://github.com/user-attachments/assets/fcb3337d-3d94-498c-b92d-19c425ab74d2)

После создадим файл matplotlib_dependencies.dot с содержанием:<br>

![image](https://github.com/user-attachments/assets/e89bd26c-e017-4877-b3e6-f3ad09845661)

Также создадим файл express_dependencies.dot с содержанием:<br>

![image](https://github.com/user-attachments/assets/4eb79da4-b906-4f6f-a3d7-40225d3480d0)

Изображение зависимости matplotlib:<br>

![image](https://github.com/user-attachments/assets/0ca17941-c707-4a05-88c0-0154220b17f3)<br>

Изображение зависимости express:<br>

![image](https://github.com/user-attachments/assets/6150edd0-d4b2-4fe0-b563-1ab751ab7040)<br>

## Задание 4
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.<br>
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different).
Найти минимальное решение для суммы 3 цифр.<br>
```
include "globals.mzn";

array[1..6] of var 0..9: numbers;
constraint all_different(numbers);

var int: FirstSum = sum(numbers[1..3]);
constraint FirstSum == sum(numbers[4..6]);

solve minimize FirstSum;

output ["Билет - ", show(numbers), " Сумма 3х цифр - ", show(FirstSum)];
```
![image](https://github.com/user-attachments/assets/d9eb25f6-40d9-4f5d-97e8-d84e5b8e34f0)<br>

## Задание 5

![image](https://github.com/user-attachments/assets/2ff7b55c-e32e-4386-940a-1c26d584a3f6)<br>

```
set of int: MenuVersions = 1..6;
set of int: DropdownVersions = 1..5;
set of int: IconVersions = 1..2;

array[MenuVersions] of int: menu = [150, 140, 130, 120, 110, 100];
array[DropdownVersions] of int: dropdown = [230, 220, 210, 200, 180];
array[IconVersions] of int: icons = [200, 100];

var MenuVersions: selected_menu;
var DropdownVersions: selected_dropdown;
var IconVersions: selected_icons;

constraint
    (selected_menu = 1 -> selected_dropdown in 1..3) /\
    (selected_menu = 2 -> selected_dropdown in 2..4) /\
    (selected_menu = 3 -> selected_dropdown in 3..5) /\
    (selected_menu = 4 -> selected_dropdown in 4..5) /\
    (selected_menu = 5 -> selected_dropdown = 5) /\
    (selected_dropdown = 1 -> selected_icons = 1) /\
    (selected_dropdown = 2 -> selected_icons in 1..2) /\
    (selected_dropdown = 3 -> selected_icons in 1..2) /\
    (selected_dropdown = 4 -> selected_icons in 1..2) /\
    (selected_dropdown = 5 -> selected_icons in 1..2);

solve satisfy;

output [
    "Selected menu version: \(menu[selected_menu])\n",
    "Selected dropdown version: \(dropdown[selected_dropdown])\n",
    "Selected icon version: \(icons[selected_icons])\n"
];
```
<br>
Результат программы:<br>
![image](https://github.com/user-attachments/assets/d3007a60-66d7-4ed1-bc39-7aa2cfa68810)<br>

## Задание 6

![image](https://github.com/user-attachments/assets/b1efad2a-d648-4588-b404-54a5d4742da5)<br>

```
set of int: FooVersions = 1..2;
set of int: LeftVersions = 1..1;
set of int: RightVersions = 1..1;
set of int: SharedVersions = 1..2;
set of int: TargetVersions = 1..2;
set of int: RootVersions = 1..1; 

var FooVersions: selected_foo;
var LeftVersions: selected_left;
var RightVersions: selected_right;
var SharedVersions: selected_shared;
var TargetVersions: selected_target;
var RootVersions: selected_root;

constraint selected_root = 1;
constraint selected_foo = 1;
constraint selected_target = 2;
constraint selected_left = 1;
constraint selected_right = 1;
constraint selected_shared >= 1;
constraint selected_shared < 2;

solve satisfy;

output [
  "Версия foo: ", show(selected_foo),".0.0", "\n",
  "Версия left: ", show(selected_left),".0.0", "\n",
  "Версия right: ", show(selected_right),".0.0", "\n",
  "Версия shared: ", show(selected_shared),".0.0", "\n",
  "Версия target: ", show(selected_target),".0.0", "\n",
  "Версия root: ", show(selected_root),".0.0", "\n"
];
```
В результате получим:<br>

![image](https://github.com/user-attachments/assets/e726a118-3b09-4321-95b2-c8a32c6d29bc)<br>

## Задание 7
Представить на MiniZinc задачу о зависимостях пакетов в общей форме, чтобы конкретный экземпляр задачи описывался только
своим набором данных.<br>
