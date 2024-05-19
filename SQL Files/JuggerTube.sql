DROP DATABASE IF EXISTS JuggerTube;
CREATE DATABASE JuggerTube;
USE JuggerTube;

SET NAMES utf8;
SET character_set_client = utf8mb4;

CREATE TABLE Tournaments (
	TournamentID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DateBeginning DATE NOT NULL,
    DateEnding DATE NOT NULL,
    City VARCHAR(50) NOT NULL,
    JTRLink VARCHAR(100) NOT NULL,
    PRIMARY KEY (TournamentID)
);

CREATE TABLE Teams (
	TeamID INT NOT NULL AUTO_INCREMENT,
	Name VARCHAR(100) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    PRIMARY KEY (TeamID)
);

CREATE TABLE Users (
	UserID INT NOT NULL AUTO_INCREMENT,
    EMail VARCHAR(100) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password TEXT NOT NULL,
    PRIMARY KEY (UserID)
);

CREATE TABLE Channels (
	ChannelID int NOT NULL AUTO_INCREMENT,
    Name VARCHAR(75) NOT NULL,
    Link VARCHAR(50) NOT NULL,
    PRIMARY KEY (ChannelID)
);

CREATE TABLE Videos (
	VideoID int NOT NULL AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    ChannelID int NOT NULL,
    Link VARCHAR(50) NOT NULL,
    TournamentID int NOT NULL,
    TeamOneID int NOT NULL,
    TeamTwoID int NOT NULL,
    UploadDate DATE NOT NULL,
    Comments MEDIUMTEXT,
    Type ENUM ('reports', 'highlights', 'tutorials', 'building', 'matches', 'music', 'podcast', 'other'),
    PRIMARY KEY (VideoID),
    FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID),
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID),
    FOREIGN KEY (TeamOneID) REFERENCES Teams(TeamID),
    FOREIGN KEY (TeamTwoID) REFERENCES Teams(TeamID)
);

CREATE TABLE user_has_channel (
	UserID INT NOT NULL,
    ChannelID INT NOT NULL,
    PRIMARY KEY (UserID, ChannelID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ChannelID) REFERENCES Channels(ChannelID)
);

CREATE TABLE user_is_part_of_team (
	UserID INT NOT NULL,
    TeamID INT NOT NULL,
    PRIMARY KEY (UserID, TeamID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);
    
