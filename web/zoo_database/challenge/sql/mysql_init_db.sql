
-- mysql -uroot -proot < $file

use sample;

CREATE TABLE animals (
  id int NOT NULL,
  name varchar(10),
  password varchar(100),
  PRIMARY KEY (id)
);

INSERT INTO
  animals(id, name, password)
VALUES
  (0, 'mysql', 'mysql_password'),
  (1, 'Monkey', 'kucss{Monk3y_1nject}'),
  (2, 'Hippo', 'smelly'),
  (3, 'Fish', 'wotor'),
  (4, 'Lion', 'rawr xD')
;
