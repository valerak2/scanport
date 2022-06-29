## Scanport

### Автор: Конколович Валерий (КН-203)
```
Многопоточный сканер TCP-портов реализованный на Python 3. 
Возможность определения протоколов: SMTP, POP3, HTTP, SNTP, DNS.
```

Файлы программы:
```
scanport.py - точка входа в программу
scanner.py - класс с реализацией сканнера 
```
Запуск с консольной версии
```
Справка по запуску: ./portscan.py --help ./portscan.py -h
Пример запуска: scanport.py -t 127.0.0.1
```