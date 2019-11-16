/*
 * This SQL script creates the users and posts tables, if they don't already exist.
 */


CREATE TABLE IF NOT EXISTS users(
    user_id INT(11) NOT NULL auto_increment,
    alias VARCHAR(50) NOT NULL,
    public_key VARCHAR(50) NOT NULL,
    public_key_encryption VARCHAR(50),
    register_date TIMESTAMP,
    PRIMARY KEY (user_id)
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS posts (
    post_id INT(11) NOT NULL auto_increment,
    user_id INT(11) NOT NULL,
    post_text VARCHAR(512) NOT NULL,
    posttime TIMESTAMP,
    PRIMARY KEY (post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8;
