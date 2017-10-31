from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x.encode('utf-8'), 1)) \
                  .reduceByKey(add)

    counts.saveAsTextFile("wc.out")

    sc.stop()
