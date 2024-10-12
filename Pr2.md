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
enum PACKAGES = { root, menu_1_0_0, menu_1_1_0, menu_1_2_0, menu_1_3_0, menu_1_4_0, menu_1_5_0, dropdown_1_8_0, dropdown_2_0_0, dropdown_2_1_0, dropdown_2_2_0, dropdown_2_3_0, icons_1_0_0, icons_2_0_0 };

array[PACKAGES] of var 0..1: installed;
constraint installed[root] == 1;

constraint ((installed[root] == 1 -> installed[menu_1_0_0] == 1) \/ 
    (installed[root] == 1 -> installed[menu_1_1_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_2_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_3_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_4_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_5_0] == 1));
    
constraint (installed[root] == 1 -> installed[icons_1_0_0] == 1);

constraint (installed[menu_1_1_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_2_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_3_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_4_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_5_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_0_0] == 1);
    
constraint (installed[menu_1_0_0] == 1) -> (installed[dropdown_1_8_0] == 1);
constraint ((installed[dropdown_2_0_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_1_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_2_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_3_0] == 1) -> (installed[icons_2_0_0] == 1));

solve minimize(sum(installed));
output ["Installed packages: ", show(installed)];
```
<br>

Результат программы:<br>

![image](https://github.com/user-attachments/assets/93d47eae-5419-483c-a8a0-9e4f28a01d16)<br>

## Задание 6

![image](https://github.com/user-attachments/assets/b1efad2a-d648-4588-b404-54a5d4742da5)<br>

```
enum PACKAGES = {root, foo_1_0_0, foo_1_1_0, target_1_0_0, target_2_0_0, left_1_0_0, right_1_0_0, shared_1_0_0, shared_2_0_0};

array[PACKAGES] of var 0..1: installed;
constraint installed[root] == 1;

constraint ((installed[root] == 1 -> installed[foo_1_0_0] == 1) \/ 
    (installed[root] == 1 -> installed[foo_1_1_0] == 1));
    
constraint (installed[root] == 1 -> installed[target_2_0_0] == 1);

constraint ((installed[foo_1_1_0] == 1 -> installed[left_1_0_0] == 1) \/ 
    (installed[foo_1_1_0] == 1 -> installed[right_1_0_0] == 1));
    
constraint ((installed[left_1_0_0] == 1 -> installed[shared_1_0_0] == 1) \/ 
    (installed[left_1_0_0] == 1 -> installed[shared_2_0_0] == 1));
    
constraint (installed[right_1_0_0] == 1 -> installed[shared_1_0_0] == 1);

constraint (installed[shared_1_0_0] == 1 -> installed[target_1_0_0] == 1);

solve minimize(sum(installed));
```
В результате получим:<br>

![image](https://github.com/user-attachments/assets/76a6735c-5b57-43e2-be21-ba78c9d86778)<br>

## Задание 7
Представить на MiniZinc задачу о зависимостях пакетов в общей форме, чтобы конкретный экземпляр задачи описывался только
своим набором данных.<br>

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

Код на python:<br>
```
packages = {
    "root": {"dependencies": ["^foo_1_0_0", "<=target_2_0_0"]},
    "foo_1_1_0": {"dependencies": ["^left_1_0_0", "^right_1_0_0"]},
    "left_1_0_0": {"dependencies": [">=shared_1_0_0"]},
    "right_1_0_0": {"dependencies": ["<shared_2_0_0"]},
    "shared_1_0_0": {"dependencies": ["^target_1_0_0"]},
    "shared_2_0_0": {"dependencies": []},
    "target_1_0_0": {"dependencies": []},
    "target_2_0_0": {"dependencies": []}
}
cnt_pack = {}
keys_list = list(packages.keys())
for key in keys_list:
    cnt_pack[key.split('_')[0]] = 'constraint ('
    
