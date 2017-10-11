#Instructions

#You should submit one file named labsql.sql with all SQL queries. 
# Make sure that we will be able to run the commands in the file if 
# we invoke from the mysql prompt the following command:

#source labsql.sql

#CREATE DATABASE BigDataLab4;

#SHOW DATABASES;
#USE BigDataLab4;

#SHOW TABLES; 

#select * from boats;
#select * from reserves;
#select * from sailors;

#Use the following format for the queries in the file:

-- ******************** a *******************
# a. Find the name and ages of all sailors
SELECT sname, age
FROM Sailors;


-- ******************** b *******************
# b. Find all sailors with a rating above 7
SELECT sid, sname
FROM Sailors
WHERE rating >= 7;


-- ******************** c *******************
# c. Find the names of sailors who have reserved boat number 103
SELECT sname
FROM Sailors
WHERE sid IN (SELECT sid
				FROM Reserves
                WHERE bid = 103);


-- ******************** d *******************
# d. Find the sids of sailors who have reserved a red boat
SELECT S.sid
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red';


-- ******************** e *******************
# e. Find the names of sailors who have reserved a red boat
SELECT S.sname
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red';


-- ******************** f *******************
# f. Find the names of sailors who have reserved at least one boat
SELECT sname
FROM Sailors
WHERE sid NOT IN (SELECT sid
					FROM Reserves);


-- ******************** g *******************
# g. Find the names of sailors who have reserved a red or a green boat
SELECT S.sname
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red'

UNION

SELECT S.sname
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'green';
# two people have the same name, careful



-- ******************** h *******************
# h. Find the names of sailors who have reserved both a red and a green boat
SELECT S.sname
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid 
	AND R.bid = B.bid 
    AND B.color = 'red'
    AND S.sid IN (SELECT DISTINCT Sa.sid
					FROM Sailors AS Sa JOIN Reserves AS Re JOIN Boats AS Bo
					WHERE Sa.sid = Re.sid AND Re.bid = Bo.bid AND Bo.color = 'green');

-- ******************** i *******************
# i. Find the sids of all sailors who have reserved red boats but not a green boats
SELECT S.sid
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
WHERE S.sid = R.sid 
	AND R.bid = B.bid 
    AND B.color = 'red'
    AND S.sid NOT IN (SELECT DISTINCT Sa.sid
					FROM Sailors AS Sa JOIN Reserves AS Re JOIN Boats AS Bo
					WHERE Sa.sid = Re.sid AND Re.bid = Bo.bid AND Bo.color = 'green');



-- ******************** j *******************
# j. Find the names of sailors who have not reserved boat number 103
SELECT sid
FROM Sailors
WHERE sid NOT IN (SELECT R.sid
					FROM Reserves AS R
                    WHERE R.bid = 103);


-- ******************** k *******************
# k. Find the names of sailors whose rating is better than some sailor called Horatio
SELECT sname
FROM Sailors
WHERE rating > (SELECT MIN(S.rating)
					FROM Sailors AS S
                    WHERE S.sname = 'horatio');


-- ******************** l *******************
# l. Find the names of sailors whose rating is better than all sailors called Horatio
SELECT sname
FROM Sailors
WHERE rating > (SELECT MAX(S.rating)
					FROM Sailors AS S
                    WHERE S.sname = 'horatio');



-- ******************** m *******************
# m. Find the names of sailors who have reserved all boats

SELECT sname 
FROM Sailors
WHERE sid NOT IN(SELECT sid1
					FROM( (SELECT Sa.sid AS sid1, Bo.bid AS bid1
							FROM Sailors AS Sa JOIN Boats AS Bo) AS Sabo
							
                            LEFT JOIN 
							
                            Reserves AS R
							
                            ON Sabo.sid1 = R.sid AND Sabo.bid1 = R.bid
						)
					WHERE sid IS null
				);
					
                    


-- ******************** n *******************
# n. Find the average age of sailors with a rating of 10
SELECT AVG(age)
FROM Sailors
WHERE rating = 10;



-- ******************** o *******************
# o. Find the name and age of the oldest sailor
SELECT sname, age
FROM Sailors
WHERE age = (SELECT MAX(S.age)
				FROM Sailors AS S);
                

-- ******************** p *******************
# p. Find the age of the youngest sailor who is eligible to vote (i.e., is at least 18 
#	 years old) for each rating level with at least two such sailors
SELECT Sa.rating, MIN(Sa.age)
FROM (SELECT *
		FROM Sailors
        WHERE age >= 18) AS Sa
GROUP BY rating
HAVING COUNT(Sa.sid) >= 2;

-- ******************** q *******************
# q. find the sids, snames and bnames of sailors and the boats they have reserved, if any
SELECT S.sid, S.sname, B.bname
FROM Sailors AS S JOIN Reserves AS R JOIN Boats AS B
	ON S.sid = R.sid AND B.bid = R.bid;


-- ******************** THE END *******************

