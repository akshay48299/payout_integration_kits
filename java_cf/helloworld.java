import java.util.Scanner;  // needed for Scanner
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.net.*;
import java.io.*;
import java.util.List;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;



public class helloworld {
    public static String token;
    public static String expiry;
    public static String clientId;
    public static String clientSecret;

    
    public void clientAuth(String clientId, String clientSecret) {
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        HashMap<String,String> headers =new HashMap<String,String>();
        String postData = "";
        
        headers.put("X-Client-Id",clientId);
        headers.put("X-Client-Secret", clientSecret);

        String link = "https://payout-gamma.cashfree.com//payout/v1/authorize";

        String response = makePostCall(link,headers,postData);
        System.out.println(response);


       // JSONParser parser = new JSONParser();
        //JSONObject responseObj = (JSONObject) parser.parse(response);
        
       // Gson u = new Gson();
        /*URLConnection linkAuthorize = new URL("https://payout­-gamma.cashfree.com//payout/v1/authorize").openConnection();
        linkAuthorize.setDoOutput(true);
        linkAuthorize.setRequestProperty("Accept-Charset", "UTF-8");
        linkAuthorize.setRequestProperty("Content-Type", "application/x-www-form-urlencoded;charset=" + "UTF-8");
        try (OutputStream responseAuthorize = linkAuthorize.getOutputStream()) {
            responseAuthorize.write(query.getBytes("UTF-8"));
        }*/




       // URLConnection responseAuthorize = linkAuthorize.openConnection();


       // System.out.println("ClientId : " + clientId);
        //System.out.println("clientSecret : " + clientSecret);

    }

    public String makePostCall(String link, Map<String, String> headers, String postData)
    {
        String response = "";
        try {
            URL myURL = new URL(link);

            HttpURLConnection conn = (HttpURLConnection)myURL.openConnection();

            for(Map.Entry m:headers.entrySet()){
                conn.setRequestProperty(m.getKey().toString(),m.getValue().toString());
            }

            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("Content-Length", "" + postData.getBytes().length);

            conn.setUseCaches(false);
            conn.setDoInput(true);
            conn.setDoOutput(true);

            OutputStream os = conn.getOutputStream();
            os.write(postData.getBytes());
            os.flush();

            if (conn.getResponseCode() != HttpURLConnection.HTTP_OK) {
                throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));

            String output;
            while ((output = br.readLine()) != null) {
                response += output;
            }

            conn.disconnect();

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.print(response);
        return response;
    }


    public static void main(String[] args){
        helloworld newuser = new helloworld();
        
        newuser.clientAuth("CF27D9CZCLC0ZHYUE26", "CF27D9CZCLC0ZHYUE26");

        System.out.println(newuser.clientId);
        
    }
 }

