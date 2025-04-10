-- Insert demo users
INSERT INTO users (email, password_hash, username)
VALUES
('alice@example.com', 'hashedpassword1', 'alice'),
('bob@example.com', 'hashedpassword2', 'bob');

-- Insert folders for user 1 (Alice)
INSERT INTO folders (name, user_id)
VALUES 
('Work', 1),
('Personal', 1);

-- Insert nested folders for Alice
INSERT INTO folders (name, parent_id, user_id)
VALUES 
('Projects', 1, 1),    -- Projects inside Work
('Travel', 2, 1);       -- Travel inside Personal

-- Insert folders for user 2 (Bob)
INSERT INTO folders (name, user_id)
VALUES 
('Research', 2),
('Ideas', 2);

-- Insert links for Alice
INSERT INTO links (url, title, short_summary, long_summary, source_website, image_url, user_id)
VALUES 
('https://example.com/article1', 'How to Code', 'Quick tips on coding.', 'A long-form guide about best practices in programming.', 'example.com', 'https://example.com/image1.jpg', 1),
('https://news.com/post/42', 'World News', 'Today’s headlines.', 'In-depth analysis of global events.', 'news.com', 'https://news.com/image42.jpg', 1);

-- Insert links for Bob
INSERT INTO links (url, title, short_summary, long_summary, source_website, image_url, user_id)
VALUES 
('https://techblog.com/ai', 'AI Trends 2025', 'Emerging AI trends.', 'Detailed exploration of upcoming AI innovations.', 'techblog.com', 'https://techblog.com/ai.jpg', 2);

-- Insert tags (some auto-generated, some manual)
INSERT INTO tags (name, is_auto_generated, user_id)
VALUES 
('coding', TRUE, 1),
('tutorial', TRUE, 1),
('news', TRUE, 1),
('favorites', FALSE, 1),
('ai', TRUE, 2),
('to-read', FALSE, 2);

-- Link-tags relationships
INSERT INTO link_tags (link_id, tag_id)
VALUES 
(1, 1), -- article1 has 'coding'
(1, 2), -- article1 has 'tutorial'
(1, 4), -- article1 has 'favorites'
(2, 3), -- World News has 'news'
(3, 5), -- AI Trends has 'ai'
(3, 6); -- AI Trends has 'to-read'

-- Folder-links relationships
-- Alice's first link is in both 'Work' and 'Projects'
INSERT INTO folder_links (folder_id, link_id)
VALUES
(1, 1),
(3, 1),
(2, 2),
(4, 2), -- World News in Personal > Travel
(5, 3); -- Bob’s link in Research
