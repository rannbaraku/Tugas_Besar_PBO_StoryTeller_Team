-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 16, 2021 at 09:21 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Newperpus`
--

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `id_item` char(20) NOT NULL,
  `id_perpustakaan` char(20) DEFAULT NULL,
  `kategori` varchar(50) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `tahun_produksi` varchar(4) NOT NULL,
  `salinan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`id_item`, `id_perpustakaan`, `kategori`, `judul`, `penulis`, `penerbit`, `tahun_produksi`, `salinan`) VALUES
('222', 'ITERA_002', 'Buku', 'Aku dan debu debu jalanan', '222', '222', '222', 222),
('333', 'ITERA_003', 'Artikel-Jurnal', 'Kyoto dan Reformasi Periode 3', 'Oda nobunaga', 'Hajime Isiyama', '2008', 11),
('BOOK_001', 'ITERA_001', 'Buku', 'Akuntansi Pengantar 1', 'Supardi', 'Gava Media', '2009', 2),
('BOOK_002', 'ITERA_002', 'Artikel-Jurnal', 'Aplikasi Klinis Induk Ovulasi & Stimulasi Ovariu', 'Samsulhadi', 'Sagung Seto', '2013', 3),
('BOOK_003', 'ITERA_003', 'Buku', 'Islam Jawa; Kesalehan Normatif Versus Kebatinan', 'Mark R. Woodward', 'LKiS', '2004', 4),
('BOOK_004', 'ITERA_001', 'Buku', 'Runtuhnya Kerajaan Hindu Jawa', 'Slamet Muljana', 'LKiS', '2007', 5),
('BOOK_005', 'ITERA_002', 'Media Digital', 'Pemrograman Web Membuat Sistem Informasi Akademik ', 'Bunafit Nugroho', 'Gava Media', '2014', 6),
('BOOK_006', 'ITERA_002', 'Media Digital', 'Analisis Kondisi Mental Sayu dalam Higehiro Series', 'rein kuriyama', 'Aniplex', '2021', 1),
('BOOK_013', 'ITERA_001', 'Artkel-Jurnal', 'Apakah kucing termasuk fluida ', 'Yukibara', 'Waskito.corp', '2021', 2);

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id_pelanggan` char(20) NOT NULL,
  `type` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(200) NOT NULL,
  `no_hp` char(20) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`id_pelanggan`, `type`, `nama`, `alamat`, `no_hp`, `email`) VALUES
('P_001', 'Gold', 'Samuel', 'Siantar', '081209876321', 'samuel@gmail.com'),
('P_002', 'Gold', 'Rifan', 'Pringsewu', '089876123453', 'rifan@gmail.com'),
('P_003', 'Gold', 'Yukibara', 'Kiyoto', '09877990', 'yukinee@gmain.jp');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id_pelanggan` char(20) DEFAULT NULL,
  `tanggal_peminjaman` date NOT NULL,
  `id_item` char(20) DEFAULT NULL,
  `tanggal_pengembalian` date DEFAULT NULL,
  `biaya` int(10) NOT NULL,
  `Status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `peminjaman`
--

INSERT INTO `peminjaman` (`id_pelanggan`, `tanggal_peminjaman`, `id_item`, `tanggal_pengembalian`, `biaya`, `Status`) VALUES
('P_002', '2021-01-01', 'BOOK_005', '2021-02-02', 0, 'Dikembalikan'),
('P_001', '2021-01-01', 'BOOK_005', '2021-04-04', 3000, 'Dikembalikan'),
('P_003', '2021-05-05', 'BOOK_006', '2021-06-06', 0, 'Dikembalikan');

-- --------------------------------------------------------

--
-- Table structure for table `perpustakaan`
--

CREATE TABLE `perpustakaan` (
  `id_perpustakaan` char(20) NOT NULL,
  `nama_perpustakaan` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `perpustakaan`
--

INSERT INTO `perpustakaan` (`id_perpustakaan`, `nama_perpustakaan`) VALUES
('ITERA_001', 'Perpustakaan GKU'),
('ITERA_002', 'Perpustakaan Gedung E'),
('ITERA_003', 'Perpustakaan LabTek II');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`id_item`),
  ADD KEY `id_perpustakaan` (`id_perpustakaan`);

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD KEY `id_item` (`id_item`),
  ADD KEY `id_pelanggan` (`id_pelanggan`);

--
-- Indexes for table `perpustakaan`
--
ALTER TABLE `perpustakaan`
  ADD PRIMARY KEY (`id_perpustakaan`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `item`
--
ALTER TABLE `item`
  ADD CONSTRAINT `item_ibfk_1` FOREIGN KEY (`id_perpustakaan`) REFERENCES `perpustakaan` (`id_perpustakaan`);

--
-- Constraints for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`id_item`) REFERENCES `item` (`id_item`),
  ADD CONSTRAINT `peminjaman_ibfk_2` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
