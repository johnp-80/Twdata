-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.6.17-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             8.3.0.4799
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for w70
CREATE DATABASE IF NOT EXISTS `w70` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `w70`;


-- Dumping structure for table w70.ally
CREATE TABLE IF NOT EXISTS `ally` (
  `ally_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `tag` varchar(50) DEFAULT NULL,
  `members` int(11) DEFAULT NULL,
  `villages` int(11) DEFAULT NULL,
  `points` double DEFAULT NULL,
  `all_points` double DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`ally_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.ally_oda
CREATE TABLE IF NOT EXISTS `ally_oda` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.ally_odd
CREATE TABLE IF NOT EXISTS `ally_odd` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.ally_odt
CREATE TABLE IF NOT EXISTS `ally_odt` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.conquer
CREATE TABLE IF NOT EXISTS `conquer` (
  `village_id` int(11) NOT NULL,
  `unix_timestamp` int(11) DEFAULT NULL,
  `new_owner` int(11) NOT NULL,
  `old_owner` int(11) NOT NULL,
  KEY `unix_timestamp` (`unix_timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for procedure w70.emptyConquer
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `emptyConquer`()
BEGIN
	TRUNCATE w70.conquer;

END//
DELIMITER ;


-- Dumping structure for procedure w70.findPlayer
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `findPlayer`(IN `player_name` VARCHAR(50))
    READS SQL DATA
    COMMENT 'Returns Player information similar to what is displayed on a village info screen in tribalwars. '
BEGIN
    Select player.name, ally.name, player.points, player.villages, player.rank from ally, player
    where player.name like player_name and player.ally = ally.ally_id;
END//
DELIMITER ;


-- Dumping structure for procedure w70.findPlayerId
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `findPlayerId`(IN `player_name` VARCHAR(50))
    COMMENT 'looks up a player by name, gets the player id'
BEGIN
	Select player.id from player where player.name like player_name;
END//
DELIMITER ;


-- Dumping structure for procedure w70.findVillage
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `findVillage`(in v_x int, v_y int)
BEGIN
	Select village.name, village.points, player.name, player.points, ally.name, ally.tag 
		from ally, player, village
		where village.x = v_x and village.y = v_y and village.player = player.id and player.ally = ally.ally_id;
END//
DELIMITER ;


-- Dumping structure for table w70.player
CREATE TABLE IF NOT EXISTS `player` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `ally` int(11) DEFAULT NULL,
  `villages` int(10) unsigned DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.player_oda
CREATE TABLE IF NOT EXISTS `player_oda` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  KEY `player_id` (`id`),
  CONSTRAINT `player_id` FOREIGN KEY (`id`) REFERENCES `player` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.player_odd
CREATE TABLE IF NOT EXISTS `player_odd` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.player_odt
CREATE TABLE IF NOT EXISTS `player_odt` (
  `rank` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for procedure w70.retrievePlayerVillages
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `retrievePlayerVillages`(IN `player_name` VARCHAR(50))
    READS SQL DATA
BEGIN
	Select village.id, village.name, village.player,
	       village.x, village.y, village.points,
	       village.rank
	from village, player where village.player = player.id and 
	player.name like player_name;

END//
DELIMITER ;


-- Dumping structure for procedure w70.updateAlly
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateAlly`(in a_id int, a_name varchar(50), a_tag varchar(50), 
								a_members int, a_villages int, a_points double, a_all_points double,
										a_rank int)
BEGIN
	insert into ally (ally_id, name, tag, members, villages, points, all_points, rank) 
		values(a_id, a_name, a_tag, a_members, a_villages, a_points, a_all_points, a_rank)
		on duplicate key update `name` = a_name, tag = a_tag, members = a_members, 
			villages = a_villages, points = a_points, all_points = a_all_points, rank = a_rank;
END//
DELIMITER ;


-- Dumping structure for procedure w70.updateAllyODA
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateAllyODA`(IN `rank` INT, IN `id` INT, IN `score` INT)
BEGIN
	INSERT INTO ally_oda (rank, id, score) VALUES(rank, id, score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updateAllyODD
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateAllyODD`(IN `id` INT, IN `rank` INT, IN `score` INT)
BEGIN
	INSERT INTO ally_odt (id, rank, score) Values(id, rank, score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updateAllyODT
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateAllyODT`(IN `od_rank` INT, IN `od_id` INT, IN `od_score` INT)
BEGIN
	INSERT INTO ally_odt (rank, id, score) VALUES(od_rank, od_id, od_score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updateConquer
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateConquer`( IN village_id  int , IN t_stamp int , IN n_owner int , IN o_owner int )
    READS SQL DATA
BEGIN
    INSERT INTO conquer ( village_id , unix_timestamp , new_owner , old_owner )
     VALUES ( village_id , t_stamp , n_owner , o_owner ) on
     duplicate key update `village_id` = village_id ,
      `new_owner` = n_owner , `old_owner` = o_owner ;
  END//
DELIMITER ;


-- Dumping structure for procedure w70.updatePlayer
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updatePlayer`(IN `id` int, IN `name` varchar(50), IN `ally` int, IN `villages` INT, IN `points` int, IN `rank` int)
BEGIN
	INSERT into player (id, name, ally, villages, points, rank) values(id, name, ally, villages, points, rank)
		ON duplicate key update name = name, ally = ally, villages = villages, points = points, rank = rank;
END//
DELIMITER ;


-- Dumping structure for procedure w70.updatePlayerODA
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updatePlayerODA`(IN `id` INT, IN `rank` INT, IN `score` INT)
BEGIN
	INSERT into player_oda values(id, rank, score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updatePlayerODD
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updatePlayerODD`(IN `id` INT, IN `rank` INT, IN `score` INT)
BEGIN
	INSERT into player_odd (id, rank, score) Values(id, rank, score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updatePlayerODT
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updatePlayerODT`(IN `id` INT, IN `rank` INT, IN `score` INT)
BEGIN
	INSERT into player_odt (id, rank, score) values(id, rank, score);
END//
DELIMITER ;


-- Dumping structure for procedure w70.updateVillage
DELIMITER //
CREATE DEFINER=`johnp80`@`%` PROCEDURE `updateVillage`(IN `id` int, IN `name` longtext, IN `x` int, IN `y` int, IN `player` int, IN `points` int, IN `rank` int)
BEGIN
	INSERT INTO village (`id`, `name`, `x`, `y`, `player`, `points`, `rank`) 
	values(id, name, x, y, player, points, rank)
	ON DUPLICATE key update `name` = name, `player` = player, `points` = points;
END//
DELIMITER ;


-- Dumping structure for table w70.village
CREATE TABLE IF NOT EXISTS `village` (
  `id` int(11) NOT NULL,
  `name` longtext NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `player` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `rank` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table w70.village_change
CREATE TABLE IF NOT EXISTS `village_change` (
  `v_id` int(11) DEFAULT NULL,
  `time_stamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `points_change` int(11) DEFAULT NULL,
  KEY `village_id` (`v_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
