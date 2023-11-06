// This temlpamte is tailored for the Node.js ecosystem, using appropriate modules and syntax. It includes instructions 
// for setting up the environment, connecting to a Qdrant server, defining functions for interacting with Qdrant, and 
// handling errors. The script also provides further resources and best practices for securing API keys and sensitive 
// data. Users can uncomment and edit sections according to their needs, and the comments provide guidance on how to 
// use each part of the script.

// Qdrant Docs:
// https://qdrant-client.readthedocs.io/en/latest/quickstart.html
// https://github.com/qdrant/qdrant-client

// Master 'qdrant_client_import' Script Template for Node.js

// ---------------------------
// Environment Setup Instructions
// ---------------------------
// Ensure Node.js (LTS version) is installed on your system.
// Initialize your Node.js project with `npm init`.
// Install the necessary packages using the package.json file:
// npm install

// ---------------------------
// Importing Modules
// ---------------------------
// Import the necessary modules
const { QdrantClient, models } = require('qdrant_client'); // Import Qdrant client library
const axios = require('axios'); // Axios is used for HTTP requests
const dotenv = require('dotenv'); // Dotenv for loading environment variables
dotenv.config();

// ---------------------------
// Configuration Section
// ---------------------------
// Configure your settings here, such as collection names, vector sizes, and connection parameters
const COLLECTION_NAME = "my_collection";
const VECTOR_SIZE = 100;
const HOST = "localhost";
const PORT = 6333;
const GRPC_PORT = 6334;

// ---------------------------
// Error Handling
// ---------------------------
// Wrap function calls in try-catch blocks to handle any potential errors
try {
    // ---------------------------
    // Connecting to Qdrant Server
    // ---------------------------
    // Replace "localhost" and "6333" with your server's host and port
    const client = new QdrantClient(`${HOST}:${PORT}`);

    // ---------------------------
    // Function Call Examples
    // ---------------------------
    // Uncomment the lines below to call functions and perform operations

    // Create a new collection
    // createCollection(client);

    // Insert vectors into a collection
    // insertVectors(client);

    // Search for similar vectors
    // const hits = searchVectors(client);

    // Search for similar vectors with filtering condition
    // const filteredHits = searchVectorsWithFilter(client);

    // ---------------------------
    // Resource Cleanup
    // ---------------------------
    // Properly close connections and clean up resources after operations are complete

} catch (error) {
    console.error(`An error occurred: ${error}`);
}

// ---------------------------
// Function Definitions
// ---------------------------
// Definitions of functions to interact with Qdrant

function createCollection(client) {
    // Create a new collection in Qdrant
    client.recreateCollection(COLLECTION_NAME, {
        vector_params: new models.VectorParams(VECTOR_SIZE, models.Distance.COSINE)
    }).then(() => {
        console.log(`Created collection '${COLLECTION_NAME}'.`);
    }).catch(error => {
        console.error(`Error creating collection: ${error}`);
    });
}

function insertVectors(client) {
    // Insert vectors into the specified collection
    const vectors = Array.from({ length: 100 }, () => Array.from({ length: VECTOR_SIZE }, Math.random));
    client.upsert(COLLECTION_NAME, {
        points: vectors.map((vector, idx) => new models.PointStruct(
            idx,
            vector,
            { color: "red", rand_number: idx % 10 }
        ))
    }).then(() => {
        console.log(`Inserted vectors into collection '${COLLECTION_NAME}'.`);
    }).catch(error => {
        console.error(`Error inserting vectors: ${error}`);
    });
}

function searchVectors(client) {
    // Search for similar vectors in the collection
    const queryVector = Array.from({ length: VECTOR_SIZE }, Math.random);
    client.search(COLLECTION_NAME, {
        query_vector: queryVector,
        limit: 5 // Return 5 closest points
    }).then(hits => {
        console.log("Performed vector search.");
        return hits;
    }).catch(error => {
        console.error(`Error searching vectors: ${error}`);
    });
}

function searchVectorsWithFilter(client) {
    // Search for similar vectors with filtering condition
    const queryVector = Array.from({ length: VECTOR_SIZE }, Math.random);
    client.search(COLLECTION_NAME, {
        query_vector: queryVector,
        query_filter: new models.Filter([
            new models.FieldCondition('rand_number', new models.Range(null, 3)) // Select only those results where `rand_number` >= 3
        ]),
        limit: 5 // Return 5 closest points
    }).then(hits => {
        console.log("Performed filtered vector search.");
        return hits;
    }).catch(error => {
        console.error(`Error searching vectors with filter: ${error}`);
    });
}

// ---------------------------
// Further Resources
// ---------------------------
// For more detailed documentation, tutorials, and community support, visit:
// Qdrant Documentation: https://qdrant.tech/documentation/
// Qdrant Tutorials: https://qdrant.tech/tutorials/
// Qdrant GitHub Repository: https://github.com/qdrant/qdrant

// ---------------------------
// Security Best Practices
// ---------------------------
// Secure your API keys and sensitive data.
// Consider using environment variables or a .env file to store them.
// Example: 
// const QDRANT_URL = process.env.QDRANT_URL;
// const QDRANT_API_KEY = process.env.QDRANT_API_KEY;
// const qdrantClient = new QdrantClient(QDRANT_URL, { headers: { 'Authorization': `Bearer ${QDRANT_API_KEY}` } });
