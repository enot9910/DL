Проект взят из [Implementation of deep learning framework](https://github.com/zhixuhao/unet) https://github.com/a-martyn/unet. В нем сверточные сети u-net применяются к сегментации изображений с клетками.  

### Запуск тестового проекта:
1. Скачиваем репозиторий и переходим в него:  

git clone https://github.com/enot9910/DL.git && cd DL

2. Скчаиваем обученную модель:  
https://drive.google.com/file/d/1GUVUG7ykk7hKLeQZSSuZWRqrV8u_HeL-/view?usp=drive_link

* Оригинальная папка с данными для обучения модели хранится по ссылке https://drive.google.com/drive/folders/1ahTpEU1c6z4Mdl_DdFQwPqbyBAGsAm0y?usp=drive_link. 

3. Встраиваем модель в проект:  
Копируем скаченную модель и вставляем его в корневую папку проекта DL. 

4. Собираем и запускаем докер: 
создание образа 
```
sudo docker build -t test1 .
```
запуск образа
```
sudo docker run test1
```
Если на вашем компьютере получены результаты аналогичные тем, что получены на моей машине, то вы увидите сообщение  
*Test passed*  
Если нет, то  
*Test failed*

