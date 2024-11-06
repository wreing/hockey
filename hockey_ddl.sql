

create table game (
  dt date,
  home_team varchar(255),
  home_score int,
  away_team carchar(255),
  away_score int,
  overtime boolean,
  type varchar(2)
);

create table team (
  id int primary key,
  name varchar(255)
);


