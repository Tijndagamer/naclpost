# naclpost database scheme

# Users

+-----------------------+-------------+------+-----+-------------------+-----------------------------+
| Field                 | Type        | Null | Key | Default           | Extra                       |
+-----------------------+-------------+------+-----+-------------------+-----------------------------+
| user_id               | int(11)     | NO   | PRI | NULL              | auto_increment              |
| alias                 | varchar(50) | NO   |     | NULL              |                             |
| public_key            | varchar(50) | NO   |     | NULL              |                             |
| public_key_encryption | varchar(50) | YES  |     | NULL              |                             |
| register_date         | timestamp   | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+-----------------------+-------------+------+-----+-------------------+-----------------------------+

# Posts

+-----------+--------------+------+-----+-------------------+-----------------------------+
| Field     | Type         | Null | Key | Default           | Extra                       |
+-----------+--------------+------+-----+-------------------+-----------------------------+
| post_id   | int(11)      | NO   | PRI | NULL              | auto_increment              |
| user_id   | int(11)      | NO   | MUL | NULL              |                             |
| post_text | varchar(512) | NO   |     | NULL              |                             |
| posttime  | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+-----------+--------------+------+-----+-------------------+-----------------------------+
