Разобраться, что собой представляют программируемые конфигурационные языки (Jsonnet, Dhall, CUE).
## Задача 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.<br>
```
local groups = [
  "ИКБО-1-24",
  "ИКБО-2-24",
  "ИКБО-3-24",
  "ИКБО-4-24",
  "ИКБО-5-24",
  "ИКБО-6-24",
  "ИКБО-7-24",
  "ИКБО-8-24",
  "ИКБО-9-24",
  "ИКБО-10-24",
  "ИКБО-11-24",
  "ИКБО-12-24",
  "ИКБО-13-24",
  "ИКБО-14-24",
  "ИКБО-15-24",
  "ИКБО-16-24",
  "ИКБО-17-24",
  "ИКБО-18-24",
  "ИКБО-19-24",
  "ИКБО-20-24",
  "ИКБО-21-24",
  "ИКБО-22-24",
  "ИКБО-23-24",
  "ИКБО-24-24"
];

local student(name, age, group, subject) = {
  name: name,
  age: age,
  group: group,
  subject: subject,
};

local students = [
  student("Иванов И.И.", 19, "ИКБО-4-24", "Конфигурационное управление"),
  student("Петров П.П.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Сидоров С.С.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Лазаренко С.А.", 19, "ИКБО-6-24", "Конфигурационное управление")
];

{
  groups: groups,
  students: students,
}
```
Установим Jsonnet на свой компьютер с помощью терминал:<br>
```
brew install jsonnet
```
Далее создадим файл Pr3.jsonnet, в который добавим приведенный в дано код, и скомпилируем файл в JSON, выполнив:<br>
```
jsonnet Pr3.jsonnet -o Pr3_1zd.json
```
Просмотреть содержимое файла JSON можно с помощью команды cat в терминале:<br>
```
cat Pr3_1zd.json
```
Результат:<br>

![image](https://github.com/user-attachments/assets/9328d131-bdff-4911-8a3c-2597d7a213ac)<br>

# Задача 2
Реализовать на Dhall приведенный выше пример в формате JSON. Использовать в реализации свойство программируемости и принцип Dry<br>

Установим Dhall нас свой компьютер с помощью терминала:<br>
```
brew install dhall-json
```
Далее создадим файл Pr3.dhall, в который добавим код пример, и скомпилируем файл в JSON, выполнив:<br>
```
dhall-to-json --file Pr3.dhall > Pr3_2zd.json
```
Просмотреть содержимое файла JSON можно с помощью команды cat в терминале:<br>
```
cat Pr3_2zd.json
```
Результат:<br>

![image](https://github.com/user-attachments/assets/6f3bf8e7-3932-4adf-8848-05d65e1e8a37)<br>

# Задача 3
Для решения дальнейших задач потребуется программа на Питоне, представленная в методичке к 3 практической работе. Разбираться в самом языке Питон при этом необязательно.<br>
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:<br>

Язык нулей и единиц.<br>
10<br>
100<br>
11<br>
101101<br>
000<br>
<br>

Создадим файл Pr3_3zd.python и оформим в нем решение 3 задачи:<br>
```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name) for name in seq)
    return str(start)

BNF = """
E = S1 | S2 | S3 | S4 | S5
S1 = "10"
S2 = "100"
S3 = "11"
S4 = "101101"
S5 = "000"
"""

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
В результате при запуске выполнения файла получим:<br>

![image](https://github.com/user-attachments/assets/ecb83236-d0f7-46b2-a679-f15f1f67f1ad)<br>

# Задача 4
Язык правильно расставленных скобок двух видов.<br>
(({((()))}))<br>
{}<br>
{()}<br>
()<br>
{}<br>

```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)

BNF = """
E = P E | F E | P | F 
P = "(" P ")" | "(" ")" 
F = "{" F "}" | "{}"
"""

for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        print(phrase.replace('"', ''))
```

Часть результата вывода программы:<br>

![image](https://github.com/user-attachments/assets/17853a17-536b-4e93-bc99-36dd957c6b4a)<br>

# Задача 5
Язык выражений алгебры логики.<br>
((~(y & x)) | (y) & ~x | ~x) & x <br>
у & ~ (у) <br>
(~(y) & y & ~y) <br>
~x <br>
~((x) & y | (y) | (x)) & x | x | (y & ~y) <br>

```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)

BNF = """
E = L | E & L | E | E | E
L = x | y | "(" E ")" | "~" L | "(" E ")" | "~" L
"""

def format_phrase(phrase):
    output = []
    prev_char = None
    open_count = 0

    for char in phrase:
        if char in ['x', 'y']:
            if prev_char in ['x', 'y']:
                continue
            output.append(char)
        elif char in ['&', '|']:
            if len(output) < 2 or output[-1] in ['&', '|'] or (prev_char in ['(', ')']):
                continue
            output.append(char)
        elif char == '(':
            if prev_char == '(':
                continue
            output.append(char)
            open_count += 1
        elif char == ')':
            if output and output[-1] == '(':
                output.pop()
                open_count -= 1
                continue
            if open_count > 0:
                output.append(char)
                open_count -= 1

        prev_char = char

    output = [c for c in output if not (c == '(' and (prev_char == '(' or (len(output) > 1 and output[-2] == '(')))]

    return ''.join(output)

for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        formatted_phrase = format_phrase(phrase)
        if formatted_phrase:
            print(formatted_phrase.replace('"', ''))
```

Часть результата вывода программы:<br>

![image](https://github.com/user-attachments/assets/2d1211b4-b9d5-4b7a-aa24-a6c32de5d7aa)<br>

# Полезные ссылки

[Configuration complexity clock<br>](https://mikehadlow.blogspot.com/2012/05/configuration-complexity-clock.html)
[Json<br>](https://www.json.org/json-ru.html)
[Язык Jsonnet<br>](https://jsonnet.org/learning/tutorial.html)
[Язык Dhall<br>](https://dhall-lang.org/)
[Учебник в котором темы построения синтаксических анализаторов (БНФ, Lex/Yacc)
изложены подробно<br>](https://ita.sibsutis.ru/sites/csc.sibsutis.ru/files/courses/trans/LanguagesAndTranslationMethods.pdf)
[<br>]()



