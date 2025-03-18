/* To connect Node to Mongodb we first have to install the mongodb packages into our project with the command "npm install mongodb"
if using Mongoose use "npm install mongoose". MongoClient is a low level mongodb driver that is best used for small applications
while mongoose is an ODM (Object-Data Mapping) for Mongodb best used for larger more complex applications*/

/*Import MongoClient from mongodb*/
const {MongoClient} = require('mongodb');

/* Use the command "npm install dotenv" into the project and import it */
require("dotenv").config();

/*Import the uri from the .env file that contains your connection string to mongodb*/
const uri = process.env.MONGO_URI;

/*Create an instance of MongoClient with the uri as the argument */
const client = new MongoClient(uri);

/*Here we set up the database connection */
async function connectDB(){
    try{
        await client.connect();
        console.log("Connected to mongoDb")

        const db = client.db("Test")
        return db;
    } catch (error){
        console.error("Connection failed!", error);
    }
}

/*Always be sure to call the function so that the conncetion intializes */
connectDB();