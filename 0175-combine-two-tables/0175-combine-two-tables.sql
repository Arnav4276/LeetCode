# Write your MySQL query statement below
select person.firstname,person.lastname,address.city,address.state from person left outer join address on person.personId=address.personId;