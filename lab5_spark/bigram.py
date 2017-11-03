from operator import add
from pyspark import SparkContext

# 
# I referred some code from http://www.mccarroll.net/blog/pyspark2/
# in this homework
#

#@staticmethod
#def get_bigram(s):
 #       s_bigrams = []
  #      words = s.split(" ")
   #     for i in range(0, len(words)-1):
    #        s_bigrams.append( ((s[i],s[i+1]),1))
#
 #       return sc.parallelize(s_bigrams)
def split(line):
    words = line.split(" ")
    return [(words[i], words[i+1]) for i in range(len(words)-1)]


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
    bigrams = sentences.map(lambda x:x.split()) \
        .flatMap(lambda x: [((x[i],x[i+1]),1) for i in range(0,len(x)-1)])

    freq_bigrams = bigrams.reduceByKey(lambda x,y:x+y) \
        .map(lambda x:(x[0],x[1])) \
        .sortBy(lambda x: x[1],False)\
        .take(100)

    sc.parallelize(freq_bigrams).saveAsTextFile("bigram_count.out")

    sc.stop()
