CREATE TABLE `user` (
`username` VARCHAR(255) NOT NULL,
`password` VARCHAR(255) NOT NULL,
`email` VARCHAR(255) NOT NULL,
PRIMARY KEY (`username`));

CREATE TABLE `note` (
`intitule` VARCHAR(255) NOT NULL,
`note` DECIMAL(5) NULL,
`matiere` VARCHAR(255) NULL,
`partie` VARCHAR(255) NULL,
`type` VARCHAR(255) NULL,
`username` VARCHAR(255) NULL,
PRIMARY KEY (`intitule`),
CONSTRAINT `username`
FOREIGN KEY (`username`)
REFERENCES `user` (`username`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);

CREATE TABLE `niveau_etude` (
`niveau_etude` VARCHAR(255) NOT NULL,
`username` VARCHAR(255) NOT NULL,
`specialite` VARCHAR(255) NOT NULL,
PRIMARY KEY (`niveau_etude`),
CONSTRAINT `username`
FOREIGN KEY (`username`)
REFERENCES `user` (`username`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);

CREATE TABLE `coefficient_matiere` (
`coefficient_matiere` DECIMAL(5) NOT NULL,
`matiere` VARCHAR(255) NOT NULL,
PRIMARY KEY (`coefficient_matiere`),
Constraint `matiere`
FOREIGN KEY (`matiere`)
REFERENCES `note`(`matiere`)
ON DELETE no ACTION
on UPDATE no ACTION);

CREATE TABLE `coefficient_partie` (
`coefficient_partie` DECIMAL(5) NOT NULL,
`partie` VARCHAR(255) NOT NULL,
PRIMARY KEY (`coefficient_partie`),
Constraint `partie`
FOREIGN KEY (`partie`)
REFERENCES `note`(`partie`)
ON DELETE no ACTION
on UPDATE no ACTION);

CREATE TABLE `coefficient_type` (
`coefficient_type` DECIMAL(5) NOT NULL,
`type` VARCHAR(255) NOT NULL,
PRIMARY KEY (`coefficient_type`),
Constraint `type`
FOREIGN KEY (`type`)
REFERENCES `note`(`type`)
ON DELETE no ACTION
on UPDATE no ACTION);