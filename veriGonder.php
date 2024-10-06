<?php
// veriGonder.php dosyası
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Veritabanı bağlantı bilgileri
    $host = 'localhost';  // Veritabanı sunucusu
    $dbname = 'nasa';     // Veritabanı adı
    $username = 'memirhan'; // MySQL kullanıcı adı
    $password = '123456';  // MySQL şifresi

    // Veritabanı bağlantısı oluşturma
    $conn = new mysqli($host, $username, $password, $dbname);

    // Bağlantıyı kontrol et
    if ($conn->connect_error) {
        die("Veritabanı bağlantısı başarısız: " . $conn->connect_error);
    }

    // Formdan gelen verileri al
    $cinsiyet = $_POST['cinsiyet'];
    $soru1 = $_POST['duygu_beyaz'];
    $soru2 = $_POST['duygu_siyah'];
    $soru3 = $_POST['duygu_mavi'];
    $soru4 = $_POST['duygu_kirmizi'];
    $soru5 = $_POST['duygu_sari'];

    // SQL sorgusu oluşturma
    $sql = "INSERT INTO kullanicilar3 (cinsiyet, soru1, soru2, soru3, soru4, soru5) VALUES ('$cinsiyet', '$soru1','$soru2','$soru3','$soru4','$soru5')";

    // Sorguyu çalıştırma
    if ($conn->query($sql) === TRUE) {
// Form verilerini işle ve kaydet (bu bölümde veriyi kaydettiğini varsayıyoruz)

// Burada veri kaydetme işlemini yap

// Başarı mesajını göstermek için
echo "<!DOCTYPE html>
<html lang='tr'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Başarılı</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            color: #28a745; /* Yeşil renk */
        }
    </style>
    <meta http-equiv='refresh' content='5;url=index.php'>
</head>
<body>
    <h1>Veri başarıyla kaydedildi!</h1>
    <p>5 saniye içinde ana sayfaya yönlendirileceksiniz...</p>
</body>
</html>";

    } else {
        echo "Hata: " . $sql . "<br>" . $conn->error;
    }

    // Veritabanı bağlantısını kapatma
    $conn->close();
    exit; // Form gönderildikten sonra sayfayı sonlandır
}
?>