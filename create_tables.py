# coding=utf-8
import mysql.connector
from mysql.connector import errorcode


###
# First fill tables into one dict entry each, with the key being the table name and value being the SQL.
###

TABLES = {}

TABLES['bruker'] = (
"	CREATE TABLE `bruker`("
"	  `brukernavn` varchar(20) NOT NULL,"
"	  `kjønn`        varchar(6),"
"	  `alder`       int(10),"
"	  CONSTRAINT `brukernavn_PK` PRIMARY KEY (`brukernavn`)"
"	) ENGINE=InnoDB")

TABLES['treningsøkt'] = (
"	CREATE TABLE `treningsøkt`("
"	  `øktid`              int(10) NOT NULL,"
"	  `varighet`           TIME,"
"	  `idrett`             varchar(20),"
"	CONSTRAINT `treningsøkt_PK` PRIMARY KEY (`øktid`)"
"	) ENGINE=InnoDB")

TABLES['har_trent'] = (
"	CREATE TABLE `har_trent`("
"	  `brukernavn`     varchar(20) NOT NULL,"
"	  `øktid`          int(10) NOT NULL,"
"	  `dato`           date,"
"	  `Tidspunkt`      TIME,"
"	  `prestasjon`     varchar(100),"
"	  `personlig_form` varchar(50),"
"	  CONSTRAINT `brukernavn_FK` FOREIGN KEY (`brukernavn`) REFERENCES `bruker`(`brukernavn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `øktid_FK`      FOREIGN KEY (`øktid`)      REFERENCES `treningsøkt`(`øktid`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['innendørsøkt'] = (
"	CREATE TABLE `innendørsøkt`("
"	  `øktid`             int(10) NOT NULL,"
"	  `ventilasjon`       varchar(30),"
"	  `antall_tilskuere`  INT,"
"	  CONSTRAINT `innendørsøktid_FK` FOREIGN KEY(`øktid`) REFERENCES treningsøkt(`øktid`)"
"	                                                           ON UPDATE CASCADE"
"	                                                           ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['utendørsøkt'] = (
"	CREATE TABLE `utendørsøkt`("
"	  `øktid`             int(10) NOT NULL,"
"	  `Temperatur`        int(10),"
"	  `værtype`           varchar(20),"
"	  CONSTRAINT `utendørsøktid_FK` FOREIGN KEY(`øktid`) REFERENCES treningsøkt(`øktid`)"
"	                                                           ON UPDATE CASCADE"
"	                                                           ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['målinger'] = (
"	CREATE TABLE `målinger`("
"	  `tidspunkt`         int(10) NOT NULL,"
"	  `øktid`             int(10) NOT NULL,"
"	  `puls`              int(10),"
"	  `breddegrad`        DOUBLE,"
"	  `lengdegrad`        DOUBLE,"
"	  `moh`				  DOUBLE,"
"	  CONSTRAINT `målinger_PK` PRIMARY KEY (`tidspunkt`),"
"	  CONSTRAINT `målinger_FK` FOREIGN KEY (`øktid`) REFERENCES treningsøkt(`øktid`)"
"	                                                           ON UPDATE CASCADE"
"	                                                           ON DELETE NO ACTION"
"	) ENGINE=InnoDB")

TABLES['mal'] = (
"	CREATE TABLE `mal`("
"	  `mal_navn`         varchar(20) NOT NULL,"
"	  `øktid`            int(10) NOT NULL,"
"	  CONSTRAINT `mal_PK` PRIMARY KEY(`mal_navn`),"
"	  CONSTRAINT `mal_FK` FOREIGN KEY(`øktid`) REFERENCES `treningsøkt`(`øktid`)"
"	                                                           ON UPDATE CASCADE"
"	                                                           ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['øvelse'] = (
"	CREATE TABLE `øvelse`("
"	  `øvelse_navn`     varchar(20) NOT NULL,"
"	  `beskrivelse`     varchar(200),"
"	  `antall_reps`     int(10),"
"	  `antall_sett`     int(10),"
"	  `belastning`      varchar(30),"
"	  CONSTRAINT `øvelse_PK` PRIMARY KEY(`øvelse_navn`)"
"	) ENGINE=InnoDB")

