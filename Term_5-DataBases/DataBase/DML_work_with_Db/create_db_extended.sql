USE master
IF DB_ID (N'BSUIR_TERM_5') IS NOT NULL 
BEGIN
  ALTER DATABASE BSUIR_TERM_5 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
  DROP DATABASE BSUIR_TERM_5;
END;
GO

CREATE DATABASE BSUIR_TERM_5;
GO
USE BSUIR_TERM_5;
GO


CREATE TABLE Faculty(
    ID UNIQUEIDENTIFIER NOT NULL,
    NAME VARCHAR(30) NOT NULL UNIQUE,

    CONSTRAINT PK_FACULTY PRIMARY KEY(ID)
);


CREATE TABLE TYPE_STUDY_LOAD(
    ID UNIQUEIDENTIFIER NOT NULL,
    NAME VARCHAR(120) NOT NULL UNIQUE,
    
    CONSTRAINT PK_TYPE_study_load PRIMARY KEY(ID)
);


CREATE TABLE Subjects(
    ID UNIQUEIDENTIFIER NOT NULL,
    NAME VARCHAR(120) NOT NULL,
    FACULTY_ID UNIQUEIDENTIFIER NULL,
    
    CONSTRAINT FK_FACULTY_SUBJECTS FOREIGN KEY(FACULTY_ID) REFERENCES Faculty(ID) ON DELETE CASCADE,
    CONSTRAINT pk_subjects PRIMARY KEY(ID)
);


CREATE TABLE STUDY_LOAD(
    ID CHAR(20) NOT NULL,
    hours NUMERIC NULL,
    SUBJECT_ID UNIQUEIDENTIFIER NOT NULL,
    Type_STUDY_ID UNIQUEIDENTIFIER NOT NULL,

    
    CONSTRAINT FK_SUBJECT_STUDY FOREIGN KEY(SUBJECT_ID) REFERENCES Subjects(ID) ON DELETE CASCADE,
    CONSTRAINT FK_TYPE_STUDY FOREIGN KEY(Type_STUDY_ID) REFERENCES TYPE_STUDY_LOAD(ID),
    
    CONSTRAINT chkStudyLoad CHECK(hours >= 0),
    CONSTRAINT PK_STUDY_LOAD PRIMARY KEY(ID)

);


CREATE TABLE Prepods(
    ID UNIQUEIDENTIFIER NOT NULL,
    LAST_NAME VARCHAR(120) NOT NULL,
    FIRST_NAME VARCHAR(120) NULL,
    FACULTY_ID UNIQUEIDENTIFIER NOT NULL,

    CONSTRAINT FK_STUDY_PREPODS FOREIGN KEY(FACULTY_ID) REFERENCES Faculty(ID) ON DELETE CASCADE,
    CONSTRAINT PK_PREPODS PRIMARY KEY(ID)
);



CREATE TABLE GROUPS(  
    -- PFK???
    ID UNIQUEIDENTIFIER NOT NULL,
    NAME VARCHAR(10) NOT NULL,
    HEAD_GROUP UNIQUEIDENTIFIER NULL,
    FACULTY_ID UNIQUEIDENTIFIER NOT NULL,

    CONSTRAINT FK_FACULTY_GROUP FOREIGN KEY(FACULTY_ID) REFERENCES Faculty(ID) ON DELETE CASCADE,
    CONSTRAINT pk_group PRIMARY KEY(ID),

);


CREATE TABLE LESSONS(
    GROUP_ID UNIQUEIDENTIFIER NOT NULL,
    PREPOD_ID UNIQUEIDENTIFIER NOT NULL,
    STUDY_ID CHAR(20) NOT NULL,

    CONSTRAINT FK_GROUP_LESSONS FOREIGN KEY(GROUP_ID) REFERENCES GROUPS(ID),
    CONSTRAINT PREPODS_LESSONS FOREIGN KEY(PREPOD_ID) REFERENCES Prepods(ID) ON DELETE CASCADE,
    CONSTRAINT Relationship20 FOREIGN KEY(STUDY_ID) REFERENCES STUDY_LOAD(ID),

    CONSTRAINT Key3 PRIMARY KEY(GROUP_ID, PREPOD_ID, STUDY_ID),
);


CREATE TABLE Students(
    ID UNIQUEIDENTIFIER NOT NULL,
    LAST_NAME VARCHAR(60) NOT NULL,
    FIRST_NAME VARCHAR(30) NULL,
    GROUP_ID UNIQUEIDENTIFIER NULL,

    CONSTRAINT fk_group_of_students FOREIGN KEY(GROUP_ID) REFERENCES GROUPS(ID) ON DELETE CASCADE,
    CONSTRAINT pk_students PRIMARY KEY(ID)


);
-- recursive relation group > students, students > group:
ALTER TABLE GROUPS
ADD CONSTRAINT fk_head_of_group
FOREIGN KEY(HEAD_GROUP) REFERENCES Students(ID);


CREATE TABLE RATING(
    ID UNIQUEIDENTIFIER NOT NULL,
    DATE DATE NOT NULL,
    VAL NUMERIC NULL,
    STUDENT_ID UNIQUEIDENTIFIER NOT NULL,
    STUDY_ID CHAR(20) NOT NULL,
    PREPODS_ID UNIQUEIDENTIFIER NOT NULL,
    IS_ABSENT CHAR(1) NULL DEFAULT('N'),


    CONSTRAINT FK_STUDENT_RATING FOREIGN KEY(STUDENT_ID) REFERENCES Students(ID),
    CONSTRAINT FK_STUDY_LESSONS FOREIGN KEY(STUDY_ID) REFERENCES STUDY_LOAD(ID),
    CONSTRAINT FK_PREPOD_RATING FOREIGN KEY(PREPODS_ID) REFERENCES Prepods(ID) ON DELETE CASCADE,

    CONSTRAINT chkValue CHECK (VAL > 3 AND VAL <= 10),
    CONSTRAINT PK_RATING PRIMARY KEY(ID),

);

