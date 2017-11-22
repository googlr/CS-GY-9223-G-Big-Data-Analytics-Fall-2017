import numpy as np
from math import sqrt
from operator import add
from pyspark.mllib.clustering import KMeans, KMeansModel
csvfile = sc.textFile('/user/ecc290/lab9/sensordatasmall/part-00000')
sensordata = csvfile.map(lambda line: line.split(','))
sdfilt = sensordata.filter(lambda x:
np.count_nonzero(np.array([int(x[6]), int(x[7]),
int(x[8])]))>0)
sdfilt.count()
vso = sdfilt.map(lambda x: np.array([int(x[6]),
int(x[7]), int(x[8])]))

def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))
for i in range(1,11):
    clusters = KMeans.train(vso, i, maxIterations=10, initializationMode="random")
    WSSSE = vso.map(lambda point: error(point)).reduce(add)
    print("Within Set Sum of Squared Error, k = " + str(i) + ": " + str(WSSSE))
clusters = KMeans.train(vso, 3, maxIterations=10, initializationMode="random")
for i in range(0,len(clusters.centers)):
    print("cluster " + str(i) + ": " + str(clusters.centers[i]))
clusters = KMeans.train(vso, 4, maxIterations=10, initializationMode="random")
for i in range(0,len(clusters.centers)):
    print("cluster " + str(i) + ": " + str(clusters.centers[i]))
def addclustercols(x):
    point = np.array([float(x[6]), float(x[7]), float(x[8])])
    center = clusters.centers[0]
    mindist = sqrt(sum([y**2 for y in (point - center)]))
    cl = 0
    for i in range(1,len(clusters.centers)):
        center = clusters.centers[i]
        distance = sqrt(sum([y**2 for y in (point - center)]))
        if distance < mindist:
            cl = i
            mindist = distance
    clcenter = clusters.centers[cl]
    return (int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), float(x[5]), int(x[6]), int(x[7]), int(x[8]), int(cl), float(clcenter[0]), float(clcenter[1]), float(clcenter[2]), float(mindist))
rdd_w_clusts = sdfilt.map(lambda x: addclustercols(x))
rdd_w_clusts.map(lambda y: (y[9],1)).reduceByKey(add).top(len(clusters.centers))
schema_sd = sqlContext.createDataFrame(rdd_w_clusts, ('highway','sensorloc', 'sensorid', 'doy', 'dow', 'time','p_v','p_s','p_o', 'cluster', 'c_v', 'c_s', 'c_o', 'dist'))
schema_sd.registerTempTable("sd")
sqlContext.sql("SELECT * FROM sd WHERE dist>50").show()
stats = sqlContext.sql("SELECT cluster, c_v, c_s, c_o, count(*) AS num, max(dist) AS maxdist, avg(dist) AS avgdist,stddev_pop(dist) AS stdev FROM sd GROUP BY cluster, c_v, c_s, c_o ORDER BY cluster")
stats.show()
def inclust(x, t):
    cl = x[9]
    c_v = x[10]
    c_s = x[11]
    c_o = x[12]
    distance = x[13]
    if float(distance) > float(t):
        cl = -1
        c_v = 0.0
        c_s = 0.0
        c_o = 0.0
    return (int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), float(x[5]), int(x[6]), int(x[7]), int(x[8]), int(cl), float(c_v), float(c_s), float(c_o), float(distance))
rdd_w_clusts_wnullclust = rdd_w_clusts.map(lambda x: inclust(x,20))
rdd_w_clusts_wnullclust.map(lambda y: (y[9],1)).reduceByKey(add).top(5)
schema_sd = sqlContext.createDataFrame(rdd_w_clusts_wnullclust, ('highway','sensorloc', 'sensorid', 'doy', 'dow', 'time','p_v','p_s','p_o', 'cluster', 'c_v','c_s','c_o','dist'))
schema_sd.registerTempTable("sd_nc")
sqlContext.sql("SELECT p_v, p_s, p_o FROM sd_nc WHERE cluster=-1 LIMIT 100").show(100)
sqlContext.sql("SELECT sensorid, cluster, count(*) AS num_outliers, avg(c_s) AS spdcntr, avg(dist) AS avgdist FROM sd WHERE dist > 20 GROUP BY sensorid, cluster ORDER BY sensorid, cluster").show()
sqlContext.sql("SELECT cluster, doy, time, c_v,c_s,c_o, p_v,p_s,p_o FROM sd WHERE cluster=0 and dist >20 ORDER BY dist").show()
clusters = KMeans.train(vso, 5, maxIterations=10, initializationMode="random")
rdd_w_clustsk5 = sdfilt.map(lambda x: addclustercols(x))
schema_sd = sqlContext.createDataFrame(rdd_w_clustsk5, ('highway','sensorloc', 'sensorid', 'doy', 'dow', 'time', 'p_v', 'p_s', 'p_o', 'cluster', 'c_v', 'c_s', 'c_o', 'dist'))
schema_sd.registerTempTable("sdk5")
sqlContext.sql("SELECT cluster, c_v, c_s, c_o, count(*) AS num, max(dist) AS maxdist, avg(dist) AS avgdist,stddev_pop(dist) AS stdev FROM sdk5 GROUP BY cluster, c_v, c_s, c_o ORDER BY cluster").show()
rdd_w_clusts_wnullclustk5 = rdd_w_clustsk5.map(lambda x: inclust(x,20))
rdd_w_clusts_wnullclustk5.map(lambda y: (y[9],1)).reduceByKey(add).top(6)
sqlContext.sql("SELECT sensorid, cluster, count(*) AS num_outliers, avg(c_s) AS spdcntr, avg(dist) AS avgdist FROM sdk5 WHERE dist > 20 GROUP BY sensorid, cluster ORDER BY sensorid, cluster").show()
sqlContext.sql("SELECT cluster, doy, time, c_v,c_s,c_o, p_v,p_s,p_o FROM sdk5 WHERE cluster=4 and dist >20 ORDER BY dist").show()
schema_sd = sqlContext.createDataFrame(rdd_w_clusts_wnullclustk5, 
('highway','sensorloc', 'sensorid', 'doy', 'dow', 'time','p_v','p_s','p_o', 'cluster', 'c_v','c_s','c_o','dist'))
schema_sd.registerTempTable("sdk5nc")
cdata= sqlContext.sql("SELECT cluster, p_v, p_s, p_o FROM sdk5nc ORDER BY cluster")
cdata.repartition(1).write.format("k5clusts.csv")
# import readline
# readline.write_history_file('/home/pyspark/history')
# for i in range(readline.get_current_history_length()):
#         print readline.get_history_item(i + 1)