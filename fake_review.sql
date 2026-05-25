-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 04, 2022 at 04:28 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `fake_review`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `cs_cart`
--

CREATE TABLE `cs_cart` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pid` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `bill_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_cart`
--

INSERT INTO `cs_cart` (`id`, `uname`, `pid`, `status`, `rdate`, `bill_id`, `price`, `category`) VALUES
(1, 'suresh', 1, 1, '21-01-2022', 2, 12000, 'Mobile'),
(2, 'suresh', 2, 1, '21-01-2022', 2, 15000, 'Mobile'),
(3, 'suresh', 8, 1, '21-01-2022', 3, 25000, 'Laptop');

-- --------------------------------------------------------

--
-- Table structure for table `cs_category`
--

CREATE TABLE `cs_category` (
  `id` int(11) NOT NULL,
  `category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_category`
--

INSERT INTO `cs_category` (`id`, `category`) VALUES
(1, 'Mobile'),
(2, 'Laptop'),
(3, 'Men-TShirt'),
(4, 'Men-Shirt'),
(5, 'Women-Cloth');

-- --------------------------------------------------------

--
-- Table structure for table `cs_product`
--

CREATE TABLE `cs_product` (
  `id` int(11) NOT NULL,
  `category` varchar(30) NOT NULL,
  `product` varchar(50) NOT NULL,
  `price` bigint(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `star` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_product`
--

INSERT INTO `cs_product` (`id`, `category`, `product`, `price`, `photo`, `detail`, `star`) VALUES
(1, 'Mobile', 'Oppo', 12000, 'P1oppo.jpg', 'Oppo Mobile', 5),
(2, 'Mobile', 'Vivo Z5x', 15000, 'P2vivo-z5x.jpg', 'Vivo Z5x mobile', 5),
(3, 'Mobile', 'Asus Zenfone Max M2', 8000, 'P3asus.jpg', 'Asus Zenfone Max M2 Mobile', 4),
(4, 'Mobile', 'Sony Xperia1', 79000, 'P4sony-xperia.jpg', 'Sony Xperia1 mobile', 4),
(5, 'Mobile', 'Samsung Galaxy J8', 15500, 'P5samsung1.jpg', 'Samsung Galaxy J8 mobile', 3),
(6, 'Laptop', 'Dell', 20000, 'P6dell.jpg', 'Dell Laptop', 1),
(7, 'Laptop', 'Acer', 18000, 'P7acer.png', 'Acer Laptop', 3),
(8, 'Laptop', 'HP', 25000, 'P8hp.jpg', 'HP Laptop', 5),
(9, 'Men-TShirt', 'T-Shirt', 150, 'P9tshirt-img.png', 'Men T-Shirt', 3),
(10, 'Women-Cloth', 'Women Cloth', 250, 'P10women-clothes-img.png', 'Women Cloth', 0),
(11, 'Men-Shirt', 'Shirt', 500, 'P11dress-shirt-img.png', 'Men Shirt', 0);

-- --------------------------------------------------------

--
-- Table structure for table `cs_purchase`
--

CREATE TABLE `cs_purchase` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `rdate` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_purchase`
--

INSERT INTO `cs_purchase` (`id`, `uname`, `amount`, `rdate`) VALUES
(1, 'suresh', 27500, '20-01-2022'),
(2, 'suresh', 27000, '21-01-2022'),
(3, 'suresh', 25000, '21-01-2022');

-- --------------------------------------------------------

--
-- Table structure for table `cs_register`
--

CREATE TABLE `cs_register` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_register`
--

INSERT INTO `cs_register` (`id`, `name`, `mobile`, `email`, `uname`, `pass`, `gender`) VALUES
(1, 'Suresh', 8856733472, 'rndittrichy@gmail.com', 'suresh', '1234', 'Male'),
(2, 'Ravi', 9988776655, 'ravi@gmail.com', 'ravi', '1234', ''),
(3, 'Rahul', 9034566264, 'aaa@gmail.com', 'aaa', 'aaa', ''),
(4, 'aaa', 994455622, 'aa@gmail.com', '', 'aaa', ''),
(5, 'aaa', 9912366789, 'aaa@gmail.com', 'bbb', 'bbb', ''),
(6, 'Ram', 9976834521, 'ram@gmail.com', 'ram', '1234', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `cs_review`
--

CREATE TABLE `cs_review` (
  `id` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `review` varchar(100) NOT NULL,
  `star` int(11) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `review_code` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_review`
--

INSERT INTO `cs_review` (`id`, `pid`, `uname`, `review`, `star`, `rdate`, `status`, `review_code`) VALUES
(1, 1, 'suresh', 'useful product', 5, '21-01-2022', 1, '53157'),
(2, 6, 'suresh', 'working easy', 4, '21-01-2022', 0, '76708'),
(3, 8, 'suresh', 'Super Laptop', 5, '21-01-2022', 1, '18201');

-- --------------------------------------------------------

--
-- Table structure for table `cs_search`
--

CREATE TABLE `cs_search` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `keyword` varchar(50) NOT NULL,
  `scount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs_search`
--

INSERT INTO `cs_search` (`id`, `uname`, `keyword`, `scount`) VALUES
(1, 'suresh', 'mobile', 1),
(2, 'suresh', 'oppo', 2);
