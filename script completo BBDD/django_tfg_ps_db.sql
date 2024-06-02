-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 02-06-2024 a las 18:09:32
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `django_tfg_ps_db`
--
CREATE DATABASE IF NOT EXISTS `django_tfg_ps_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `django_tfg_ps_db`;
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
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
-- Estructura de tabla para la tabla `auth_group_permissions`
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
-- Estructura de tabla para la tabla `auth_permission`
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
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(25, 'Can add auth permission', 7, 'add_authpermission'),
(26, 'Can change auth permission', 7, 'change_authpermission'),
(27, 'Can delete auth permission', 7, 'delete_authpermission'),
(28, 'Can view auth permission', 7, 'view_authpermission'),
(29, 'Can add auth user', 8, 'add_authuser'),
(30, 'Can change auth user', 8, 'change_authuser'),
(31, 'Can delete auth user', 8, 'delete_authuser'),
(32, 'Can view auth user', 8, 'view_authuser'),
(33, 'Can add auth user user permissions', 9, 'add_authuseruserpermissions'),
(34, 'Can change auth user user permissions', 9, 'change_authuseruserpermissions'),
(35, 'Can delete auth user user permissions', 9, 'delete_authuseruserpermissions'),
(36, 'Can view auth user user permissions', 9, 'view_authuseruserpermissions'),
(37, 'Can add django session', 10, 'add_djangosession'),
(38, 'Can change django session', 10, 'change_djangosession'),
(39, 'Can delete django session', 10, 'delete_djangosession'),
(40, 'Can view django session', 10, 'view_djangosession'),
(41, 'Can add inventario', 11, 'add_inventario'),
(42, 'Can change inventario', 11, 'change_inventario'),
(43, 'Can delete inventario', 11, 'delete_inventario'),
(44, 'Can view inventario', 11, 'view_inventario'),
(45, 'Can add jugadores', 12, 'add_jugadores'),
(46, 'Can change jugadores', 12, 'change_jugadores'),
(47, 'Can delete jugadores', 12, 'delete_jugadores'),
(48, 'Can view jugadores', 12, 'view_jugadores'),
(49, 'Can add objetos', 13, 'add_objetos'),
(50, 'Can change objetos', 13, 'change_objetos'),
(51, 'Can delete objetos', 13, 'delete_objetos'),
(52, 'Can view objetos', 13, 'view_objetos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
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
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$3Hj8anaqdugzAhZ5WFfXjH$SAXFBA8UJff3IIMC/IqEdAfEVP7I2eHK854y7Q/G+HE=', '2024-06-02 17:52:46.796412', 1, 'curro', '', '', '', 1, 1, '2024-04-23 17:34:30.059575'),
(2, 'pbkdf2_sha256$720000$ik1vnUd4WHCgdDVxw4PGoL$HCActxksXPcxoLWYlP1vQYVuNMzvHHh1+6jNcSdZf20=', '2024-06-02 17:42:00.997598', 0, 'raul', '', '', '', 0, 1, '2024-04-23 17:42:26.285962'),
(3, 'pbkdf2_sha256$720000$Fp4iA7FzvgKFZS25wPUhzi$MH8hAfV20IKOp0/comXVSy1PHf1uVt8yszrAZP1WNLA=', '2024-06-02 18:00:10.401626', 0, 'luca', '', '', '', 0, 1, '2024-04-23 18:25:47.142396'),
(4, 'pbkdf2_sha256$720000$W8ZyZ9KMTODfvYL9iyouaj$a6Hq7hL3fwkLOBCROcEa6nNC8B7Qx4lIevL1E8brUE0=', '2024-05-23 12:25:53.600065', 0, 'dani', '', '', '', 0, 1, '2024-04-23 19:33:07.697818'),
(8, 'pbkdf2_sha256$720000$19y85mRHr6CGXtaXUUm4BN$DqtqMtCKsZ0ktIb10Us/y0Eea9wfrHB4z3WHej92mXo=', '2024-05-20 16:43:44.180758', 0, 'maria', '', '', '', 0, 1, '2024-05-15 18:02:22.376613'),
(9, 'pbkdf2_sha256$720000$tDB8MG6YC1YsFnFAAUw6Y6$y2JIhpuQw4YIGtjorkzmirGHxUXexEAYQ5mzRfI/KLg=', '2024-05-20 09:57:47.198759', 0, 'carla', '', '', '', 0, 1, '2024-05-16 08:30:39.880662'),
(10, 'pbkdf2_sha256$720000$K4bDFqxt7R8z1ZZZFteP73$S+IbF1CQ8VQMsOMdzcJz6B8uxiJE/Zg1Kp8lLGPKq18=', '2024-05-19 10:15:56.300929', 0, 'javi', '', '', '', 0, 1, '2024-05-19 10:15:55.757371'),
(11, 'pbkdf2_sha256$720000$UzLOrmTHys883A04BbVUVD$ETRMmW4FzIohu95HA6NLYvJbOzhWWOTVGrjRI0Ye3fI=', '2024-05-20 19:44:03.840425', 0, 'demon', '', '', '', 0, 1, '2024-05-20 19:44:03.301063'),
(12, 'pbkdf2_sha256$720000$VZOR7Bl6ZN2UGf1W4C3uGe$za3RdviDpquvFAAQyaC/Cv9ylsLD2h5imxZzGv+1z5U=', '2024-05-20 19:45:56.429621', 0, 'demon2', '', '', '', 0, 1, '2024-05-20 19:45:55.883823'),
(13, 'pbkdf2_sha256$720000$jprNUwZ66MDgDdYlzDhbtz$9eSdDsRZfDfrGGpHCDnSaXrk13s8trifwqS91RoXLWs=', '2024-05-20 19:56:19.191464', 0, 'vichi', '', '', '', 0, 1, '2024-05-20 19:56:18.655135'),
(14, 'pbkdf2_sha256$720000$PzQlfywg4VBWQcpQ1WOrsT$Drt4msC7/Xj+O2pQHN76FoTfE9w7ZHiLO7Dv76N0Ckw=', '2024-05-20 20:00:21.531607', 0, 'lolo', '', '', '', 0, 1, '2024-05-20 20:00:20.990674'),
(15, 'pbkdf2_sha256$720000$q9dOnyn7XBKydbJQJc7QpJ$tqkJLQD7kHWiSfqWmy8x8rYl5C5nsOuz9uOZZ3i1mus=', '2024-05-20 20:26:29.787563', 0, 'victor', '', '', '', 0, 1, '2024-05-20 20:25:08.705453'),
(16, 'pbkdf2_sha256$720000$2xiHP6YFuAbulO1YqDXgst$JAWqik5bsrLHk7Xvp6VEHsegevXWPxCiCGf9NEj4CDM=', '2024-05-22 11:16:19.755511', 0, 'kokoro', '', '', '', 0, 1, '2024-05-22 11:16:19.192127'),
(17, 'pbkdf2_sha256$720000$r9VWApvVCGBKYCPCnbHeAR$YskADiOrbaihryZ41BPIqrlMzeYmF99nv1w1w8CJxC0=', '2024-05-22 20:37:11.818674', 0, 'xavivi', '', '', '', 0, 1, '2024-05-22 20:34:45.176179'),
(18, 'pbkdf2_sha256$720000$ylXKrCF8JPJAHZzLoGvF72$i5G2b07YS3F4sxa71LVvP9y6JwjOybomGFzMjkkT+NQ=', '2024-05-22 21:26:24.248943', 0, 'paquito', '', '', '', 0, 1, '2024-05-22 21:26:23.715779'),
(19, 'pbkdf2_sha256$720000$P1i4M4wKp63x9jNpJWZv3x$0hrMwhxClI8kVzWq3GrFK+W/nHA4UJsBJ/pVmhiZqdM=', '2024-05-23 05:45:33.733817', 0, 'dani2', '', '', '', 0, 1, '2024-05-23 05:45:33.203909'),
(20, 'pbkdf2_sha256$720000$mONgbHfy5gArPndcapeOM7$ZYVcJwSpMBPpgiMD/nlTB2sqt0/InY73MrOJ65/wy8s=', '2024-05-23 06:48:14.731909', 0, 'koko', '', '', '', 0, 1, '2024-05-23 06:48:14.195546'),
(21, 'pbkdf2_sha256$720000$pS3pYuBhq4I4cf1i0m0dUB$hE5CfiN+1tVbcMCM4pZwEt43+DXYK1pg8TAlmrTxixU=', '2024-06-02 18:01:34.169275', 0, 'zana', '', '', '', 0, 1, '2024-05-24 14:35:04.606404'),
(22, 'pbkdf2_sha256$720000$Y379qg6qegrK1KvZuFaSTk$Ju589fJ3NGNH7CV6gLeMoLl3fzETfwGognmSowUiYr4=', '2024-06-02 17:47:56.477983', 0, 'marta', '', '', '', 0, 1, '2024-05-26 11:09:58.100322'),
(23, 'pbkdf2_sha256$720000$g4PBwBE5qb3G5fj3kqDTP9$1QeAauON4XK19xECvKqLaeZxdWF9hZ3IXzi7iISzvio=', '2024-05-27 15:29:40.793793', 0, 'john', '', '', '', 0, 1, '2024-05-27 15:29:40.252076'),
(24, 'pbkdf2_sha256$720000$u0un4gyOgn1RoRXMimjfwd$QgNjpWr9Z9Ea3eq9AO3Fwt0iLe9cdyeyUA2hKGJs0oc=', '2024-05-27 15:56:33.090612', 0, 'ayami', '', '', '', 0, 1, '2024-05-27 15:56:32.545431'),
(25, 'pbkdf2_sha256$720000$cTHhMcnAry3FT8CAFBpMgz$66UhTTFmVdVyuF/tBTTe1C3/PQ6WHHo/HW8oDttUflc=', '2024-05-30 20:55:51.639674', 0, 'luislo', '', '', '', 0, 1, '2024-05-30 20:53:08.329906'),
(26, 'pbkdf2_sha256$720000$vUFRKHRc4ev7QVynU5lgqK$lNN+Ht63Yk+o8QGFSIEJHqCw4Nrva/1tfBGSJhRczgY=', '2024-06-02 17:33:23.538556', 0, 'JNM', '', '', '', 0, 1, '2024-06-02 17:28:42.982747'),
(27, 'pbkdf2_sha256$720000$an3mwDnc4p04XUwUGncPSS$OstePkZIU0oJWMOIb6h8puG8wdwfBvLVa+iIhx4YJKE=', '2024-06-02 17:55:03.689720', 0, 'danni', '', '', '', 0, 1, '2024-06-02 17:55:03.152956'),
(28, 'pbkdf2_sha256$720000$6fi0kpmE9vZSrx6v36VMvD$0NB5sIk9e6J2b95QAXakQNiBPag+x/7qHdA1A7IDhkw=', '2024-06-02 18:05:07.508513', 0, 'maria11', '', '', '', 0, 1, '2024-06-02 18:05:06.970960');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
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
-- Estructura de tabla para la tabla `auth_user_user_permissions`
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
-- Estructura de tabla para la tabla `django_admin_log`
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
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-04-23 19:35:38.074774', '18', 'Objetos object (18)', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 13, 1),
(2, '2024-05-15 10:27:20.733376', '3', 'Objetos object (3)', 2, '[{\"changed\": {\"fields\": [\"Precio\"]}}]', 13, 1),
(3, '2024-05-20 20:30:49.222285', '37', 'Objetos object (37)', 1, '[{\"added\": {}}]', 13, 1),
(4, '2024-05-20 20:31:09.645600', '37', 'Objetos object (37)', 3, '', 13, 1),
(5, '2024-05-21 09:04:59.909543', '50', 'Inventario object (50)', 2, '[{\"changed\": {\"fields\": [\"Cantidad\"]}}]', 11, 1),
(6, '2024-05-26 11:21:50.443459', '38', 'Lanzacohetes', 1, '[{\"added\": {}}]', 13, 1),
(7, '2024-05-27 15:40:48.283345', '6', 'Chaleco Táctico', 2, '[{\"changed\": {\"fields\": [\"Precio\"]}}]', 13, 1),
(8, '2024-05-27 15:41:25.097226', '17', 'dani2', 2, '[{\"changed\": {\"fields\": [\"Dinero\"]}}]', 12, 1),
(9, '2024-05-27 15:58:41.754151', '13', 'Munición de lanzaranadas', 2, '[{\"changed\": {\"fields\": [\"Precio\"]}}]', 13, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'tfg_ps_app', 'authpermission'),
(8, 'tfg_ps_app', 'authuser'),
(9, 'tfg_ps_app', 'authuseruserpermissions'),
(10, 'tfg_ps_app', 'djangosession'),
(11, 'tfg_ps_app', 'inventario'),
(12, 'tfg_ps_app', 'jugadores'),
(13, 'tfg_ps_app', 'objetos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-04-23 17:34:07.563653'),
(2, 'auth', '0001_initial', '2024-04-23 17:34:07.896380'),
(3, 'admin', '0001_initial', '2024-04-23 17:34:08.016073'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-04-23 17:34:08.038820'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-23 17:34:08.044822'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-04-23 17:34:08.088832'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-04-23 17:34:08.115447'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-04-23 17:34:08.141966'),
(9, 'auth', '0004_alter_user_username_opts', '2024-04-23 17:34:08.146967'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-04-23 17:34:08.170973'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-04-23 17:34:08.170973'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-04-23 17:34:08.176974'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-04-23 17:34:08.202595'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-04-23 17:34:08.225599'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-04-23 17:34:08.251240'),
(16, 'auth', '0011_update_proxy_permissions', '2024-04-23 17:34:08.256241'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-04-23 17:34:08.279248'),
(18, 'sessions', '0001_initial', '2024-04-23 17:34:08.303252'),
(19, 'tfg_ps_app', '0001_initial', '2024-04-23 17:34:08.308253'),
(20, 'tfg_ps_app', '0002_delete_authpermission_delete_authuser_and_more', '2024-05-23 10:34:13.482382');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
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
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7k4azihrn8t14bqj8sn2d85hig3tlxnx', 'e30:1rzK3C:Snml49GcF7ooKsRrxv7hHThdJTArnDyvIwag3tCZgug', '2024-05-07 17:35:26.820523'),
('evzto2q7qbtipmxs0f79wem3f49vjg39', '.eJxVjDsOwjAQBe_iGlm2499S0nMGazdecADZUpxUiLuTSCmgfTPz3iLhupS0dp7TlMVZWHH63QjHJ9cd5AfWe5Njq8s8kdwVedAury3z63K4fwcFe9lqr1B5RqQxOPBg7GCzIcNMNxu0hsFpUAxOI7PzAASWfLQhmrg1JorPF9fiN1Y:1s14Cg:StetKoHukJ46sE9T71g4fWlGVt3dXKqtHRpx1CChkYo', '2024-05-12 13:04:26.354552'),
('e0vv1gdv99r8lp2uuxmrpe8bzv3zyog3', '.eJxVjDsOwjAQBe_iGlm2499S0nMGazdecADZUpxUiLuTSCmgfTPz3iLhupS0dp7TlMVZWHH63QjHJ9cd5AfWe5Njq8s8kdwVedAury3z63K4fwcFe9lqr1B5RqQxOPBg7GCzIcNMNxu0hsFpUAxOI7PzAASWfLQhmrg1JorPF9fiN1Y:1s1WSH:vvOnpAAecsj1UEVjJNv7LAenLGqVkLRBv36Fbrf5CII', '2024-05-13 19:14:25.681000'),
('83d9kleko0ai0rqcl8xgndefslu18idd', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1s6pLv:oeP1-bAbIZWXDaBdVxLw7QFnkB1kdcd27KLaRDGUHyM', '2024-05-14 11:25:47.015852'),
('g7gutiodbumlo6ytdug2cyyq77h8fgu1', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1s7Bqn:u5YO0CdaByJQ8vg0zkpyahPh6JXJw5hlPU1j_hnWZbw', '2024-05-15 11:27:09.568071'),
('vq8auwp20em5z5g8u4hkc89cazu5tq6t', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1s7Wh7:algwpnV8D5ruZebvqltg2adndFSJuRN1ZNE46xqDl44', '2024-05-16 09:42:33.412445'),
('rpz1jpz4wq5p2x0yxsuj1g7py8qvxo0d', '.eJxVjDEOwjAMRe-SGUVYsUvKyM4ZIsdOSAElUtNOiLtDpQ6w_vfef5nA61LC2tMcJjVng-bwu0WWR6ob0DvXW7PS6jJP0W6K3Wm316bpedndv4PCvXxrh4QE6EXYMYvGnCPAoCKoAAyY6cTkFaJDBhpZRy84cNQjEYCY9wf8_zhu:1s7Bz7:pm0x28ww_g-7gJbbzYt8wEI3wQn2NngsS1AC5JcCtnM', '2024-05-15 11:35:45.782329'),
('swepu7l9zer3xeg2qicl2l89vw74mjkr', '.eJxVjEsOAiEQBe_C2hDQ5ufSvWcgDd3IqIFkmFkZ766TzEK3r6reS0RclxrXwXOcSJyFF4ffLWF-cNsA3bHdusy9LfOU5KbInQ557cTPy-7-HVQc9VtbGwLkrBP4opTOxTlmXbC4E2GwbOgITvuEijhoy2yNStmwUWCBGcT7A_LpOEQ:1s7IxK:9xdVVaiHM7yjtPOodb5tOgAovN04KZG2v_qX6fWsBrI', '2024-05-15 19:02:22.914082'),
('n54r5gps1fyunttv49hrc0a726zdwovy', '.eJxVjDsOwjAQBe_iGlm2499S0nMGa9decAA5UpxUiLuTSCmgfTPz3iLhutS0dp7TWMRZDOL0uxHmJ7cdlAe2-yTz1JZ5JLkr8qBdXqfCr8vh_h1U7HWrvULlGZFycODB2MEWQ4aZbjZoDYPToBicRmbnAQgs-WhDNHFrTBSfL9dJN1U:1s90Qw:Gi_S6bxf74Wz-0SfdUxYL2MM0q5bJJzV08pcJSuvdmY', '2024-05-20 11:39:58.847066'),
('rnnqyz5shkt3bhha74lkjsap66q68f9f', '.eJxVjDsOwjAQBe_iGlm2499S0nMGa9decAA5UpxUiLuTSCmgfTPz3iLhutS0dp7TWMRZDOL0uxHmJ7cdlAe2-yTz1JZ5JLkr8qBdXqfCr8vh_h1U7HWrvULlGZFycODB2MEWQ4aZbjZoDYPToBicRmbnAQgs-WhDNHFrTBSfL9dJN1U:1s9Qw4:3qBzRbo-Q72Rqk5nePIx2CN4pOe-S9aVxVwimvViGZs', '2024-05-21 15:57:52.810812'),
('yzea2y977gc3ywl6h6i4z9fmzokrgb99', '.eJxVjDEOwjAMRe-SGUVYsUvKyM4ZIsdOSAElUtNOiLtDpQ6w_vfef5nA61LC2tMcJjVng-bwu0WWR6ob0DvXW7PS6jJP0W6K3Wm316bpedndv4PCvXxrh4QE6EXYMYvGnCPAoCKoAAyY6cTkFaJDBhpZRy84cNQjEYCY9wf8_zhu:1s90ce:AsT5rB6I7cau423Zq0w_yQMgoz85Fhrr2VW_HlRrVrw', '2024-05-20 11:52:04.775487'),
('kkinau2n00adola19qwn6ccdiv1csyzz', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1s99bC:77OZz1fWtXNfOBWwCCVdRM5gIgmf8HRcypXsniPGzlM', '2024-05-20 21:27:10.388530'),
('kho6nn12l5fyjahbvba8lcmgr2oqvtjc', '.eJxVjEsOAiEQBe_C2hCaPy7dewYCdCujBpJhZmW8uyGZhW5fVb03i2nfatwHrXFBdmaSnX63nMqT2gT4SO3eeeltW5fMp8IPOvi1I70uh_t3UNOosxZK6uyUd1Z5C87cjBWIRRMVD2BKIANauOwpmOCyRhACpPdYICMK9vkCuzU3FQ:1s9LqK:U0pWR2l-6WTzOtOCQAR3FAeNjmTovFafFKQLfkdFkSg', '2024-05-21 10:31:36.990304'),
('jm5t93fxwcg9c1icznmen6m1e6pkkiri', '.eJxVjDsOwjAQBe_iGlm2499S0nMGa9decAA5UpxUiLuTSCmgfTPz3iLhutS0dp7TWMRZDOL0uxHmJ7cdlAe2-yTz1JZ5JLkr8qBdXqfCr8vh_h1U7HWrvULlGZFycODB2MEWQ4aZbjZoDYPToBicRmbnAQgs-WhDNHFrTBSfL9dJN1U:1s9kkh:NywMffRZMd4CuHQZ3QkM8w3gHRVid55tGqEp4Bqe0kg', '2024-05-22 13:07:27.125092'),
('mlugrbcpq7ki4cd8dy00zv0cjlgwsnm5', '.eJxVjDsOwjAQBe_iGlm2499S0nMGa9decAA5UpxUiLuTSCmgfTPz3iLhutS0dp7TWMRZDOL0uxHmJ7cdlAe2-yTz1JZ5JLkr8qBdXqfCr8vh_h1U7HWrvULlGZFycODB2MEWQ4aZbjZoDYPToBicRmbnAQgs-WhDNHFrTBSfL9dJN1U:1s9tiU:17MGHHOqXHI1OUFUdqCwTopc4WzMgY3N7GCAtAq0OGc', '2024-05-22 22:41:46.008983'),
('07l77knjxymjz9ctiaquhxsd2sj5fk8p', '.eJxVjMsOwiAQRf-FtSGlPAZcuvcbyJQZpGogKe3K-O_apAvd3nPOfYmI21ri1nmJM4mzUCBOv-OE6cF1J3THemsytbou8yR3RR60y2sjfl4O9--gYC_fOlutbdIYFKNFQlJAzgdvRu-AB1aGyTnUYFNiNqPNWZEz4DIAhWkQ7w8ScThQ:1s9shz:sLxcjAF6E5LUyVNdPja8WnE0ODxboui56nG9kkRoM4s', '2024-05-22 21:37:11.819675'),
('f8s623lx4gd4nt8q3yxellw1wcr7xde7', '.eJxVjDsKwzAQRO-iOgj91kIp0-cMYrVaRU6CDJZdmdw9NrhIqoF5b2YTEdelxrXzHMcsrkIHcfktE9KL20HyE9tjkjS1ZR6TPBR50i7vU-b37XT_Dir2uq8Dm4TGFtAeigMDCMU4G1zYE5IeyHjFGllZT9bwoEpIxOSYNCCz-HwB9jE4MA:1sA1Gf:OhkohCB3y979o5a4vh0MSX5o4f3MKqPNNNpNic3sMhU', '2024-05-23 06:45:33.734817'),
('yqcbjzfj91ryvxjobsznjmgx7ye6lgry', '.eJxVjDsOwjAQBe_iGlm2499S0nMGa9decAA5UpxUiLuTSCmgfTPz3iLhutS0dp7TWMRZDOL0uxHmJ7cdlAe2-yTz1JZ5JLkr8qBdXqfCr8vh_h1U7HWrvULlGZFycODB2MEWQ4aZbjZoDYPToBicRmbnAQgs-WhDNHFrTBSfL9dJN1U:1sA3rA:237caswuPJou7s6rbtQxPSURNuwv6Ii1oGGFPpVO0Uk', '2024-05-23 09:31:24.480700'),
('ukqi6knjb7ngg9zfjbpxoufg4c7uud7a', '.eJxVjDEOwjAMRe-SGUVYsUvKyM4ZIsdOSAElUtNOiLtDpQ6w_vfef5nA61LC2tMcJjVng-bwu0WWR6ob0DvXW7PS6jJP0W6K3Wm316bpedndv4PCvXxrh4QE6EXYMYvGnCPAoCKoAAyY6cTkFaJDBhpZRy84cNQjEYCY9wf8_zhu:1sA5mS:Qr0aPuWCIiqCbY3W34ZXKw5GJTEh0k0hJgfgjOqQ7Z0', '2024-05-23 11:34:40.015662'),
('1n5cdhxhmkcinfrgnu6978zdh6ebr6zm', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1sAW4r:RYDMsC5gnnPhElNekY4ZDqFOYpt-yCToz59LD515w9k', '2024-05-24 15:39:25.217843'),
('xsuxorqmsqb7htjwtvo7xuouaf0py380', '.eJxVjEsOwiAUAO_C2hB4IB-X7nsGwuOBVA1NSrsy3l1JutDtzGReLMR9q2HveQ0zsQsDyU6_EGN65DYM3WO7LTwtbVtn5CPhh-18Wig_r0f7N6ix1_FFabw6o7AeQZniSRTQEb5Uk7Ig0BBhEtnGAk6A05a00qUUSc46yd4f6b83dQ:1sBBxC:2DNfmPmBVhtzhdwXaHMdLxWo8cZ6tieFMxzrclrt-jI', '2024-05-26 12:22:18.422376'),
('5029ichzbo1rnho56y3z23wyimly6onf', '.eJxVjMsOwiAQRf-FtSEOw6O4dN9vIAMDUjU0Ke3K-O_apAvd3nPOfYlA21rD1vMSJhYXAeL0u0VKj9x2wHdqt1mmua3LFOWuyIN2Oc6cn9fD_Tuo1Ou31smUAgm0Qu8oKU3MiOg8KhzIsEfKztpoLBdVKOPgtTmDxQzgtbLi_QHXnDcW:1sBC6f:dP-E7KktrMfJ7N8RJP_xLhEH8tndUuA72RW-Xk6orMA', '2024-05-26 12:32:05.800737');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

DROP TABLE IF EXISTS `inventario`;
CREATE TABLE IF NOT EXISTS `inventario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jugador_id` int DEFAULT NULL,
  `objeto_id` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jugador_id` (`jugador_id`,`objeto_id`),
  KEY `inventario_objeto_id_fk` (`objeto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id`, `jugador_id`, `objeto_id`, `cantidad`) VALUES
