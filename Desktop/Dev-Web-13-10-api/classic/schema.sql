CREATE DATABASE IF NOT EXISTS `2026_m1` CHARACTER SET utf8mb4;
USE `2026_m1`;

CREATE TABLE IF NOT EXISTS utilisateur (
    id_u    INT AUTO_INCREMENT PRIMARY KEY,
    nom_u   VARCHAR(100) NOT NULL,
    email_u VARCHAR(255) NOT NULL UNIQUE,
    mdp_u   VARCHAR(255) NOT NULL,
    role_u  ENUM('client','admin') NOT NULL DEFAULT 'client'
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS produit (
    id_p          INT AUTO_INCREMENT PRIMARY KEY,
    type_p        VARCHAR(100) NOT NULL,
    designation_p VARCHAR(255) NOT NULL,
    prix_ht       DECIMAL(10,2) NOT NULL,
    ppromo        TINYINT UNSIGNED NULL,          -- % de promo, NULL = pas de promo
    image_p       VARCHAR(255) NULL,              -- fichier dans uploads/
    date_in       DATE NOT NULL,
    times_in      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stock_p       INT NOT NULL DEFAULT 0
) ENGINE=InnoDB;
