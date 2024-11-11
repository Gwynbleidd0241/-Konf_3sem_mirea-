# Практическая работа № 4

## Задача 1
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing=git/с помощью команд эмулятора git получить следующее состояние проекта:<br>

![image](https://github.com/user-attachments/assets/c99b1cb2-6744-44d8-b6c0-3a85219786a5)<br>

## Задача 2
Создать локальный git-репозиторий. Задать свои имя и почту (далее - coder1).<br>
Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git:<br>
```
gwynbleidd@MacBook-Air-Sergej-3 ~ % cd Desktop
gwynbleidd@MacBook-Air-Sergej-3 Desktop % mkdir Pr4_2 
gwynbleidd@MacBook-Air-Sergej-3 Desktop % cd Pr4_2
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Инициализирован пустой репозиторий Git в /Users/gwynbleidd/Desktop/Pr4_2/.git/
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git config user.name "Lazarenko Sergey"
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git config user.email "example@mail.ru"
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % touch prog.py
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git status
Текущая ветка: master

Еще нет коммитов

Неотслеживаемые файлы:
  (используйте «git add <файл>...», чтобы добавить в то, что будет включено в коммит)
	prog.py

индекс пуст, но есть неотслеживаемые файлы
(используйте «git add», чтобы проиндексировать их)
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git add .
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git status 
Текущая ветка: master

Еще нет коммитов

Изменения, которые будут включены в коммит:
  (используйте «git rm --cached <файл>...», чтобы убрать из индекса)
	новый файл:    prog.py

gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git commit -m "Тестовый коммит"
[master (корневой коммит) d70d469] Тестовый коммит
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 prog.py
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git log --oneline

d70d469 (HEAD -> master) Тестовый коммит
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % git log
commit d70d469a31f1863e86bc7a43fc6a17bdc6f0ba41 (HEAD -> master)
Author: Lazarenko Sergey <example@mail.ru>
Date:   Wed Nov 6 09:58:50 2024 +0300

    Тестовый коммит
gwynbleidd@MacBook-Air-Sergej-3 Pr4_2 % 
```

## Задача 3
Создать рядом с локальным репозиторием bare-репозиторий с именем server.<br>
Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 c server.<br>
Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее - coder2). Добавить файл readme.md с описанием программы. Обновить сервер.<br>
Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.<br>
Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.<br>
Прислать список набранных команд и содержимое git log.<br>

