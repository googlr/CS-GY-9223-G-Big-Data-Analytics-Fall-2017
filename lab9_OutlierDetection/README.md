# Description
Outlier Detection with Spark MLLIB, SparkSQL

# Data
Data source/lab adapted from: https://aws.amazon.com/blogs/big-data/anomaly-detection-usingpyspark-hive-and-hue-on-amazon-emr/

# Setup on Dumbo
- Login to dumbo
- Set up environment:
```python
module load python/gnu/3.4.4
export PYSPARK_PYTHON=/share/apps/python/3.4.4/bin/python
export PYTHONHASHSEED=0
export SPARK_YARN_USER_ENV=PYTHONHASHSEED=0
```
- Start pyspark:
`pyspark`
