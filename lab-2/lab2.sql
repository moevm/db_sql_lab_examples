create table users
(
    id integer not null primary key AUTO_INCREMENT,
    username varchar(255) not null  unique,
    email varchar(254) not null unique,
    avatar varchar(200),
    isActive bool not null,
    isStaff bool not null,
    role varchar(15)
);

INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (1, 'name_0', 'sample_0_email@gmail.com', null, 1, 0, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (2, 'name_1', 'sample_1_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 0, 0, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (3, 'name_2', 'sample_2_email@gmail.com', null, 1, 0, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (4, 'name_3', 'sample_3_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 0, 0, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (5, 'name_4', 'sample_4_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 0, 1, 'guest');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (6, 'name_5', 'sample_5_email@gmail.com', null, 0, 1, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (7, 'name_6', 'sample_6_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 1, 1, 'guest');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (8, 'name_7', 'sample_7_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 1, 1, 'admin');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (9, 'name_8', 'sample_8_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 1, 1, 'guest');
INSERT INTO users (id, username, email, avatar, isActive, isStaff, role) VALUES (10, 'name_9', 'sample_9_email@gmail.com', 'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png', 0, 1, 'guest');




SELECT * FROM users;

SELECT username, email FROM users WHERE isActive = true AND email LIKE 'sample_0%';
