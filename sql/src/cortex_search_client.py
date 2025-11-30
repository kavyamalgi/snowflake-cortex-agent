import os
from snowflake.core import Root
from snowflake.snowpark import Session

CONNECTION_PARAMETERS = {
	"account": os.environ["your_account_info"],
	"user": os.environ["your_username"],
	"password": os.environ["your_password"],
	"role": "test_role",
	"warehouse": "test_warehouse",
	"database": "BUILD_DEMO",
	"schema": "BOOKS_DATA",
}

session = Session.builder.configs(CONNECTION_PARAMETERS).create()
root = Root(session)

# fetch service
my_service = (root
	.databases["BUILD_DEMO"]
	.schemas["BOOKS_DATA"]
	.cortex_search_services["GOODREADS_SEARCH"]
)

# query service
resp = my_service.search(
	query="<your query here>",
	columns=["TITLE", "STAR_RATING", "AUTHOR", "URL"],
	limit=10,
)

print(resp.to_json())
