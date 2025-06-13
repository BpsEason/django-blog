CREATE DATABASE blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 文章表結構（由 Django 自動生成，此處為參考）
CREATE TABLE blog_post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    category VARCHAR(50) NOT NULL DEFAULT 'Uncategorized'
);