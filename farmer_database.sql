-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 24, 2024 at 12:24 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `farmer_database`
--
CREATE DATABASE IF NOT EXISTS `farmer_database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `farmer_database`;

-- --------------------------------------------------------

--
-- Table structure for table `appointment_details`
--

DROP TABLE IF EXISTS `appointment_details`;
CREATE TABLE IF NOT EXISTS `appointment_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `address` longtext NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `appointment_date` date NOT NULL,
  `query_subject` varchar(20) NOT NULL,
  `additional_info` longtext NOT NULL,
  `user_id` int NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Appointment_details_user_id_51d3f568` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `appointment_details`
--

INSERT INTO `appointment_details` (`id`, `name`, `age`, `address`, `contact_number`, `appointment_date`, `query_subject`, `additional_info`, `user_id`, `status`) VALUES
(15, 'user', 21, 'lb nagar', '9855343', '2024-01-29', 'Fertilization', 'ok', 12, 'Cancelled'),
(13, 'user4', 21, 'hayathanagat', '8787878787', '2024-05-31', 'Disease', 'need an appoint,ent', 11, 'Cancelled'),
(11, 'user', 21, 'hayathnagar', '0909909098', '2024-01-22', 'Fertilization', 'need an aapointment', 9, 'Accepted'),
(12, 'user', 21, 'hayathnagar', '878787878', '2024-01-24', 'Fertilization', 'need an appointment ', 10, 'Cancelled');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add farmer query', 8, 'add_farmerquery'),
(30, 'Can change farmer query', 8, 'change_farmerquery'),
(31, 'Can delete farmer query', 8, 'delete_farmerquery'),
(32, 'Can view farmer query', 8, 'view_farmerquery'),
(33, 'Can add feedback', 9, 'add_feedback'),
(34, 'Can change feedback', 9, 'change_feedback'),
(35, 'Can delete feedback', 9, 'delete_feedback'),
(36, 'Can view feedback', 9, 'view_feedback'),
(37, 'Can add response', 10, 'add_response'),
(38, 'Can change response', 10, 'change_response'),
(39, 'Can delete response', 10, 'delete_response'),
(40, 'Can view response', 10, 'view_response'),
(41, 'Can add appointment', 11, 'add_appointment'),
(42, 'Can change appointment', 11, 'change_appointment'),
(43, 'Can delete appointment', 11, 'delete_appointment'),
(44, 'Can view appointment', 11, 'view_appointment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'farmerapp', 'user'),
(8, 'farmerapp', 'farmerquery'),
(9, 'farmerapp', 'feedback'),
(10, 'expertapp', 'response'),
(11, 'farmerapp', 'appointment');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-01-13 11:39:17.305611'),
(2, 'auth', '0001_initial', '2024-01-13 11:39:17.806303'),
(3, 'admin', '0001_initial', '2024-01-13 11:39:17.992755'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-01-13 11:39:17.998798'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-01-13 11:39:18.004349'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-01-13 11:39:18.078487'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-01-13 11:39:18.117049'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-01-13 11:39:18.154054'),
(9, 'auth', '0004_alter_user_username_opts', '2024-01-13 11:39:18.164298'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-01-13 11:39:18.196505'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-01-13 11:39:18.197515'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-01-13 11:39:18.203854'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-01-13 11:39:18.237494'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-01-13 11:39:18.271119'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-01-13 11:39:18.304948'),
(16, 'auth', '0011_update_proxy_permissions', '2024-01-13 11:39:18.311106'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-01-13 11:39:18.343761'),
(18, 'sessions', '0001_initial', '2024-01-13 11:39:18.381529'),
(19, 'farmerapp', '0001_initial', '2024-01-13 11:41:29.045391'),
(20, 'farmerapp', '0002_farmerquery', '2024-01-15 13:08:15.725189'),
(21, 'farmerapp', '0003_farmerquery_latitude_farmerquery_longitude_and_more', '2024-01-15 17:23:14.940033'),
(22, 'farmerapp', '0004_feedback', '2024-01-15 17:53:02.955791'),
(23, 'expertapp', '0001_initial', '2024-01-17 11:49:26.515933'),
(24, 'farmerapp', '0005_appointment', '2024-01-18 15:26:22.288039'),
(25, 'farmerapp', '0006_appointment_status', '2024-01-18 15:35:45.405364');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('kohpt2z0s3maj91fkln67xv4rg0gf2ki', 'eyJxdWVyeSI6NjgsInVzZXJfaWQiOjd9:1rRok9:VGCllpDhNoCsdsqD0uBfiNcgoCualBSIH1jfM7d2B5U', '2024-02-05 07:29:17.836206'),
('n534btc2xq3r5bdspumyf6ubjarjep8j', 'eyJxdWVyeSI6NzB9:1rRtRy:AV7rS8z0qiNixow3Unr3uf7Njw_j66jWhvsQ6SJSQiw', '2024-02-05 12:30:50.395795'),
('216v0j9on7kywfn2t234g2eday0kpc9v', 'eyJxdWVyeSI6NzB9:1rRtgz:3DnVcyQ8jBRuCe8t3TEusWUtXCOcs-pkoHC24AwBi1g', '2024-02-05 12:46:21.323316'),
('oppd1g1ighbchdc4c3gywtpgyl7w3p5m', 'eyJxdWVyeSI6NjZ9:1rSGic:xD-1s8HWBDfKcGHra4NHPzSY5qRatdQSO0sMX0_FcEw', '2024-02-06 13:21:34.889218'),
('et2ll8p54x3jy0yvo8b3xgq05lxnjqe2', 'eyJxdWVyeSI6NzF9:1rScHK:em9VEe1bW45P6myE6vWi6jr5mH2XOmvLrtvap5bbbME', '2024-02-07 12:22:50.560023');

-- --------------------------------------------------------

--
-- Table structure for table `farmer_query`
--

DROP TABLE IF EXISTS `farmer_query`;
CREATE TABLE IF NOT EXISTS `farmer_query` (
  `query_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact_number` varchar(50) NOT NULL,
  `query_type` varchar(20) NOT NULL,
  `crop_information` longtext NOT NULL,
  `query_subject` varchar(20) NOT NULL,
  `specific_issue` longtext NOT NULL,
  `location` varchar(100) NOT NULL,
  `country` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pin_code` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `weather_condition` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`query_id`),
  KEY `Farmer_Query_user_id_9dae2f9e` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `farmer_query`
