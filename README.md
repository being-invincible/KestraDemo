# Kestra Introduction Demo
Introduction to workflow orchestration with Kestra


In this repo, I will explore Kestra, a workflow orchestration tool to write an ETL pipeline to ingest NY Taxi Data to Postgres (locally) and in BigQuery (GCP Cloud)

## What is Kestra?

## How to get started?
You can use docker to start your project with Kestra quickly. You can also find the same docker command from !(Kestra Documentation)[https://kestra.io/docs/getting-started/quickstart].

```docker
docker run --pull=always --rm -it -p 8080:8080 --user=root -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local
```

This is only to get you started quickly. To save your workflows in your Kestra instance, we need to use docker-compose. This particular command will download the docker-compose.yml file to setup Kestra and Postgres

```bash
curl -o docker-compose.yml \
https://raw.githubusercontent.com/kestra-io/kestra/develop/docker-compose.yml
```

Run **docker compose up** to start your project. Head to 'localhost:8080'.

## Build your first ETL in Kestra:
I am gonna use the NY taxi dataset (Green and Yellow), and use inputs and variables from Kestra to dynamically extract the data. 

combine them into a staging table and load them into 
