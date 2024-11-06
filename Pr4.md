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
