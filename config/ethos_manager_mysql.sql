-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2018 at 10:45 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ethos_manager`
--
CREATE DATABASE IF NOT EXISTS `ethos_manager` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
USE `ethos_manager`;

-- --------------------------------------------------------

--
-- Table structure for table `algo`
--

CREATE TABLE `algo` (
  `algo_id` bigint(20) UNSIGNED NOT NULL,
  `algo_name` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `algo`:
--

-- --------------------------------------------------------

--
-- Table structure for table `coin`
--

CREATE TABLE `coin` (
  `coin_id` bigint(20) UNSIGNED NOT NULL,
  `coin_name` varchar(120) NOT NULL,
  `coin_short` varchar(10) NOT NULL,
  `algo_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `coin`:
--   `algo_id`
--       `algo` -> `algo_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `coin_wallet`
--

CREATE TABLE `coin_wallet` (
  `coin_wallet_id` bigint(20) UNSIGNED NOT NULL,
  `coin_id` bigint(20) UNSIGNED NOT NULL,
  `coin_wallet_name` varchar(120) NOT NULL,
  `coin_wallet_value` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `coin_wallet`:
--   `coin_id`
--       `coin` -> `coin_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `ethos_mac`
--

CREATE TABLE `ethos_mac` (
  `ethos_mac_id` bigint(20) UNSIGNED NOT NULL,
  `ethos_mac_value` char(6) NOT NULL,
  `mining_rig_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `ethos_mac`:
--   `mining_rig_id`
--       `mining_rig` -> `mining_rig_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `ethos_ver`
--

CREATE TABLE `ethos_ver` (
  `ethos_ver_id` bigint(20) UNSIGNED NOT NULL,
  `ethos_ver_name` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `ethos_ver`:
--

-- --------------------------------------------------------

--
-- Table structure for table `global_site_value`
--

CREATE TABLE `global_site_value` (
  `global_site_value_id` int(10) UNSIGNED NOT NULL,
  `mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `value_name` varchar(120) NOT NULL,
  `value_value` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `global_site_value`:
--   `mining_site_id`
--       `mining_site` -> `mining_site_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `hardware`
--

CREATE TABLE `hardware` (
  `hardware_id` bigint(20) UNSIGNED NOT NULL,
  `hardware_name` varchar(120) NOT NULL,
  `hardware_type_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `hardware`:
--   `hardware_type_id`
--       `hardware_type` -> `hardware_type_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `hardware_hashrate`
--

CREATE TABLE `hardware_hashrate` (
  `hardware_hashrate_id` bigint(20) UNSIGNED NOT NULL,
  `mining_rig_id` bigint(20) UNSIGNED NOT NULL,
  `hardware_id` bigint(20) UNSIGNED NOT NULL,
  `algo_id` bigint(20) UNSIGNED NOT NULL,
  `hashrate_value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `hardware_hashrate`:
--   `algo_id`
--       `algo` -> `algo_id`
--   `hardware_id`
--       `hardware` -> `hardware_id`
--   `mining_rig_id`
--       `mining_rig` -> `mining_rig_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `hardware_type`
--

CREATE TABLE `hardware_type` (
  `hardware_type_id` bigint(20) UNSIGNED NOT NULL,
  `hardware_type_name` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `hardware_type`:
--

-- --------------------------------------------------------

--
-- Table structure for table `matix_algo-mining_software`
--

CREATE TABLE `matix_algo-mining_software` (
  `matrix_algo-mining_software_id` bigint(20) UNSIGNED NOT NULL,
  `algo_id` bigint(20) UNSIGNED NOT NULL,
  `mining_software_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `matix_algo-mining_software`:
--   `algo_id`
--       `algo` -> `algo_id`
--   `mining_software_id`
--       `mining_software` -> `mining_software_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `matix_ethos_ver-miner`
--

CREATE TABLE `matix_ethos_ver-miner` (
  `matrix_id` bigint(20) UNSIGNED NOT NULL,
  `matix_name` varchar(250) NOT NULL,
  `ethos_ver_id` bigint(20) UNSIGNED NOT NULL,
  `miner_id` bigint(20) UNSIGNED NOT NULL,
  `mining_software_value` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `matix_ethos_ver-miner`:
--   `ethos_ver_id`
--       `ethos_ver` -> `ethos_ver_id`
--   `miner_id`
--       `mining_software` -> `mining_software_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `matix_hardware-mining_rig`
--

CREATE TABLE `matix_hardware-mining_rig` (
  `matix_hardware-mining_rig_id` bigint(20) UNSIGNED NOT NULL,
  `matrix_hardware-mining_rig_name` varchar(120) NOT NULL,
  `hardware_id` bigint(20) UNSIGNED NOT NULL,
  `minging_rig_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `matix_hardware-mining_rig`:
--   `hardware_id`
--       `hardware` -> `hardware_id`
--   `minging_rig_id`
--       `mining_rig` -> `mining_rig_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `matrix_pool_mining_site-pool_mining_site`
--

CREATE TABLE `matrix_pool_mining_site-pool_mining_site` (
  `matrix_pool_mining_site-pool_mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `pool_mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `mining_site_cred_id` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `matrix_pool_mining_site-pool_mining_site`:
--   `mining_site_cred_id`
--       `mining_site_cred` -> `minng_site_cred_id`
--   `pool_mining_site_id`
--       `pool_mining_site` -> `pool_mining_site_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_rig`
--

CREATE TABLE `mining_rig` (
  `mining_rig_id` bigint(20) UNSIGNED NOT NULL,
  `mining_rig_name` varchar(120) NOT NULL,
  `reboot_value` int(11) NOT NULL,
  `ethos_ver` bigint(20) UNSIGNED NOT NULL,
  `mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `mining_rig_config_url` varchar(250) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `mining_rig`:
--   `ethos_ver`
--       `ethos_ver` -> `ethos_ver_id`
--   `mining_site_id`
--       `mining_site` -> `mining_site_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_site`
--

-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2018 at 04:01 AM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ethos_manager`
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_site`
--

CREATE TABLE `mining_site` (
  `mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `mining_site_name` varchar(120) NOT NULL,
  `custom_panel_name` char(6) NOT NULL,
  `custom_panel_pass` char(6) NOT NULL,
  `max_gpu_temp` int(11) NOT NULL,
  `global_fan` int(11) NOT NULL,
  `autoreboot` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mining_site`
--
ALTER TABLE `mining_site`
  ADD PRIMARY KEY (`mining_site_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mining_site`
--
ALTER TABLE `mining_site`
  MODIFY `mining_site_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


--
-- RELATIONSHIPS FOR TABLE `mining_site`:
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_site_cred`
--

CREATE TABLE `mining_site_cred` (
  `minng_site_cred_id` bigint(20) UNSIGNED NOT NULL,
  `pool_website_id` bigint(20) UNSIGNED NOT NULL,
  `cred_name` varchar(120) NOT NULL,
  `mining_site_username` varchar(120) NOT NULL,
  `mining_site_pass` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `mining_site_cred`:
--   `pool_website_id`
--       `pool_website` -> `pool_website_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_site_payout_history`
--

CREATE TABLE `mining_site_payout_history` (
  `mining_site_payout_historty_id` bigint(20) UNSIGNED NOT NULL,
  `pool_api_request_id` bigint(20) UNSIGNED NOT NULL,
  `algo_id` bigint(20) UNSIGNED NOT NULL,
  `pool_mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `pool_fee` double(5,2) NOT NULL,
  `current` double(15,9) NOT NULL,
  `est_last24h` double(15,9) NOT NULL,
  `act_last24h` double(15,9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `mining_site_payout_history`:
--   `algo_id`
--       `algo` -> `algo_id`
--   `pool_api_request_id`
--       `pool_api_request` -> `pool_api_request_id`
--   `pool_mining_site_id`
--       `pool_mining_site` -> `pool_mining_site_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `mining_software`
--

CREATE TABLE `mining_software` (
  `mining_software_id` bigint(20) UNSIGNED NOT NULL,
  `ethos_ver_id` bigint(20) UNSIGNED NOT NULL,
  `ethos_miner_name` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `mining_software`:
--   `ethos_ver_id`
--       `ethos_ver` -> `ethos_ver_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `pool_api_request`
--

CREATE TABLE `pool_api_request` (
  `pool_api_request_id` bigint(20) UNSIGNED NOT NULL,
  `pool_website_id` bigint(20) UNSIGNED NOT NULL,
  `pool_api_timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `pool_api_request`:
--

-- --------------------------------------------------------

--
-- Table structure for table `pool_mining_site`
--

CREATE TABLE `pool_mining_site` (
  `pool_mining_site_id` bigint(20) UNSIGNED NOT NULL,
  `pool_website_id` bigint(20) UNSIGNED NOT NULL,
  `pool_mining_algo_id` bigint(20) UNSIGNED NOT NULL,
  `pool_mining_url` varchar(250) NOT NULL,
  `pool_mining_port` int(11) NOT NULL,
  `pool_api_suffix` varchar(250) NOT NULL,
  `pool_value_mult` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `pool_mining_site`:
--   `pool_mining_algo_id`
--       `algo` -> `algo_id`
--   `pool_website_id`
--       `pool_website` -> `pool_website_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `pool_website`
--

CREATE TABLE `pool_website` (
  `pool_website_id` bigint(20) UNSIGNED NOT NULL,
  `pool_name` varchar(120) NOT NULL,
  `pool_url` varchar(250) NOT NULL,
  `pool_api_url` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `pool_website`:
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `algo`
--
ALTER TABLE `algo`
  ADD PRIMARY KEY (`algo_id`);

--
-- Indexes for table `coin`
--
ALTER TABLE `coin`
  ADD PRIMARY KEY (`coin_id`);

--
-- Indexes for table `coin_wallet`
--
ALTER TABLE `coin_wallet`
  ADD PRIMARY KEY (`coin_wallet_id`);

--
-- Indexes for table `ethos_mac`
--
ALTER TABLE `ethos_mac`
  ADD PRIMARY KEY (`ethos_mac_id`);

--
-- Indexes for table `ethos_ver`
--
ALTER TABLE `ethos_ver`
  ADD PRIMARY KEY (`ethos_ver_id`);

--
-- Indexes for table `global_site_value`
--
ALTER TABLE `global_site_value`
  ADD PRIMARY KEY (`global_site_value_id`);

--
-- Indexes for table `hardware`
--
ALTER TABLE `hardware`
  ADD PRIMARY KEY (`hardware_id`);

--
-- Indexes for table `hardware_hashrate`
--
ALTER TABLE `hardware_hashrate`
  ADD PRIMARY KEY (`hardware_hashrate_id`);

--
-- Indexes for table `hardware_type`
--
ALTER TABLE `hardware_type`
  ADD PRIMARY KEY (`hardware_type_id`);

--
-- Indexes for table `matix_algo-mining_software`
--
ALTER TABLE `matix_algo-mining_software`
  ADD PRIMARY KEY (`matrix_algo-mining_software_id`);

--
-- Indexes for table `matix_ethos_ver-miner`
--
ALTER TABLE `matix_ethos_ver-miner`
  ADD PRIMARY KEY (`matrix_id`);

--
-- Indexes for table `matix_hardware-mining_rig`
--
ALTER TABLE `matix_hardware-mining_rig`
  ADD PRIMARY KEY (`matix_hardware-mining_rig_id`);

--
-- Indexes for table `matrix_pool_mining_site-pool_mining_site`
--
ALTER TABLE `matrix_pool_mining_site-pool_mining_site`
  ADD PRIMARY KEY (`matrix_pool_mining_site-pool_mining_site_id`);

--
-- Indexes for table `mining_rig`
--
ALTER TABLE `mining_rig`
  ADD PRIMARY KEY (`mining_rig_id`);

--
-- Indexes for table `mining_site`
--
ALTER TABLE `mining_site`
  ADD PRIMARY KEY (`mining_site_id`);

--
-- Indexes for table `mining_site_cred`
--
ALTER TABLE `mining_site_cred`
  ADD PRIMARY KEY (`minng_site_cred_id`);

--
-- Indexes for table `mining_site_payout_history`
--
ALTER TABLE `mining_site_payout_history`
  ADD PRIMARY KEY (`mining_site_payout_historty_id`);

--
-- Indexes for table `mining_software`
--
ALTER TABLE `mining_software`
  ADD PRIMARY KEY (`mining_software_id`);

--
-- Indexes for table `pool_api_request`
--
ALTER TABLE `pool_api_request`
  ADD PRIMARY KEY (`pool_api_request_id`);

--
-- Indexes for table `pool_mining_site`
--
ALTER TABLE `pool_mining_site`
  ADD PRIMARY KEY (`pool_mining_site_id`);

--
-- Indexes for table `pool_website`
--
ALTER TABLE `pool_website`
  ADD PRIMARY KEY (`pool_website_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `algo`
--
ALTER TABLE `algo`
  MODIFY `algo_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `coin`
--
ALTER TABLE `coin`
  MODIFY `coin_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `coin_wallet`
--
ALTER TABLE `coin_wallet`
  MODIFY `coin_wallet_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `ethos_mac`
--
ALTER TABLE `ethos_mac`
  MODIFY `ethos_mac_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `ethos_ver`
--
ALTER TABLE `ethos_ver`
  MODIFY `ethos_ver_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `global_site_value`
--
ALTER TABLE `global_site_value`
  MODIFY `global_site_value_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hardware`
--
ALTER TABLE `hardware`
  MODIFY `hardware_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hardware_hashrate`
--
ALTER TABLE `hardware_hashrate`
  MODIFY `hardware_hashrate_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `hardware_type`
--
ALTER TABLE `hardware_type`
  MODIFY `hardware_type_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `matix_algo-mining_software`
--
ALTER TABLE `matix_algo-mining_software`
  MODIFY `matrix_algo-mining_software_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `matix_ethos_ver-miner`
--
ALTER TABLE `matix_ethos_ver-miner`
  MODIFY `matrix_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `matix_hardware-mining_rig`
--
ALTER TABLE `matix_hardware-mining_rig`
  MODIFY `matix_hardware-mining_rig_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `matrix_pool_mining_site-pool_mining_site`
--
ALTER TABLE `matrix_pool_mining_site-pool_mining_site`
  MODIFY `matrix_pool_mining_site-pool_mining_site_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mining_rig`
--
ALTER TABLE `mining_rig`
  MODIFY `mining_rig_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mining_site`
--
ALTER TABLE `mining_site`
  MODIFY `mining_site_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mining_site_cred`
--
ALTER TABLE `mining_site_cred`
  MODIFY `minng_site_cred_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mining_site_payout_history`
--
ALTER TABLE `mining_site_payout_history`
  MODIFY `mining_site_payout_historty_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mining_software`
--
ALTER TABLE `mining_software`
  MODIFY `mining_software_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pool_api_request`
--
ALTER TABLE `pool_api_request`
  MODIFY `pool_api_request_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pool_mining_site`
--
ALTER TABLE `pool_mining_site`
  MODIFY `pool_mining_site_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pool_website`
--
ALTER TABLE `pool_website`
  MODIFY `pool_website_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
