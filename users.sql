-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2020 at 11:39 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.3.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `senderMail` varchar(50) NOT NULL,
  `receiverMail` varchar(50) NOT NULL,
  `message` varchar(2000) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`senderMail`, `receiverMail`, `message`, `time`) VALUES
('ABC@QWE.A', 'abc@qwe.a', 'HELLO', '2020-01-19 08:07:58'),
('ABC@QWE.A', 'abc@qwe.a', 'Hello', '2020-01-19 08:08:09'),
('abc@qwe.a', 'mm@m.com', 'Hello', '2020-01-19 08:11:06'),
('abc@qwe.a', 'mm@m.com', 'mhghj', '2020-01-19 09:15:39'),
('abc@qwe.a', 'as', 'hih', '2020-01-19 09:41:18'),
('abc@qwe.a', 'xlkc@SC', '123', '2020-01-19 09:53:38'),
('abc@qwe.a', 'xlkc@SC', '111', '2020-01-19 09:54:02'),
('abc@qwe.a', 'xlkc@SC', 'hey', '2020-01-19 10:05:55'),
('abc@qwe.a', 'xlkc@SC', '123', '2020-01-19 10:06:06'),
('abc@qwe.a', 'mm@m.com', 'hh', '2020-01-19 10:24:50'),
('abc@qwe.a', 'mm@m.com', 'hello', '2020-01-19 10:30:23'),
('abc@qwe.a', 'mm@m.com', 'test', '2020-01-19 10:30:50'),
('abc@qwe.a', 'as', 'abc', '2020-01-19 10:31:09'),
('abc@qwe.a', 'xlkc@SC', 'aaa', '2020-01-19 10:31:15'),
('abc@qwe.a', 'xlkc@SC', 'hey', '2020-01-19 10:33:09'),
('abc@qwe.a', 'xlkc@SC', 'hello', '2020-01-19 10:33:12'),
('abc@qwe.a', 'xlkc@SC', 'scnsc', '2020-01-19 10:33:13'),
('abc@qwe.a', 'xlkc@SC', 'sadxasdsaxds', '2020-01-19 10:33:13'),
('abc@qwe.a', 'xlkc@SC', 'xsn', '2020-01-19 10:33:14'),
('abc@qwe.a', 'xlkc@SC', 'sj', '2020-01-19 10:33:14'),
('abc@qwe.a', 'xlkc@SC', 'sjd', '2020-01-19 10:33:14'),
('abc@qwe.a', 'xlkc@SC', 'sadj', '2020-01-19 10:33:14'),
('abc@qwe.a', 'xlkc@SC', 'sad', '2020-01-19 10:33:14'),
('abc@qwe.a', 'xlkc@SC', 'vfvfdv', '2020-01-19 10:33:26'),
('abc@qwe.a', 'xlkc@SC', 'vfvf', '2020-01-19 10:33:27'),
('abc@qwe.a', 'xlkc@SC', 'fvfd', '2020-01-19 10:33:28'),
('abc@qwe.a', 'xlkc@SC', 'dslfds', '2020-01-19 10:34:45'),
('abc@qwe.a', 'xlkc@SC', 'dfsd', '2020-01-19 10:34:46'),
('abc@qwe.a', 'xlkc@SC', 'dfs', '2020-01-19 10:34:47'),
('abc@qwe.a', 'xlkc@SC', 'djfn', '2020-01-19 10:36:59'),
('abc@qwe.a', 'xlkc@SC', 'fdsf', '2020-01-19 10:37:00'),
('abc@qwe.a', 'xlkc@SC', 'fdsf', '2020-01-19 10:37:00'),
('abc@qwe.a', 'xlkc@SC', 'sdfdsf', '2020-01-19 10:37:01'),
('abc@qwe.a', 'xlkc@SC', 'sf', '2020-01-19 10:37:01'),
('abc@qwe.a', 'xlkc@SC', 'sdf', '2020-01-19 10:37:02'),
('abc@qwe.a', 'xlkc@SC', 'sv', '2020-01-19 10:37:02'),
('abc@qwe.a', 'xlkc@SC', 'fdf', '2020-01-19 10:37:03'),
('abc@qwe.a', 'xlkc@SC', 'fg', '2020-01-19 10:37:11'),
('abc@qwe.a', 'xlkc@SC', 'ghgjhgjhgjhgj', '2020-01-19 10:37:14'),
('abc@qwe.a', 'xlkc@SC', 'fgfg', '2020-01-19 10:37:18'),
('xlkc@SC', 'abc@qwe.a', 'Hi', '2020-01-19 10:38:27'),
('xlkc@SC', 'abc@qwe.a', 'Ddjd', '2020-01-19 10:38:32'),
('sunny@gmail.com', 'xlkc@SC', 'Hey', '2020-01-19 10:38:33');

-- --------------------------------------------------------

--
-- Table structure for table `userinfo`
--

CREATE TABLE `userinfo` (
  `username` varchar(32) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userinfo`
--

INSERT INTO `userinfo` (`username`, `password`, `email`) VALUES
('Abc', 'Aa@123', 'abc@qwe.a'),
('aaa', 'sd', 'as'),
('mmm', 'Aa1@111', 'mm@m.com'),
('Sunny', 'Sunny@123', 'sunny@gmail.com'),
('test', 'aA@1234567', 'test@gmail.com'),
('Anc', 'abc@ABC1', 'xlkc@SC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `userinfo`
--
ALTER TABLE `userinfo`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
