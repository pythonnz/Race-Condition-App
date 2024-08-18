DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS properties;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE properties (
  name TEXT UNIQUE PRIMARY KEY NOT NULL,
  value TEXT UNIQUE NOT NULL
);

-- CREATE TABLE problems (
--   id TEXT UNIQUE PRIMARY KEY NOT NULL,
--   name TEXT UNIQUE NOT NULL,
--   is_active BOOLEAN NOT NULL DEFAULT FALSE
-- );
