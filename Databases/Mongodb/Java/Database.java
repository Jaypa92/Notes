import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;
import io.github.cdimascio.dotenv.Dotenv;

public class Database {
    public static void main(String[] args) {
        Dotenv dotenv = Dotenv.load();
        String uri = dotenv.get("MONGO_URI");

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            MongoDatabase database = mongoClient.getDatabase("test");
            System.out.println("Connected to database: " + database.getName());
        } catch (Exception e) {
            System.err.println("Connection failed: " + e.getMessage());
        }
    }
}