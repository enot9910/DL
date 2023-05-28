Проект взят из [Implementation of deep learning framework](https://github.com/zhixuhao/unet). В нем сверточные сети u-net применяются к сегментации изображений с клетками.  

### Запуск тестового проекта:
1. Скачиваем репозиторий и переходим в него:  

https://github.com/enot9910/DL.git

2. Скчаиваем обученную модель:  
https://drive.google.com/file/d/1GUVUG7ykk7hKLeQZSSuZWRqrV8u_HeL-/view?usp=drive_link

3. Встраиваем модель в проект:  
Копируем скаченную модель и вставляем его в папку прокта DL. 

4. Собираем и запускаем докер:  
```
sudo docker build -t test1 .
```
```
sudo docker run test1
```
Если на вашем компьютере получены результаты аналогичные тем, что получены на моей машине, то вы увидите сообщение  
*Test passed*  
Если нет, то  
*Test failed*

