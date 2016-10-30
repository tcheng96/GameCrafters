
from pyspark import SparkContext
from random  import uniform

conf = SparkConf().setAppName("gamesHW").setMaster("local")
sc = SparkContext(conf=conf)

naive =  sc.parallelize(range(1,1000)). \
            filter(lambda x: (x % 3 == 0) or (x % 5 == 0)). \
            reduce(lambda a, b: a + b)

print(naive)