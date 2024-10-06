-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 06 Eki 2024, 10:53:30
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `nasa`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanicilar3`
--

CREATE TABLE `kullanicilar3` (
  `id` int(11) NOT NULL,
  `cinsiyet` varchar(10) NOT NULL,
  `soru1` varchar(50) NOT NULL,
  `soru2` varchar(50) NOT NULL,
  `soru3` varchar(50) NOT NULL,
  `soru4` varchar(50) NOT NULL,
  `soru5` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `kullanicilar3`
--

INSERT INTO `kullanicilar3` (`id`, `cinsiyet`, `soru1`, `soru2`, `soru3`, `soru4`, `soru5`) VALUES
(13, 'erkek', 'temizlik_ferahlık', 'temizlik_ferahlık', 'temizlik_ferahlık', 'temizlik_ferahlık', 'temizlik_ferahlık'),
(14, 'kiz', 'sogukluk', 'sogukluk', 'sogukluk', 'sogukluk', 'sogukluk'),
(15, 'erkek', 'temizlik_ferahlık', 'yalnizlik', 'temizlik_ferahlık', 'temizlik_ferahlık', 'umut_yenilik'),
(16, 'erkek', 'temizlik_ferahlık', 'bosluk', 'umut_yenilik', 'yalnizlik', 'huzur'),
(17, 'erkek', 'bosluk', 'umut_yenilik', 'yalnizlik', 'huzur', 'sogukluk'),
(18, 'erkek', 'yalnizlik', 'yalnizlik', 'yalnizlik', 'yalnizlik', 'yalnizlik'),
(19, 'kiz', 'huzur', 'yalnizlik', 'bosluk', 'temizlik_ferahlık', 'sogukluk'),
(20, 'erkek', 'temizlik_ferahlık', 'bosluk', 'huzur', 'sogukluk', 'sogukluk');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `kullanicilar3`
--
ALTER TABLE `kullanicilar3`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kullanicilar3`
--
ALTER TABLE `kullanicilar3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
