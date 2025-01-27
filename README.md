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
I am gonna load the NY Taxi dataset which is split into years and months into a stagging table to combine them all and then load it into a Postgres DB for further conduct analysis. 

I am gonna use the NY taxi dataset (Green and Yellow), and define inputs and variables from Kestra to dynamically extract the data. Then combine them into a stagging table and load them into a final database as clean data.

### Inputs

1. Colour of the dataset (yellow or green)
2. Year (2019, 2020)
3. Month (1 to 12)

```yml
inputs:
  - id: taxi
    type: SELECT
    displayName: Select taxi type
    values: [yellow, green]
    defaults: yellow

  - id: year
    type: SELECT
    displayName: Select year
    values: ["2019", "2020"]
    defaults: "2019"

  - id: month
    type: SELECT
    displayName: Select month
    values: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    defaults: "01"
```

Kestra variables allow dynamic rendering of the inputs. Let's create the variables as follows,
1. For the file name
2. For staging table
3. For the database which has all the combined data
4. The data itself (The output of the extraction)

```yml
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public.{{inputs.taxi}}_tripdata_staging"
  table: "public.{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv']}}"
```

Follow this code to understand more about it and use it in your custom workflows. 

```yml

```
