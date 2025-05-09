INSERT IGNORE INTO videos (
    name,
    category,
    video_link,
    link_type,
    upload_date,
    comment,
    date_of_recording,
    channel_id,
    is_deleted
) VALUES
('Testvideo 1', 'reports', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 1, false),
('Testvideo 2', 'highlights', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 1, false),
('Testvideo 3', 'sparbuilding', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 1, false),
('Testvideo 4', 'match', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 1, false),
('Testvideo 5', 'song', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 2, false),
('Testvideo 6', 'podcast', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 3, false),
('Testvideo 7', 'awards', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 4, false),
('Testvideo 8', 'training', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 5, false),
('Testvideo 9', 'other', 'https://youtu.be/f27SC622NvE', 'youtube', '2028-03-10T23:00:00', 'comment', NULL, 6, false);
