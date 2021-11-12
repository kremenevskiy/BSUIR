USE BSUIR_TERM_5;
GO

-- ADD some faculties
INSERT INTO Faculty(ID, NAME)
VALUES
    (NEWID(), 'KSIS'),
    (NEWID(), 'FITU');


-- Insert some groups
INSERT INTO GROUPS(ID, NAME, HEAD_GROUP, FACULTY_ID)
VALUES
    (NEWID(), '123456', NULL, (SELECT ID FROM Faculty WHERE NAME='KSIS'));


-- Insert some students
INSERT INTO Students(ID, LAST_NAME, GROUP_ID)
VALUES
    (NEWID(), 'Ivanov', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Petrov', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Kremenevskiy', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Kukareko', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Ivanchuk', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Voiteshonok', (SELECT ID FROM GROUPS WHERE NAME='123456')),
    (NEWID(), 'Ermakov', (SELECT ID FROM GROUPS WHERE NAME='123456'));


-- Insert Head of group
UPDATE GROUPS
SET HEAD_GROUP = (SELECT ID FROM Students WHERE LAST_NAME='Ivanov')
WHERE NAME='123456';


-- Insert some prepods
INSERT INTO Prepods(ID, LAST_NAME, FACULTY_ID)
VALUES
    (NEWID(), 'Vasechkin', (SELECT ID FROM Faculty WHERE NAME='KSIS')),
    (NEWID(), 'Tesluk', (SELECT ID FROM Faculty WHERE NAME='KSIS')),
    (NEWID(), 'Butoma', (SELECT ID FROM Faculty WHERE NAME='KSIS')),
    (NEWID(), 'Volorova', (SELECT ID FROM Faculty WHERE NAME='KSIS')),
    (NEWID(), 'Petechkin', (SELECT ID FROM Faculty WHERE NAME='FITU'));


-- Insert some subjects
INSERT INTO Subjects(ID, NAME, FACULTY_ID)
VALUES
    (NEWID(), 'Introduction to speciality', (SELECT FACULTY_ID
                                             FROM GROUPS
                                             WHERE NAME='123456')),
    (NEWID(), 'High Math And Analysis', (SELECT FACULTY_ID
                                         FROM GROUPS
                                         WHERE NAME='123456')),
    (NEWID(), 'Python and it applications', (SELECT FACULTY_ID
                                             FROM GROUPS
                                             WHERE NAME='123456')),
    (NEWID(), 'DataScience and Machine Learning', (SELECT FACULTY_ID
                                                   FROM GROUPS
                                                   WHERE NAME='123456'));


-- Insert some type study load
INSERT INTO TYPE_STUDY_LOAD(ID, NAME)
VALUES
    (NEWID(), 'Lection'),
    (NEWID(), 'Practice'),
    (NEWID(), 'Lab');


-- Insert study load amount
INSERT INTO STUDY_LOAD(ID, hours, SUBJECT_ID, Type_STUDY_ID)
VALUES
    ('INTRO',
    2,
    (SELECT ID FROM Subjects WHERE NAME='Introduction to speciality'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection')),

    ('HighMath_LK',
    40,
    (SELECT ID FROM Subjects WHERE NAME='High Math And Analysis'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection')),

    ('HighMath_Practice',
    40,
    (SELECT ID FROM Subjects WHERE NAME='High Math And Analysis'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Practice')),

    ('Python_LK',
    60,
    (SELECT ID FROM Subjects WHERE NAME='Python and it applications'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection')),

    ('Python_Lab',
    60,
    (SELECT ID FROM Subjects WHERE NAME='Python and it applications'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lab')),

    ('DS_ML_LK',
    80,
    (SELECT ID FROM Subjects WHERE NAME='DataScience and Machine Learning'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection')),

    ('DS_ML_Practice',
    80,
    (SELECT ID FROM Subjects WHERE NAME='DataScience and Machine Learning'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Practice')),

    ('DS_ML_Lab',
    80,
    (SELECT ID FROM Subjects WHERE NAME='DataScience and Machine Learning'),
    (SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lab'));


-- Insert some lessons for group and prepod
INSERT INTO LESSONS(GROUP_ID, PREPOD_ID, STUDY_ID)
VALUES
    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Vasechkin'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='Introduction to speciality')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='High Math And Analysis')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='High Math And Analysis')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Practice'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='Python and it applications')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='Python and it applications')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lab'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='DataScience and Machine Learning')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lection'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='DataScience and Machine Learning')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Practice'))),

    ((SELECT ID FROM GROUPS WHERE NAME='123456'),
     (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'),
     (SELECT ID FROM STUDY_LOAD WHERE SUBJECT_ID = (SELECT ID
                                                    FROM Subjects
                                                    WHERE NAME='DataScience and Machine Learning')
                                       AND Type_STUDY_ID=(SELECT ID FROM TYPE_STUDY_LOAD WHERE NAME='Lab')));


-- Insert some marks for students
INSERT INTO RATING(ID, DATE, VAL, STUDENT_ID, STUDY_ID, PREPODS_ID, IS_ABSENT)
VALUES
    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Ivanov'),
    'INTRO', (SELECT ID FROM Prepods WHERE LAST_NAME='Vasechkin'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'HighMath_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'HighMath_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'Python_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'DS_ML_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'DS_ML_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'DS_ML_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kremenevskiy'),
    'DS_ML_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 8, (SELECT ID FROM Students WHERE LAST_NAME='Kukareko'),
    'Python_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 6, (SELECT ID FROM Students WHERE LAST_NAME='Kukareko'),
    'DS_ML_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 9, (SELECT ID FROM Students WHERE LAST_NAME='Kukareko'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Kukareko'),
    'HighMath_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 4, (SELECT ID FROM Students WHERE LAST_NAME='Kukareko'),
    'HighMath_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 9, (SELECT ID FROM Students WHERE LAST_NAME='Ivanchuk'),
    'Python_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 8, (SELECT ID FROM Students WHERE LAST_NAME='Ivanchuk'),
    'DS_ML_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 7, (SELECT ID FROM Students WHERE LAST_NAME='Ivanchuk'),
    'DS_ML_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Ivanchuk'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Ivanchuk'),
    'HighMath_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 7, (SELECT ID FROM Students WHERE LAST_NAME='Voiteshonok'),
    'Python_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 8, (SELECT ID FROM Students WHERE LAST_NAME='Voiteshonok'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 5, (SELECT ID FROM Students WHERE LAST_NAME='Voiteshonok'),
    'HighMath_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 9, (SELECT ID FROM Students WHERE LAST_NAME='Voiteshonok'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Voiteshonok'),
    'HighMath_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 4, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'DS_ML_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'HighMath_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 9, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'DS_ML_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Volorova'), 'N'),

    (NEWID(), GETDATE(), 6, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'Python_Lab', (SELECT ID FROM Prepods WHERE LAST_NAME='Butoma'), 'N'),

    (NEWID(), GETDATE(), 10, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'HighMath_Practice', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N'),

    (NEWID(), GETDATE(), 8, (SELECT ID FROM Students WHERE LAST_NAME='Ermakov'),
    'HighMath_LK', (SELECT ID FROM Prepods WHERE LAST_NAME='Tesluk'), 'N');




-- Adding file system to database
ALTER DATABASE BSUIR_TERM_5
ADD FILEGROUP fileGroup
GO

ALTER DATABASE BSUIR_TERM_5
ADD FILE
(
	NAME = testfile,
	FILENAME = '/Users/kremenevskiy/testfile.ndf',
	SIZE = 5MB,
    MAXSIZE = 100MB,
    FILEGROWTH = 5MB
)
TO FILEGROUP fileGroup
GO



-- deleting all rows from all
DELETE FROM Faculty;
DELETE FROM TYPE_STUDY_LOAD;
DELETE FROM Subjects;
DELETE FROM STUDY_LOAD;
DELETE FROM Prepods;
DELETE FROM GROUPS;
DELETE FROM LESSONS;
DELETE FROM Students;
DELETE FROM RATING;

-- check if all tables deleted
SELECT COUNT(ID) as count
FROM Faculty
UNION
SELECT COUNT(ID) as count
FROM TYPE_STUDY_LOAD
UNION
SELECT COUNT(ID) as count
FROM Subjects
UNION
SELECT COUNT(ID) as count
FROM STUDY_LOAD
UNION
SELECT COUNT(ID) as count
FROM Prepods
UNION
SELECT COUNT(ID) as count
FROM GROUPS
UNION
SELECT COUNT(GROUP_ID) as count
FROM LESSONS
UNION
SELECT COUNT(ID) as count
FROM Students
UNION
SELECT COUNT(ID) as count
FROM RATING;


-- useful selectd to see information :)
SELECT *
FROM Faculty;

SELECT *
FROM TYPE_STUDY_LOAD;

SELECT *
FROM Subjects;

SELECT *
FROM STUDY_LOAD;

SELECT *
FROM Prepods;

SELECT *
FROM GROUPS;

SELECT *
FROM LESSONS;

SELECT *
FROM Students;

SELECT *
FROM RATING;