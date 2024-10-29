#!/bin/bash

# Start the Spark master
$SPARK_HOME/sbin/start-master.sh

# Start Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=''

# Keep the container running
tail -f /dev/null