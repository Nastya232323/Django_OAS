# Obvious Acrostic Steganography

Простая программа наглядной стеганографии в акротекстах.

См. пост на хабре:
TODO (Насть, когда начнёшь писать и скроешь в черновики, присвоят ID-шник. Укажи его тут)

<изображение процессов>

## Сокрытие и извлечение

### Сокрытие

TODO

### Извлечение

TODO

## ССС (Стандартный Стеганографический Стек)

В ССС процесс передачи
сокрытого сообщения следующий:

```
искомое сообщение
       ||
      \  /
       \/
сжатое сообщение
       ||
      \  /
       \/
коды, исправляющие ошибки
       ||
      \  /
       \/
потоковый шифр
```

Однако целью данной работы не было разработать
полноценную стеганографическую систему,
а наглядно **показать** что
акротексты можно разрабатывать не только
ручным и автоматическим способом, но и
"полуавтоматическим"

В данном случае оператор (человек)
является гарантом "каественного" текста,
а машина предлагает различные варианты
корректного кодирования для передачи стегосообщения.


## DANTSOVA

В качестве ядра использовалась простая программа DANTSOVA.

Форк проекта: https://github.com/PavelMSTU/DANTSOVA
См. пост на хабре: https://habr.com/post/280646/