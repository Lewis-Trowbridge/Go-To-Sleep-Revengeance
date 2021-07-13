CREATE TABLE timezones (
    timezone_id VARCHAR(50) PRIMARY KEY,
    timezone_name VARCHAR(50),
    utc_offset INTEGER,
    dst_offset INTEGER
);

CREATE TABLE area_cache (
    area_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    area_name VARCHAR(50),
    latitude REAL,
    longitude REAL,
    timezone_id VARCHAR(50),
    FOREIGN KEY (timezone_id) REFERENCES timezones(timezone_id)
);

CREATE TABLE server_linked_channels (
    server_id INTEGER,
    channel_id INTEGER,
    PRIMARY KEY (server_id, channel_id)
);

CREATE TABLE sleep_tracker (
    user_id INTEGER PRIMARY KEY,
    area_id INTEGER,
    server_id INTEGER,
    bedtime_offset INTEGER DEFAULT 0,
    aggressive_ping INTEGER DEFAULT 0,
    FOREIGN KEY (area_id) REFERENCES area_cache(area_id),
    FOREIGN KEY (server_id) REFERENCES server_linked_channels(server_id)
);