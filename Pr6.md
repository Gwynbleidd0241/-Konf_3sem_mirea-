# Практическое задание №6

## Задача 0

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

## Задача 1
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.

Содержимое pr4_1.py:<br>
```
import json

def generate_makefile(graph):
    with open('Makefile', 'w') as f:
        for target, deps in graph.items():
            deps_str = ' '.join(deps)
            f.write(f'{target}: {deps_str}\n')
            f.write(f'\t@echo "Building {target}"\n\n')

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    generate_makefile(graph)
    print("Makefile создан.")
```

Содержимое civgraph.json:<br>
```
{
    "mathematics": ["drama_poetry", "mysticism"],
    "drama_poetry": ["foreign_trade"],
    "foreign_trade": ["code_of_laws"],
    "mysticism": ["early_empire"],
    "early_empire": ["pottery"],
    "pottery": [],
    "code_of_laws": [],
    "mining": [],
    "bronze_working": ["mining"],
    "sailing": ["astrology"],
    "astrology": [],
    "celestial_navigation": ["sailing"],
    "writing": ["pottery"],
    "irrigation": [],
    "currency": [],
    "masonry": []
}
```

В результате получим:<br>

![image](https://github.com/user-attachments/assets/d397bb13-349a-4b9e-9d81-8a8a51d0fe7b)<br>

## Задача №2
Реализовать вариант трансляции, при котором повторный запуск таке не выводит для civgraph на экран уже выполненные "задачи":<br>
Содержимое pr4_2.py:<br>

![image](https://github.com/user-attachments/assets/b0be5237-ef17-451f-8542-71f7b1508c7f)<br>

![image](https://github.com/user-attachments/assets/09d92ed7-c5df-4c87-9337-088918bb8400)<br>

## Задача №3
Добавить цель clean, не забыв и про "животное":<br>
Содержимое pr4_3.py:<br>

![image](https://github.com/user-attachments/assets/db0e08f1-e104-48ab-b0d6-a158804f565d)<br>

![image](https://github.com/user-attachments/assets/e870132d-f036-4512-b2b3-fec5654b230f)<br>

## Задача №4
Написать makefile для следующего скрипта сборки:
```
gcc prog-c data.c -o prog 
dir /B › files.lst 
7z a distr.zip *.*
```
Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: рrod и data. Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС. В makefile должны быть, как минимум, следующие задачи: all, clean, archive. Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются:<br>

![image](https://github.com/user-attachments/assets/cfe4fecd-b4d6-4479-b878-17f712829f39)<br>

Содержимое Makefile:
```
SRC = prod.go data.go
OUT = prod
ARCHIVE = archive.zip

all: $(OUT) $(ARCHIVE)

$(OUT): $(SRC)
        go build -o $(OUT) $(SRC)
        @echo "$(OUT) builded."
SRC = prod.go data.go
OUT = prod
ARCHIVE = archive.zip

all: $(OUT) $(ARCHIVE)

$(OUT): $(SRC)
        go build -o $(OUT) $(SRC)
        @echo "$(OUT) builded."

$(ARCHIVE): $(OUT)
        zip -r $(ARCHIVE) $(SRC) $(OUT)
        @echo "Archived in $(ARCHIVE)."

clean:
        rm -f $(OUT) $(ARCHIVE)
        @echo "Cleaned."

.PHONY: all clean
```

![image](https://github.com/user-attachments/assets/f7383213-d93b-4f80-ab1c-f5ba2d10726c)