(1, 1, 1, 1),
(2, 1, 4, 1),
(3, 1, 7, 1),
(4, 1, 10, 1),
(5, 2, 2, 1),
(52, 11, 35, 1),
(61, 2, 1, 1),
(8, 2, 11, 1),
(67, 4, 6, 1),
(83, 3, 2, 1),
(84, 3, 5, 3),
(30, 3, 1, 2),
(32, 6, 22, 1),
(51, 4, 3, 1),
(90, 19, 18, 1),
(50, 4, 21, 1),
(17, 5, 2, 1),
(18, 5, 5, 1),
(19, 5, 8, 1),
(20, 5, 11, 1),
(34, 7, 3, 1),
(35, 7, 5, 1),
(46, 4, 33, 1),
(37, 8, 30, 1),
(38, 8, 31, 1),
(41, 6, 32, 1),
(42, 6, 21, 1),
(43, 6, 3, 1),
(44, 6, 31, 1),
(45, 6, 30, 1),
(53, 11, 1, 1),
(54, 11, 33, 1),
(55, 11, 34, 1),
(58, 13, 1, 2),
(59, 13, 2, 2),
(60, 13, 3, 1),
(62, 2, 3, 1),
(63, 2, 4, 1),
(64, 2, 34, 1),
(92, 19, 5, 1),
(68, 4, 4, 2),
(69, 4, 8, 1),
(70, 15, 26, 1),
(71, 15, 24, 1),
(72, 16, 1, 1),
(73, 16, 3, 1),
(74, 17, 14, 1),
(75, 17, 22, 1),
(76, 17, 35, 1),
(77, 17, 4, 1),
(78, 17, 5, 1),
(79, 18, 34, 1),
(80, 18, 3, 1),
(89, 19, 12, 1),
(91, 19, 2, 1),
(93, 19, 33, 1),
(94, 19, 4, 3),
(95, 20, 36, 1),
(96, 21, 5, 1),
(97, 21, 8, 1),
(98, 21, 33, 1),
(99, 21, 14, 1),
(100, 22, 35, 1),
(101, 22, 3, 1),
(102, 23, 21, 1),
(103, 23, 2, 1),
(104, 23, 30, 1),
(105, 24, 5, 1),
(106, 24, 35, 1),
(107, 24, 28, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugadores`
--

DROP TABLE IF EXISTS `jugadores`;
CREATE TABLE IF NOT EXISTS `jugadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `dinero` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `jugadores`
--

INSERT INTO `jugadores` (`id`, `user_id`, `dinero`) VALUES
(1, 1, 1000),
(2, 2, 515),
(3, 3, 615),
(4, 4, 2120),
(6, 8, 1695),
(7, 9, 4765),
(8, 10, 4550),
(9, 11, 5000),
(10, 12, 5000),
(11, 13, 3250),
(12, 14, 5000),
(13, 15, 4395),
(14, 16, 5000),
(15, 17, 4200),
(16, 18, 4745),
(17, 19, 50000),
(18, 20, 4595),
(19, 21, 3270),
(20, 22, 0),
(21, 23, 3540),
(22, 24, 4295),
(23, 25, 3650),
(24, 26, 3750),
(25, 27, 5000),
(26, 28, 5000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetos`
--

DROP TABLE IF EXISTS `objetos`;
CREATE TABLE IF NOT EXISTS `objetos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `precio` int NOT NULL,
  `tipo_objeto` enum('Arma','Municion','Curacion','Armadura','Skin') DEFAULT NULL,
  `url_imagen` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `objetos`
--

INSERT INTO `objetos` (`id`, `nombre`, `descripcion`, `precio`, `tipo_objeto`, `url_imagen`) VALUES
(1, 'Cuchillo', 'Un cuchillo afilado, ideal para combates cuerpo a cuerpo.', 50, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/0/04/Arm2_%281%29.jpg/revision/latest?cb=20120415030947&path-prefix=es'),
(2, 'Pistola Samurai Edge', 'La icónica pistola de S.T.A.R.S., modelo Samurai Edge.', 150, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/b/b1/PistolajillRE.png/revision/latest?cb=20200205224138&path-prefix=es'),
(3, 'Escopeta M37', 'Una poderosa escopeta de doble cañón, ideal para enfrentarse a hordas de enemigos.', 205, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/f/f9/Escopeta_M37.jpg/revision/latest/scale-to-width-down/1000?cb=20170127192932&path-prefix=es'),
(4, 'Granada de Fragmentación', 'Una granada explosiva que causa daño en un área determinada.', 80, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/2/2d/Granada_de_mano_RE2_remake.jpg/revision/latest/scale-to-width-down/1000?cb=20190205050418&path-prefix=es'),
(5, 'Spray Medicinal', 'Un spray medicinal que restaura una cantidad moderada de salud.', 300, 'Curacion', 'https://static.wikia.nocookie.net/residentevil/images/6/60/Spray_primeros_auxilios.png/revision/latest?cb=20200625210523&path-prefix=es'),
(6, 'Chaleco Táctico', 'Un chaleco táctico que proporciona una protección moderada.', 150, 'Armadura', 'https://static.wikia.nocookie.net/residentevil/images/8/89/Chaleco_antibalas_RE4R.png/revision/latest?cb=20230619134025&path-prefix=es'),
(7, 'Traje de Kevlar', 'Un traje de kevlar que proporciona una protección excepcional.', 200, 'Armadura', 'https://i.etsystatic.com/30592998/r/il/b10746/4041638410/il_fullxfull.4041638410_6z9c.jpg'),
(8, 'Hierba Verde', 'Una hierba verde que restaura cierta cantidad de salud.', 150, 'Curacion', 'https://static.wikia.nocookie.net/residentevil/images/a/a3/Hierba_verde.png/revision/latest?cb=20200625210632&path-prefix=es'),
(9, 'Hierba Roja', 'Una hierba roja que potencia la curación si se combina con una verde.', 250, 'Curacion', 'https://static.wikia.nocookie.net/residentevil/images/e/ea/Hierba_roja.png/revision/latest?cb=20200625210642&path-prefix=es'),
(11, 'Munición de 9mm', 'Munición estándar para la pistola.', 10, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/e/e0/Munici%C3%B3n_pistola_RE0.png/revision/latest?cb=20200702073508&path-prefix=es'),
(12, 'Munición de Escopeta', 'Munición de escopeta de calibre 12.', 15, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/3/32/Cartuchos_de_escopeta_RE4_remake.png/revision/latest?cb=20230615203215&path-prefix=es'),
(13, 'Munición de lanzaranadas', 'Munición especial para lanzagranadas.', 50, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/5/5a/Granadas_explosivas_RE0.png/revision/latest?cb=20200702073540&path-prefix=es'),
(14, 'Piedra de afilar', 'Afilar el cuchillo', 10, 'Municion', 'https://www.eliteguias.com/img/juegos/elden-ring/hoja-de-afilar-de-piedras-refulgentes.jpg'),
(15, 'Botiquín de Primeros Auxilios', 'Un botiquín básico que restaura una cantidad moderada de salud.', 40, 'Curacion', 'https://static.wikia.nocookie.net/residentevil/images/0/02/Botiqu%C3%ADn.jpg/revision/latest?cb=20180311235815&path-prefix=es'),
(16, 'Botiquín Avanzado', 'Un botiquín avanzado que restaura una cantidad considerable de salud.', 80, 'Curacion', 'https://static.wikia.nocookie.net/residentevil/images/1/1f/Botiquin_abierto.jpg/revision/latest?cb=20180318203708&path-prefix=es'),
(17, 'Escudo Anti-Criaturas', 'Un escudo diseñado específicamente para protegerse de las criaturas.', 50, 'Armadura', 'https://static.wikia.nocookie.net/residentevil/images/0/00/Escudo_de_los_Salazar.jpg/revision/latest/scale-to-width-down/1000?cb=20180414045641&path-prefix=es'),
(18, 'Granada de Humo', 'Granada de humo para encubrir.', 25, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/3/3a/Flash_Grenade.jpg/revision/latest?cb=20130802001027&path-prefix=es'),
(19, 'Granada Paralizante', 'Granada paralizante que aturde temporalmente a los enemigos.', 35, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/1/1f/Incendiary_Grenade.jpg/revision/latest?cb=20130801234028&path-prefix=es'),
(20, 'Poción de Velocidad', 'Poción que aumenta temporalmente la velocidad del jugador.', 30, 'Curacion', 'https://img.freepik.com/fotos-premium/pocion-magica-velocidad-etiqueta-botella-tiene-simbolo-remolino-que-sugiere-velocidad_555090-30509.jpg'),
(21, 'Skin de Leon S. Kennedy', 'Una skin que transforma el aspecto del personaje en Leon S. Kennedy, el protagonista de Resident Evil 2.', 800, 'Skin', 'https://i0.wp.com/www.residenteviljacket.com/wp-content/uploads/2023/10/1-Resident-Evil-4-Jacket-Leon-S-Kennedy-Shearling-Jacket.webp?fit=500%2C680&ssl=1'),
(22, 'Skin de Jill Valentine', 'Una skin que cambia el aspecto del personaje en Jill Valentine, la heroína de Resident Evil 3.', 850, 'Skin', 'https://static.wikia.nocookie.net/nemesis/images/5/58/Jill-valentine.jpg/revision/latest?cb=20101106192009&path-prefix=es'),
(23, 'Skin de Nemesis', 'Una skin que convierte al personaje en Nemesis, la temible criatura de Resident Evil 3.', 1000, 'Skin', 'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2019/11/resident-evil-3-nemesis_0.jpg?tf=3840x'),
(24, 'Lanzagranadas', 'Un arma que dispara granadas explosivas.', 500, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/2/22/Lanzagranadas_REmake.jpg/revision/latest?cb=20191213153913&path-prefix=es'),
(25, 'Municion acida', 'Munición especial que contiene ácido, utilizada en el lanzagranadas.', 300, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/2/22/Granadas_%C3%A1cidas_RE0.png/revision/latest?cb=20200702073608&path-prefix=es'),
(26, 'Municion incendiaria', 'Munición que causa incendios, utilizada en el lanzagranadas.', 300, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/9/91/Granadas_%C3%ADgneas_RE0.png/revision/latest?cb=20200702073558&path-prefix=es'),
(28, 'Rifle de asalto', 'Un arma automática de alta cadencia de fuego.', 450, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/1/1d/Rifle_de_asalto_CQBR_RE4_arma.jpg/revision/latest/scale-to-width-down/1000?cb=20230626071225&path-prefix=es'),
(29, 'Municion para rifle de asalto', 'Munición utilizada en el rifle de asalto.', 200, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/b/bf/Cargador_ametralladora_RE0.png/revision/latest?cb=20200702073639&path-prefix=es'),
(30, 'Magnum 357', 'Un potente revólver de gran calibre.', 400, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/5/55/Rev%C3%B3lver_magnum.jpg/revision/latest?cb=20191213144929&path-prefix=es'),
(31, 'Balas para magnum', 'Munición para el revólver Magnum 45.', 50, 'Municion', 'https://static.wikia.nocookie.net/residentevil/images/c/c4/Balas_magnum_RE0.png/revision/latest?cb=20200702073529&path-prefix=es'),
(32, 'Skin de Ada Wong', 'Aspecto alternativo para el personaje Ada Wong.', 1000, 'Skin', 'https://new.imagehostx.com/upload/2024/02/26/ada-wong-pack-for-g8f-01_1708920698.jpg'),
(33, 'Skin de Wesker', 'Aspecto alternativo para el personaje Wesker.', 1000, 'Skin', 'https://i.pinimg.com/736x/f1/f7/e5/f1f7e520e7269462a71fa14099550966.jpg'),
(34, 'Chaleco S.T.A.R.S.', 'Chaleco táctico usado por miembros del equipo S.T.A.R.S.', 200, 'Armadura', 'https://i.ebayimg.com/images/g/UPAAAOSw615g2sUS/s-l1200.webp'),
(35, 'Gabardina UMBRELLA', 'Gabardina utilizada por agentes de UMBRELLA.', 500, 'Armadura', 'https://m.media-amazon.com/images/I/61n62MoRePL.jpg'),
(36, 'Remedio virus-T', 'Remedio para el virus-T.', 5000, 'Curacion', 'https://ae01.alicdn.com/kf/S31733e8c33514414aa02a84d318b04bdq/Umbrella-biochemistry-Suitcase-T-Virus-Vial-Display-Case-Cosplay-horror-Movie-Villainous-Item-Prop-Replica.jpg'),
(38, 'Lanzacohetes', 'El lanzacohetes es un RPG-7 de origen ruso muy poderoso, solo una ojiva. Suele derribar de un solo golpe a todos los enemigos.', 30000, 'Arma', 'https://static.wikia.nocookie.net/residentevil/images/b/ba/Rocket-launcherre5.png/revision/latest?cb=20200304225043&path-prefix=es');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
