## Snowflake Cortex AI Agent

## Overview
This project demonstrates a Snowflake Intelligence Agent built using Snowflake Cortex Analyst and Cortex Search to enable natural language analytics over structured data stored in Snowflake. The system allows users to ask questions in plain English and receive real-time SQL-powered insights.

This project showcases how large language models, vector search, and cloud data warehousing can be integrated into a secure, production-style AI workflow.


## Architecture
- Snowflake Data Warehouse
- Snowflake Cortex Search (semantic retrieval)
- Snowflake Cortex Analyst (natural language to SQL)
- Snowflake Intelligence Agent
- SQL-based data ingestion and transformation


## Tech Stack
- Snowflake SQL
- Snowflake Cortex Search
- Snowflake Cortex Analyst
- Snowflake Intelligence
- Cloud-based vector storage (Snowflake managed)


## Data Pipeline
1. Data uploaded into Snowflake using SQL `COPY INTO`
2. Data cleaned and transformed using Snowflake SQL
3. Indexed with Cortex Search for semantic retrieval
4. Queried using Cortex Analyst with natural language
5. Responses generated through Snowflake Intelligence Agent


## Key Features
- Natural language to SQL querying
- Semantic vector search using Cortex Search
- Fully cloud-native AI deployment
- Secure enterprise-grade data handling
- Serverless architecture inside Snowflake

  ## Snowflake Intelligence Agent Setup
  The Snowflake Intelligence Agent for this project was configured via the Snowflake UI:
  - Connected the `BOOKS_SEMANTIC_VIEW` semantic model as the data source
  - Linked the `GOODREADS_SEARCH` Cortex Search service for semantic retrieval over `AUTHOR`, `TITLE`, and `URL`
  - Enabled natural language querying over the `GOODREADS_BOOKS` table
  - Tested questions such as:
  - "Show me highly rated fantasy books"
  - "List books by authors similar to Brandon Sanderson"
  
  Because the configuration is UI-driven, there is no standalone SQL file for the agent setup. Instead, the semantic model (`semantic/BOOKS_SEMANTIC_VIEW.yaml`) and Python client (`src/cortex_search_client.py`) demonstrate how the agent is powered under the hood.

## Demo Screenshots
Screenshots of the Cortex Search service, Analyst queries, and results are available in the `screenshots/` folder.

## What This Demonstrates
- Cloud AI Engineering
- RAG-style retrieval inside Snowflake
- SQL-powered ML workflows
- Vector search and LLM orchestration
- Enterprise data platform integration


## Future Improvements
- Add Snowflake Streamlit UI
- Integrate Snowpipe for real-time ingestion
- Add unstructured document ingestion
- Add query feedback optimization


## Author
Kavya Malgi  
Statistics & Data Science – UT Austin  
Snowflake SnowPro Certified
