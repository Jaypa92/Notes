import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import io.github.cdimascio.dotenv.Dotenv;

public class Main {
    public static void main(String[] args) {

        Dotenv dotenv = Dotenv.load();

        String url = dotenv.get("DB_URL");
        String user = dotenv.get("DB_USER");
        String pass = dotenv.get("DB_PASS");

        try{
            Connection conn = DriverManager.getConnection(url, user, pass);
            System.out.println("Connected to MySQL!");
            conn.close();
        } catch (SQLException e){
            System.out.println("Connection failed!");
            e.printStackTrace();
        }
    }
}