def satisfy_condition(condition):
    result = ""
    if condition.startswith('^'):
        base_version = condition[1:].split('_')
        for key in keys_list:
            check_vers = key.split('_')
            if key.startswith(base_version[0]) and check_vers[1] == base_version[1] and check_vers[1] >= base_version[2]:
                result += f"installed[{key}] == 1 \/ "
        result = result[:-4]
    elif condition.startswith('>='):
        base_version = condition[2:].split('_')
        for key in keys_list:
            check_vers = key.split('_')
            if key.startswith(base_version[0]) and (check_vers[1] > base_version[1] or (check_vers[1] == base_version[1] and check_vers[2] >= base_version[2])):
                result += f"installed[{key}] == 1 \/ "
        result = result[:-4]
    elif condition.startswith('<='):
        base_version = condition[2:].split('_')
        for key in keys_list:
            check_vers = key.split('_')
            if key.startswith(base_version[0]) and (check_vers[1] < base_version[1] or (check_vers[1] == base_version[1] and check_vers[2] <= base_version[2])):
                result += f"installed[{key}] == 1 \/ "
        result = result[:-4]
    elif condition.startswith('<'):
        base_version = condition[1:].split('_')
        for key in keys_list:
            check_vers = key.split('_')
            if key.startswith(base_version[0]) and (check_vers[1] < base_version[1] or (check_vers[1] == base_version[1] and
                                                                                         check_vers[2] < base_version[2])):
                result += f"installed[{key}] == 1 \/ "
        result = result[:-4]
    elif condition.startswith('>'):
        base_version = condition[1:].split('_')
        for key in keys_list:
            check_vers = key.split('_')
            if key.startswith(base_version[0]) and (check_vers[1] > base_version[1] or (check_vers[1] == base_version[1] and
                                                                                         check_vers[2] > base_version[2])):
                result += f"installed[{key}] == 1 \/ "
        result = result[:-4]
    return "(" + result + ")"

def generate_minizinc_code(packages):
    package_names = ', '.join(keys_list)
    minizinc_code = f"enum PACKAGES = {{{package_names}}};\n"
    minizinc_code += "array[PACKAGES] of var 0..1: installed;\n\n"
    minizinc_code += "constraint installed[root] == 1;\n"
    for package, details in packages.items():
        dependencies = details["dependencies"]
        if dependencies:
            dep_constraints = []
            for dep in dependencies:
                if dep.startswith(('^', '>=', '<=', '>', '<')):
                    constraint = satisfy_condition(dep)
                    if constraint:
                        dep_constraints.append(constraint)
                else:
                    dep_constraints.append(f"installed[{dep}] == 1")
            constraint = "constraint installed[{}] == 1 -> ({});\n".format(
                package, ' /\\ '.join(dep_constraints)
            )
            minizinc_code += constraint
    minizinc_code += "\n"
    for i in keys_list:
        cnt_pack[i.split('_')[0]] += f"installed[{i}] + "
    for i in list(cnt_pack.keys()):
        minizinc_code += cnt_pack[i][:-3] + ") <= 1;\n"
        
    minizinc_code += "\nsolve minimize sum(installed);\n"
    return minizinc_code

minizinc_code = generate_minizinc_code(packages)
print(minizinc_code)
```

Сгенерированный код на MiniZinc:<br>
```
enum PACKAGES = {root, foo_1_1_0, left_1_0_0, right_1_0_0, shared_1_0_0, shared_2_0_0, target_1_0_0, target_2_0_0};
array[PACKAGES] of var 0..1: installed;

constraint installed[root] == 1;
constraint installed[root] == 1 -> ((installed[foo_1_1_0] == 1) /\ (installed[target_1_0_0] == 1 \/ installed[target_2_0_0] == 1));
constraint installed[foo_1_1_0] == 1 -> ((installed[left_1_0_0] == 1) /\ (installed[right_1_0_0] == 1));
constraint installed[left_1_0_0] == 1 -> ((installed[shared_1_0_0] == 1 \/ installed[shared_2_0_0] == 1));
constraint installed[right_1_0_0] == 1 -> ((installed[shared_1_0_0] == 1));
constraint installed[shared_1_0_0] == 1 -> ((installed[target_1_0_0] == 1));

constraint (installed[root]) <= 1;
constraint (installed[foo_1_1_0]) <= 1;
constraint (installed[left_1_0_0]) <= 1;
constraint (installed[right_1_0_0]) <= 1;
constraint (installed[shared_1_0_0] + installed[shared_2_0_0]) <= 1;
constraint (installed[target_1_0_0] + installed[target_2_0_0]) <= 1;

solve minimize sum(installed);
```

Полученный ответ:<br>

![image](https://github.com/user-attachments/assets/95c90485-0182-48ac-961c-3f3bfc6a8a74)
