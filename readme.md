  
1.
Tools used for Implementation:
Python, Postgres,  Apollo GraphQL API, Flask web server

I went ahead with Python due to it's simple and amazing exchange of resources to integrate the environemnts of Google Cloud, Postgres, a GraphQL API and Flask web server. 
Python has great interoperability with these tools to deliver on accomplishment of the task which is heavily data based.
Python has a Command Line Interface for accessing Google Cloud called "gs" which was used to fetch csv data.
Libraries such as ariadne was perfect for Python on defining schemas from scratch for the GraphQL API implementation.
SQLAlchemy was used for the Postgres integration into the Python environment.
Pandas was used for data manipulation and processing parallel mechanisms.
Flask library was used for ease of setup of the web server for the GraphQL API setup.

2.
I must say this excercise was a very good one and focuses on the importance of performance scaling using the right tools with a focus on the right hardware resouces when processing massive amount of data.
On my attempt to do the operation, I realize hardware specifications are utmost important.
The computer I had used for this operation has 12gb Ram with Intel i7 Core and 256 SSD NVMe drive & 2TB Internal Hard Disk.
Internet Speed was very important also.
I had to pay attention to limits of my hardware specifications and design the code to process the data in batches to utilize the available resources.

3.
Performance Metrics include:

First up tho, I had tried to use Python with Google Cloud CLI to fetch the data from Google Cloud directly into memory to push to Postgres, but this was too expensive.
I decided it was best to fetch the csv objects and store unto my local computer.
This process was completed in about 2 hrs 30 mins with my current internet speed at 10MB/s. 
if I opted for high internet speed then this time could be cut in half.
Fetched from Google Cloud included: 1282 csv objects in the token-transfer folder and 1 csv object in token folder with combined size of approximately 64.5GB 

Python was used to prepare the csv objects in batches in order to push to the Postgres database.
This operation was completed in about 2 hours with my current hardware spefications as described.
ingested into Postgres was 219,222,954 rows from token-transfers as well as 144,716 rows from the token folders.

Performance was good regarding ingestion of data in GraphQL API, I had designed query to select n number of records directly from Postges database as a Response via the API.
Otherwise other queries could be designed with arguments to control data flow via GraphQL API Response.


4.
For the purposes of a Production Application, there needs to be careful consideration of the tools/stack to be used for implementation since focus is on performing operations on massive amount of structured and unstructured data across multiple environments. I really like how the mentioned tools (Python, Postgres, Apollo GraphQL API, Flask Web) work together to get the operation done from scratch. More tests could be done to compare performance of other popular tools such as Node.JS in integrating massive amount of data from various API systems.

5.
Docker/ Kubernetes are most popular deployment platforms to package the core of the final application to make sure proper functioning across various environments.