TABLES['utført'] = (
"	CREATE TABLE `utført`("
"	  `repetisjoner` int(10),"
"	  `sett`         int(10),"
"	  `vekt`         int(10),"
"	  `lengde`       varchar(10),"
"	  `kommentar`    varchar(200),"
"	  `øktid`        int(10) NOT NULL,"
"	  `øvelse_navn`  varchar(20),"
"	  CONSTRAINT `inneholder_FK1`    FOREIGN KEY(`øktid`) REFERENCES `treningsøkt`(`øktid`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `inneholder_FK2`    FOREIGN KEY(`øvelse_navn`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['mål'] = (
"	CREATE TABLE `mål`("
"	  `målid`        int(10) NOT NULL,"
"	  `tidsfrist`    date,"
"	  `repetisjoner` int(10),"
"	  `sett`         int(10),"
"	  `vekt`         int(10),"
"	  `lengde`       varchar(10),"
"	  `kommentar`    varchar(200),"
"	  `brukernavn`   varchar(200),"
"	  `øvelse_navn`  varchar(200),"
"	  CONSTRAINT `mål_PK` PRIMARY KEY (`målid`),"
"	  CONSTRAINT `bruker_FK` FOREIGN KEY(`brukernavn`) REFERENCES `bruker`(`brukernavn`)"
"	                                                      ON UPDATE CASCADE"
"	                                                      ON DELETE CASCADE,"
"	  CONSTRAINT `øvelse_FK` FOREIGN KEY(`øvelse_navn`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                      ON UPDATE CASCADE"
"	                                                      ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['styrkeøvelse'] = (
"	CREATE TABLE `styrkeøvelse`("
"	  `øvelse_navn`    varchar(20) NOT NULL,"
"	  CONSTRAINT `styrkeøvelse_FK` FOREIGN KEY(`øvelse_navn`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                      ON UPDATE CASCADE"
"	                                                      ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['kondisjonsøvelse'] = (
"	CREATE TABLE `kondisjonsøvelse`("
"	  `øvelse_navn`    varchar(20) NOT NULL,"
"	  CONSTRAINT `kondisjonsøvelse_FK` FOREIGN KEY(`øvelse_navn`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                      ON UPDATE CASCADE"
"	                                                      ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['kan_erstatte'] = (
"	CREATE TABLE `kan_erstatte`("
"	  `navn1`   varchar(20) NOT NULL,"
"	  `navn2`   varchar(20) NOT NULL,"
"	  CONSTRAINT `kan_erstatte_FK1` FOREIGN KEY(`navn1`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `kan_erstatte_FK2` FOREIGN KEY(`navn2`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['kategori'] = (
"	CREATE TABLE `kategori`("
"	  `kategori_navn` varchar(30) NOT NULL,"
"	  CONSTRAINT `kategori_PK` PRIMARY KEY(`kategori_navn`)"
"	) ENGINE=InnoDB")

TABLES['under_gruppe'] = (
"	CREATE TABLE `under_gruppe`("
"	  `kategori_navn1` varchar(20),"
"	  `kategori_navn2` varchar(20),"
"	  CONSTRAINT `under_gruppe_FK1` FOREIGN KEY(`kategori_navn1`) REFERENCES `kategori`(`kategori_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `under_gruppe_FK2` FOREIGN KEY(`kategori_navn2`) REFERENCES `kategori`(`kategori_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['over_gruppe'] = (
"	CREATE TABLE `over_gruppe`("
"	  `kategori_navn1` varchar(20),"
"	  `kategori_navn2` varchar(20),"
"	  CONSTRAINT `over_gruppe_FK1` FOREIGN KEY(`kategori_navn1`) REFERENCES `kategori`(`kategori_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `over_gruppe_FK2` FOREIGN KEY(`kategori_navn2`) REFERENCES `kategori`(`kategori_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"	) ENGINE=InnoDB")

TABLES['medlem_av_kategori'] = (
"	CREATE TABLE `medlem_av_kategori`("
"	  `øvelse_navn`     varchar(20),"
"	  `kategori_navn`   varchar(20),"
"	  CONSTRAINT `medlem_av_kategori_FK1`     FOREIGN KEY(`øvelse_navn`) REFERENCES `øvelse`(`øvelse_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE,"
"	  CONSTRAINT `medlem_av_kategori_FK2`  FOREIGN KEY(`kategori_navn`) REFERENCES `kategori`(`kategori_navn`)"
"	                                                         ON UPDATE CASCADE"
"	                                                         ON DELETE CASCADE"
"     ) ENGINE=InnoDB")


def execute_create_tables(cursor, cnx):
    global TABLES
    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cnx.commit()
