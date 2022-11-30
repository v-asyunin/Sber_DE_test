
#### Обзор Spark v3.3

Спарк `3.3` значительно вырос по функционалу по отношению к предыдущим релизам. Основной фокус делается на улучшение поддержки Pandas APIs. 
Вот что на этот счет декларируют разработчики:

> "This release (3.3.0) improve join query performance via Bloom filters, increases the Pandas API coverage with the support of popular Pandas features such as datetime.timedelta and merge_asof, simplifies the migration from traditional data warehouses by improving ANSI compliance and supporting dozens of new built-in functions, boosts development productivity with better error handling, autocompletion, performance, and profiling."

https://spark.apache.org/releases/spark-release-3-3-0.html
___
Впервые поддержка pandas APIs была реализована в версии `3.2`, а в версии `3.3` была значительно расширена: 

spark 3.2.1 pandas API:
https://spark.apache.org/docs/3.2.1/api/python/user_guide/pandas_on_spark/index.html

spark 3.3 pandas API:
https://spark.apache.org/docs/3.3.0/api/python/user_guide/pandas_on_spark/supported_pandas_api.html


#### Нарушения обратной своместимости в spark 3.3

 - Drop references to Python 3.6 support in docs and python/docs ([SPARK-36977](https://issues.apache.org/jira/browse/SPARK-36977))
 - Remove namedtuple hack by replacing built-in pickle to cloudpickle ([SPARK-32079](https://issues.apache.org/jira/browse/SPARK-32079))
 - Bump minimum pandas version to 1.0.5 ([SPARK-37465](https://issues.apache.org/jira/browse/SPARK-37465))

Весь список изменений в Spark 3.3:
https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12315420&version=12350369

#### Важные апгрейды версий

- [Upgrade ORC to 1.7.1](https://issues.apache.org/jira/browse/SPARK-37232)
- [Upgrade Scala to 2.13.8](https://issues.apache.org/jira/browse/SPARK-37880)
- [Upgrade SBT to 1.6.0](https://issues.apache.org/jira/browse/SPARK-37760)
- [Upgrade lz4-java to 1.8.0](https://issues.apache.org/jira/browse/SPARK-36256)
- [Upgrade kubernetes-client to 5.12.1](https://issues.apache.org/jira/browse/SPARK-38244)
- [Upgrade Maven to 3.8.4](https://issues.apache.org/jira/browse/SPARK-37619)
- [Upgrade RoaringBitmap to 0.9.23](https://issues.apache.org/jira/browse/SPARK-37653)
- [Upgrade log4j from 2.17 to 2.17.1](https://issues.apache.org/jira/browse/SPARK-37774)
- [Upgrade h2 from 1.4.195 to 2.0.202](https://issues.apache.org/jira/browse/SPARK-37734)
- [Upgrade SLF4J to 1.7.32](https://issues.apache.org/jira/browse/SPARK-37790)

#### Что делать?

Версия `3.3` выглядит отлично, много багов пофикшено и много возможностей добавлено, разработка не останавливается 
и будут новые фичи и новые фиксы. Как в текущих реалиях понять стоит ли переходить с `3.2.1` на `3.3.0/3.3.1` ?
В рамках тестового задания ответ - никак. Нужно знать особенности конкретного проекта, сколько в нем легаси кода,
оценить трудозатраты при переезде на новые версии и т.д. Наиболее приемлемым вариантом видится построение разработки на рельсы  
в "ногу со временем", более частый плавный апгрейд "мелких" инструментов на проекте и переодические апгрейды крупных, но без 
оголтелой гонки за всем модным и новым.
