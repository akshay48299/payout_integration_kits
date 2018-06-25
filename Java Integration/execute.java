package cashfreeUser_java_integration;


public class execute{

    public static void main(String[] args)throws Exception {
        
        cfPayout newuser = new cfPayout();

        System.out.println(newuser.clientAuth("sampleClientId","sampleClientSecret","TEST/PROD"));

    }


}


