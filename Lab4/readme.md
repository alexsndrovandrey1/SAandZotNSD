# Развертывание Threat intelligence Platform OpenCTI

## Цель работы

1. Освоить базовые подходы процессов Threat Intelligence
2. Освоить современные инструменты развертывания контейнеризованных приложений
3. Получить навыки поиска информации об угрозах ИБ

## Ход выполнения работы

1. Подготовка файлов кофигураций

* Клонируем репозитурий с GitHub

```()
sudo git clone https://github.com/OpenCTI-Platform/docker.git 
```

![All text](screenhots/1.png)

* Генерируем UUID

```()
cat /proc/sys/kernel/random/uuid
```

* Увеличиваем виртуальную память

```()
sudo sysctl -w vm.max_map_count=1048575
```

![All text](screenhots/3.png)

* Конфигурируем файл `.env`

![All text](screenhots/2.png)

* Дополнительная установка ELK

```()
 docker pull elastic/elasticsearch:8.6.2
```

2. Запускаем OpenCTI

* Запуск контейнера в фоновом режиме

```()
sudo docker-compose up -d
```

![All text](screenhots/4.png)

3. Перейдем в веб-интерфейс OpenCTI `localhost:8088`

![All text](screenhots/5.png)

4. Зайдем на сайт с документацией по импорту файлов и увидем, что существует библиотека python для работы с OpenCTI. Напишем код для импорта файла в opencti:

```()
import pycti
from datetime import datetime

date = datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")

api_url = 'http://localhost:8088'
api_token = '56ad8745-f2n5-781e-lw3h-658071gr2956'
client = pycti.OpenCTIApiClient(api_url, api_token)

with open('hosts.txt', 'r') as f:
    domains = f.read().splitlines()
k = 1
for domain in domains:
    indicator = client.indicator.create(
    name="HOST number  {}".format(k),
    description="For pr5 RTU MEMREA",
    pattern_type="stix",
    pattern="[domain-name:value = '{}']".format(domain),
    x_opencti_main_observable_type="IPv4-Addr",
    valid_from=date,
    update=True,
    score=75,
    )
    print("Created indicator with ID:", indicator["id"])
    k += 1
```

Ответ:
![All text](screenhots/6.png)

![All text](screenhots/7.png)

5. Преобразуем все индикаторы в Observables

![All text](screenhots/8.png)

![All text](screenhots/9.png)

6. Импортируем сетевой трафик, полученный в lab_2 в OpenCTI

![All text](screenhots/10.png)

7. Добавим этот файл в рабочую область

![All text](screenhots/11.png)

8. Перейдем в раздел с анализом и отфильтруем поиск по нежелательному траффику

![All text](screenhots/12.png)

## Оценка результата

С помощью платформы OpenCTI удалось проанализировать трафик на предмет перехода по нежелательным доменам.

## Выводы

Таким образом, были изучены возможности работы с платформой threat intelligence OpenCTI
