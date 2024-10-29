# Dockerfile
# Use an official Python image as the base
FROM ubuntu:22.04

WORKDIR /app

# Set environment variables for versions and paths
ENV HADOOP_VERSION=3.3.0
ENV SPARK_VERSION=3.5.3
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_HOME=/app/hadoop
ENV SPARK_HOME=/app/spark
ENV PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON=python3
# Update and install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    curl \
    wget \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Install Hadoop
RUN wget https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz && \
    mv /app/hadoop-$HADOOP_VERSION $HADOOP_HOME && \
    rm hadoop-$HADOOP_VERSION.tar.gz

# Install Spark
RUN wget https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz && \
    tar -xzvf spark-$SPARK_VERSION-bin-hadoop3.tgz && \
    mv /app/spark-$SPARK_VERSION-bin-hadoop3 $SPARK_HOME && \
    rm spark-$SPARK_VERSION-bin-hadoop3.tgz


 

# Install Jupyter and PySpark
RUN pip install jupyter pyspark

# Expose ports for Jupyter, Hadoop, and Spark UI


# Expose Spark and Jupyter ports
EXPOSE 7077 8080 4040 8888 9870

# Copy entrypoint script
COPY makessh.sh /makessh.sh
RUN chmod +x /makessh.sh

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set the entrypoint to the start script
ENTRYPOINT ["/start.sh"]