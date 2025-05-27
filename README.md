# Real-Time Public Transit Tracking & Data Analysis

## Project Overview

This project aims to provide **real-time updates** about public transit systems, focusing on **delays** and **estimated arrival times** for transit vehicles such as buses. Our prototype is built specifically for **Bloomington, Indiana**, but the architecture is scalable to other cities and transit systems.

We have used open-source tools such as **Kafka**, **Apache Spark**, and **PostgreSQL**.
---

## Problem Solved

Passengers often face uncertainty with bus/train arrival times and unexpected delays. This system addresses that by:

- Pulling real-time data in the form of:
  - **Alerts**
  - **Vehicle Position Updates**
  - **Trip Updates**
- Processing this data to:
  - Track vehicle location
  - Detect delays
  - Estimate arrival times

---

## Core Components

| Component       | Purpose                            | Free Tool Used                               |
|-----------------|------------------------------------|----------------------------------------------|
| **Kafka**       | Real-time data ingestion           | Local setup using Docker                     |
| **Spark**       | Stream processing & ETL            | Apache Spark on Databricks Community Edition |
| **PostgreSQL**  | Processed data storage             | Local or free-tier PostgreSQL DB             |
| **Dashboard**   | Visualization of real-time status  | Streamlit / Grafana (local) / REST API       |

---

## System Architecture

[Simulated GPS / Public Transit API (GTFS-RT)]

|
[Kafka Producer]

|
[Kafka Broker (Docker)]

|
[Spark Structured Streaming Job]

|
[Transformations & ETA Logic]

|
[PostgreSQL / Delta Table Storage]

|
[Streamlit Dashboard / REST API]

