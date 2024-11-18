# Задача 1
Реализовать с помощью математического языка LaTeX нижеприведенную формулу:
![image](https://github.com/user-attachments/assets/e6e4738f-bc1d-4221-91d1-10aadd16d8cc)
Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.
```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}

\begin{document}

\begin{equation*}
\int_{x}^{\infty} \frac{dt}{t(t^2 - 1) \log t} = \int_{x}^{\infty} \frac{1}{t \log t} \left( \sum_{m} t^{-2m} \right) dt = \sum_{m} \int_{x}^{\infty} \frac{t^{-2m}}{t \log t} \, dt \overset{(u = t^{-2m})}{=} - \sum_{m} \operatorname{li}(x^{-2m})
\end{equation*}

\text{Лазаренко Сергей Александрович}

\end{document}
```
![image](https://github.com/user-attachments/assets/09f2b788-a26c-4691-8b71-f592435f5a93)
