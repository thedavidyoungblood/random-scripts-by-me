# Qdrant Docs:
# https://qdrant-client.readthedocs.io/en/latest/quickstart.html
# https://github.com/qdrant/qdrant-client

# Master 'qdrant_client_import' Script Template for Python

# ---------------------------
# Environment Setup Instructions
# ---------------------------
# Ensure Python 3.8+ is installed on your system.
# Create a virtual environment to manage dependencies:
# python3 -m venv qdrant_env
# Activate the virtual environment:
# source qdrant_env/bin/activate (Linux/Mac) or qdrant_env\Scripts\activate (Windows)
# Install the necessary packages using the requirements.txt file:
# pip install -r requirements.txt

# ---------------------------
# Importing Modules
# ---------------------------
# Import the necessary modules from the Qdrant client library
from qdrant_client import QdrantClient, models, AsyncQdrantClient
import numpy as np
import asyncio
import logging
import os

# ---------------------------
# Logging Setup
# ---------------------------
# Set up basic logging to track the flow of operations and debug issues
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ---------------------------
# Configuration Section
# ---------------------------
# Configure your settings here, such as collection names, vector sizes, and connection parameters
COLLECTION_NAME = "my_collection"
VECTOR_SIZE = 100
HOST = "localhost"
PORT = 6333
GRPC_PORT = 6334

# ---------------------------
# Error Handling
# ---------------------------
# Wrap function calls in try-except blocks to handle any potential errors
try:
    # ---------------------------
    # Connecting to Qdrant Server
    # ---------------------------
    # Replace "localhost" and "6333" with your server's host and port
    client = QdrantClient(host=HOST, port=PORT)
    logging.info("Connected to Qdrant server.")

    # ---------------------------
    # Function Call Examples
    # ---------------------------
    # Uncomment the lines below to call functions and perform operations

    # Create a new collection
    # create_collection(client)

    # Insert vectors into a collection
    # insert_vectors(client)

    # Search for similar vectors
    # hits = search_vectors(client)
    # logging.info(f"Search results: {hits}")

    # Search for similar vectors with filtering condition
    # filtered_hits = search_vectors_with_filter(client)
    # logging.info(f"Filtered search results: {filtered_hits}")

    # ---------------------------
    # Resource Cleanup
    # ---------------------------
    # Properly close connections and clean up resources after operations are complete
    # client.close()
    # logging.info("Closed connection to Qdrant server.")

except Exception as e:
    logging.error(f"An error occurred: {e}")

# ---------------------------
# Function Definitions
# ---------------------------
# Definitions of functions to interact with Qdrant

def create_collection(client):
    """
    Create a new collection in Qdrant.
    :param client: QdrantClient instance
    """
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
        )
        logging.info(f"Created collection '{COLLECTION_NAME}'.")
    except Exception as e:
        logging.error(f"Error creating collection: {e}")

def insert_vectors(client):
    """
    Insert vectors into the specified collection.
    :param client: QdrantClient instance
    """
    try:
        vectors = np.random.rand(100, VECTOR_SIZE)
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=idx,
                    vector=vector.tolist(),
                    payload={"color": "red", "rand_number": idx % 10}
                )
                for idx, vector in enumerate(vectors)
            ]
        )
        logging.info(f"Inserted vectors into collection '{COLLECTION_NAME}'.")
    except Exception as e:
        logging.error(f"Error inserting vectors: {e}")

def search_vectors(client):
    """
    Search for similar vectors in the collection.
    :param client: QdrantClient instance
    :return: Search results
    """
    try:
        query_vector = np.random.rand(VECTOR_SIZE)
        hits = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=5  # Return 5 closest points
        )
        logging.info("Performed vector search.")
        return hits
    except Exception as e:
        logging.error(f"Error searching vectors: {e}")

def search_vectors_with_filter(client):
    """
    Search for similar vectors with filtering condition.
    :param client: QdrantClient instance
    :return: Filtered search results
    """
    try:
        query_vector = np.random.rand(VECTOR_SIZE)
        hits = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            query_filter=models.Filter(
                must=[  # These conditions are required for search results
                    models.FieldCondition(
                        key='rand_number',  # Condition based on values of `rand_number` field.
                        range=models.Range(
                            gte=3  # Select only those results where `rand_number` >= 3
                        )
                    )
                ]
            ),
            limit=5  # Return 5 closest points
        )
        logging.info("Performed filtered vector search.")
        return hits
    except Exception as e:
        logging.error(f"Error searching vectors with filter: {e}")

# ---------------------------
# Async Client Usage
# ---------------------------
# Uncomment the following lines to use the asynchronous version of QdrantClient
# async def main():
#     async_client = AsyncQdrantClient(url=f"http://{HOST}:{PORT}")
#     await async_client.create_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
#     )
#     # Include other async operations here
#     # ...
#     logging.info("Async operations completed.")
#     await async_client.close()

#     # Uncomment the line below to run the async main function
#     # asyncio.run(main())

# ---------------------------
# Further Resources
# ---------------------------
# For more detailed documentation, tutorials, and community support, visit:
# Qdrant Documentation: https://qdrant.tech/documentation/
# Qdrant Tutorials: https://qdrant.tech/tutorials/
# Qdrant GitHub Repository: https://github.com/qdrant/qdrant

# ---------------------------
# Virtual Environment Instructions
# ---------------------------
# It's recommended to run this script within a virtual environment.
# This helps manage dependencies and avoid conflicts.
# Follow the environment setup instructions at the beginning of this script.

# ---------------------------
# Requirements File
# ---------------------------
# A requirements.txt file should be present in the same directory as this script.
# It lists all the necessary packages for the project.
# Use the command 'pip install -r requirements.txt' to install them.

# ---------------------------
# Security Best Practices
# ---------------------------
# Secure your API keys and sensitive data.
# Consider using environment variables or a .env file to store them.
#
# Example:
# import os
# from dotenv import load_dotenv
# from qdrant_client import QdrantClient

# load_dotenv()  # Load environment variables from .env file

# qdrant_client = QdrantClient(
#     url=os.getenv("QDRANT_URL"), 
#     api_key=os.getenv("QDRANT_API_KEY"),
# )