```
gwynbleidd@MacBook-Air-Sergej-3 Desktop % cd Pr4_3   
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % branch
zsh: command not found: branch
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % mkdir coder1
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % cd coder1
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Инициализирован пустой репозиторий Git в /Users/gwynbleidd/Desktop/Pr4_3/coder1/.git/
gwynbleidd@MacBook-Air-Sergej-3 coder1 % bracnh
zsh: command not found: bracnh
gwynbleidd@MacBook-Air-Sergej-3 coder1 % branch
zsh: command not found: branch
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git branch
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git config user.name "Coder 1"
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git config user.email "coder1@corp.com"
gwynbleidd@MacBook-Air-Sergej-3 coder1 % echo "print('Hello from RTU MIREA')" > prog.py
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git add prog.py
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git commit -m "first commit"

[master (корневой коммит) e946877] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git branch
* master
gwynbleidd@MacBook-Air-Sergej-3 coder1 % cd ..
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git bracnh
git: «bracnh» не является командой git. Смотрите «git --help».

Самые похожие команды:
	branch
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git branch
* main
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git branch -M master
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git branch          
* master
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git init --bare server.git
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Инициализирован пустой репозиторий Git в /Users/gwynbleidd/Desktop/Pr4_3/server.git/
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % cd coder1
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git remote add server ../server.git
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git remote -v
server	../server.git (fetch)
server	../server.git (push)
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git push server master
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (3/3), 234 байта | 234.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
 * [new branch]      master -> master
gwynbleidd@MacBook-Air-Sergej-3 coder1 % cd ..
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % git clone server.git coder2
Клонирование в «coder2»...
готово.
gwynbleidd@MacBook-Air-Sergej-3 Pr4_3 % cd coder1
gwynbleidd@MacBook-Air-Sergej-3 coder1 % echo "Program_1 info" >> README.md
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git add README.md
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git commit -m "coder 1 info"
[master a3b1322] coder 1 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
gwynbleidd@MacBook-Air-Sergej-3 coder1 % git push server master                  
Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 279 байтов | 279.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
   e946877..a3b1322  master -> master
gwynbleidd@MacBook-Air-Sergej-3 coder1 % cd ../coder2
gwynbleidd@MacBook-Air-Sergej-3 coder2 % echo "Program_2 info" >> README.md
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git add README.md
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git config user.name "Coder 2"
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git config user.email "coder2@corp.com"
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git commit -m "coder2 info"
[master cae46a6] coder2 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git push origin master
To /Users/gwynbleidd/Desktop/Pr4_3/server.git
 ! [rejected]        master -> master (fetch first)
error: не удалось отправить некоторые ссылки в «/Users/gwynbleidd/Desktop/Pr4_3/server.git»
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git branch
* master
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git pull origin master
remote: Перечисление объектов: 4, готово.
remote: Подсчет объектов: 100% (4/4), готово.
remote: Сжатие объектов: 100% (2/2), готово.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Распаковка объектов: 100% (3/3), 259 байтов | 129.00 КиБ/с, готово.
Из /Users/gwynbleidd/Desktop/Pr4_3/server
 * branch            master     -> FETCH_HEAD
   e946877..a3b1322  master     -> origin/master
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git add README.md
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git commit -m "readme fix"
Текущая ветка: master
Ваша ветка и «origin/master» разделились
и теперь имеют 1 и 1 разных коммита в каждой соответственно.

нечего коммитить, нет изменений в рабочем каталоге
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git push origin master
To /Users/gwynbleidd/Desktop/Pr4_3/server.git
 ! [rejected]        master -> master (non-fast-forward)
error: не удалось отправить некоторые ссылки в «/Users/gwynbleidd/Desktop/Pr4_3/server.git»
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git push origin main  
error: src refspec main ничему не соответствует
error: не удалось отправить некоторые ссылки в «/Users/gwynbleidd/Desktop/Pr4_3/server.git»
gwynbleidd@MacBook-Air-Sergej-3 coder2 % git log --graph --all
*   commit d5257be56a5189b1923f44894c2536ad7f05f8d0 (HEAD -> master, origin/master, origin/HEAD)
|\  Merge: c6ac512 68a15ba
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Wed Nov 11 10:34:53 2024 +0300
| |
| |     readme fix
| |
| * commit 68a15ba92253243373430c5ca614417c1f08b8e2
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Wed Nov 11 10:28:08 2024 +0300
| |
| |     coder 1 info
| |
* | commit c6ac512ad70f08e516da97e8e17d9118d4a47a8d
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Wed Nov 11 10:30:03 2024 +0300
|
|       coder2 info
|
* commit e26dc965e1f97f1d169cb178c3851d2681759ae6
  Author: Coder 1 <coder1@corp.com>
  Date:   Wed Nov 11 10:24:53 2024 +0300

      first commit
```

## Задача 4

Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git:<br>

```
import subprocess


def list_git_objects():
    try:
        result = subprocess.run(
            ["git", "rev-list", "--all", "--objects"],
            capture_output=True, text=True, check=True
        )
        return [line.split()[0] for line in result.stdout.splitlines()]
    except subprocess.CalledProcessError:
        print("Ошибка при получении списка объектов")
        return []


def main():
    for obj in list_git_objects():
        print(f"\n{'=' * 45}\nHash {obj}\n{'=' * 45}")
        subprocess.run(["git", "cat-file", "-p", obj], check=True)


if __name__ == "__main__":
    main()
```

![image](https://github.com/user-attachments/assets/1ad74364-fd6d-45d9-9a6e-7438e0747881)<br>
