'''use cortex search when you want hybrid search (combination of vector embedding and keyword search)'''

create or replace database BUILD_DEMO;
use database BUILD_DEMO;
create or replace schema BOOKS_DATA;
use schema BOOKS_DATA;

CREATE or replace TABLE GOODREADS_BOOKS
(
TITLE VARCHAR,
AUTHOR VARCHAR,
URL VARCHAR,
STAR_RATING NUMBER
)
AS
SELECT
NAME,
AUTHOR,
URL,
TO_NUMBER(STAR_RATING)
FROM AI_TRAINING_DATASET_FROM_GOODREADS_BOOKS.PUBLIC.GOODREADSBOOK;

SELECT * FROM GOODREADS_BOOKS;

