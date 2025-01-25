# Kestra Introduction Demo
Introduction to workflow orchestration with Kestra


In this repo, I will explore Kestra, a workflow orchestration tool to write an ETL pipeline to ingest NY Taxi Data to Postgres (locally) and in BigQuery (GCP Cloud)

## What is Kestra?

## How to get started?
You can use docker to start your project with Kestra quickly. You can also find the same docker command from (Kestra Documentation)[https://kestra.io/docs/getting-started/quickstart].

```docker
docker run --pull=always --rm -it -p 8080:8080 --user=root -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local
```