--

INSERT INTO `farmer_query` (`query_id`, `name`, `email`, `contact_number`, `query_type`, `crop_information`, `query_subject`, `specific_issue`, `location`, `country`, `state`, `city`, `pin_code`, `created_at`, `user_id`, `latitude`, `longitude`, `weather_condition`) VALUES
(66, 'user', 'user3@gmail.com', '878787878', 'Technical', 'cotton', 'Fertilization', 'this is just the random data to send to the agriexpert !\r\n', 'hayathanagar', 'India', 'Telangana', 'Hyderabad', '500036', '2024-01-21 14:02:51.712951', 10, 17.3801472, 78.4990208, ''),
(67, 'user4', 'user4@gmail.com', '8787878', 'Technical', 'cotton', 'Fertilization', 'this is exapmle question !', 'hayathnagar', 'India', 'Telangana', 'Hayathnagar_Khalsa', '501505', '2024-01-21 14:16:50.108023', 11, 17.3170234, 78.5983048, ''),
(71, 'newuser', 'new@gmail.com', '986575356', 'Technical', 'potato', 'Other', 'plant is drying ', 'lb nagar', 'India', 'Telangana', 'Hyderabad', '500074', '2024-01-24 11:49:12.478379', 12, 17.3522021, 78.5493461, 'Haze');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_details`
--

DROP TABLE IF EXISTS `feedback_details`;
CREATE TABLE IF NOT EXISTS `feedback_details` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `rating` int NOT NULL,
  `additional_comments` longtext NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `Feedback_details_user_id_1d6e94ec` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `feedback_details`
--

INSERT INTO `feedback_details` (`feedback_id`, `user_name`, `user_email`, `rating`, `additional_comments`, `user_id`) VALUES
(12, 'user', 'new@gmail.com', 4, 'good ', 12),
(8, 'user', 'newuser2@gmail.com', 2, 'need to improve', 9),
(9, 'user', 'newuser3@gmail.com', 3, '', 10),
(10, 'user', 'newuser3@gmail.com', 1, 'need improvement ', 10),
(11, 'user4', 'user4@gmail.com', 1, 'need to improve ', 11);

-- --------------------------------------------------------

--
-- Table structure for table `respones_expert`
--

DROP TABLE IF EXISTS `respones_expert`;
CREATE TABLE IF NOT EXISTS `respones_expert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `query_id` int NOT NULL,
  `response_text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `respones_expert`
--

INSERT INTO `respones_expert` (`id`, `name`, `email`, `query_id`, `response_text`) VALUES
(31, 'upender', 'upenderimp25@gmail.com', 62, 'updated Seeking your expertise to address a challenging situation regarding crop diseases. Your insights and guidance are invaluable in navigating through this issue and implementing effective solutions. Looking forward to your expert advice on managing and mitigating the impact of crop diseases. Your assistance is greatly appreciated.\r\n\r\n'),
(30, 'upender', 'upenderimp25@gmail.com', 63, 'हाँ, हम सतत कृषि प्रथाओं पर मार्गदर्शन प्रदान करने में विशेषज्ञ हैं। हमारे कृषि विशेषज्ञ आपको पर्यावरण-मैत्री पैदायिक खेती विधियों, मिट्टी संरक्षण, जल प्रबंधन, और अधिक की दृष्टि प्रदान कर सकते हैं। कृपया हमारी संसाधनों का अन्वेषण करें और व्यक्तिगत सलाह के लिए संपर्क करें।'),
(29, 'upender', 'upenderimp25@gmail.com', 62, 'hi upender, Thank you for reaching out and providing details about the challenges you\'re facing with crop diseases. I appreciate your proactive approach in seeking assistance. I\'m committed to providing you with tailored advice and effective solutions to manage and mitigate the impact of these diseases on your crops. Let\'s work together to find the best strategies for a healthier and more resilient crop yield. Your dedication to addressing these issues is commendable, and I look forward to assisting you further'),
(32, 'user', 'user3@gmail.com', 66, 'hello user3 this is response to your question we can update the responses\r\n'),
(33, 'user4', 'user4@gmail.com', 67, 'response text edited\r\n'),
(34, 'newuser', 'new@gmail.com', 71, 'this is response text  to you updated\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_phone` varchar(50) NOT NULL,
  `user_location` varchar(50) NOT NULL,
  `user_profile` varchar(100) NOT NULL,
  `status` varchar(15) NOT NULL,
  `otp` varchar(6) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `user_email`, `user_password`, `user_phone`, `user_location`, `user_profile`, `status`, `otp`) VALUES
(12, 'newuser', 'new@gmail.com', '1', '66', 'lb nagar', 'images/user/Tomato___Leaf_Mold_4.JPG', 'Accepted', '0'),
(11, 'newuser4', 'user4@gmail.com', '0', '87878787', 'hayathnagar', 'images/user/Tomato___Target_Spot_5.JPG', 'Accepted', '0'),
(9, 'newuser', 'newuser2@gmail.com', '1', '8787675754', 'hayathanagar', 'images/user/tem1.png', 'Accepted', '0'),
(10, 'user', 'newuser3@gmail.com', '1', '878787878', 'hayathnagar', 'images/user/Tomato___Early_blight_3.JPG', 'Accepted', '0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
