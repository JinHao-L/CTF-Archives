import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.util.Base64;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

class Scratch {
    public static final String ani = "9EuOL+hToZVoYKand7aM47Qdq2uZs2kRjmiKDZDaApg=";
    public static final String b = "UEJLREYyV2l0aEhtYWNTSEEyNTY=";
    public static final String gajjae = "aE+NsnTAQ51wReH4oSQAwuA9IwF8njqcY8bEzTZZ8Kk=";
    public static final String saline_water = "nomorethan8";
    public static final String hospital_ward = "N0H4Ts_mobileCTF";
    public static final String app_name = "I_Spy_With_My_Little_Eye";
    public static final String birth_time = "MTYxMzgzNjgwMA==";
    public static final String decrypt_me = "Decrypt Me!";
    public static final String majayo = "a911ZJ31XupABHKqs4jimsbG2irv1u/jmKjPw9uWf7Mo6zDNiCp9JzVFfOxP+I9o";


    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeySpecException, InvalidAlgorithmParameterException, NoSuchPaddingException, IllegalBlockSizeException, BadPaddingException, InvalidKeyException {

        String start = "MT";
        start += "Yx";
        start += "Mz";
        start += "gz";
        start += "Nj";
        start += "gw";
        start += "MA";
        start += "==";
        start = new String(Base64.getDecoder().decode(start));
        String alg = new String(Base64.getDecoder().decode(b));
        System.out.println(alg);
        PBEKeySpec spec = new PBEKeySpec(start.toCharArray(), saline_water.getBytes(), 65536, 256);
        SecretKey key = new SecretKeySpec(SecretKeyFactory.getInstance(alg).generateSecret(spec).getEncoded(), "AES");

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        cipher.init(2, key, new IvParameterSpec(hospital_ward.getBytes()));

        String out = new String(cipher.doFinal(Base64.getDecoder().decode(majayo)));
        System.out.println(out);
    }
}