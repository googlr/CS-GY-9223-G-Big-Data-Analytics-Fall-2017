from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here
    def get_bigram(s):
        bigrams = []
        words = s.split(" ")
        for i in range(0, len(words)-1):
            bigrams.append( ((s[i],s[i+1]),1))

        return sc.parallelize(bigrams)
    #bigrams = []
    #for sentence in sentences:
     #   s = sentence.split(" ")
      #  for i in range(0, len(s)-1):
       #     bigrams.append( ((s[i],s[i+1]), 1) )


    top100bigram = sentences.map(lambda s: get_bigram(s)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False).take(100)
    top100bigram.saveAsTextFile("top100bigram.out")
              

    sc.stop()
