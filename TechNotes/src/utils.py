#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具函数模块
提供常用的辅助功能
"""

import os
import re
from datetime import datetime


def format_file_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"


def get_file_extension(filename):
    """获取文件扩展名"""
    return os.path.splitext(filename)[1][1:].lower()


def is_markdown_file(filename):
    """判断是否为Markdown文件"""
    return get_file_extension(filename) == 'md'


def sanitize_filename(filename):
    """清理文件名中的非法字符"""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def get_current_time():
    """获取当前时间字符串"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def count_lines(filepath):
    """统计文件行数"""
    if not os.path.exists(filepath):
        return 0
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def count_words(filepath):
    """统计文件字数（中文）"""
    if not os.path.exists(filepath):
        return 0
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        # 统计中文字符
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
        # 统计英文单词
        english_words = len(re.findall(r'[a-zA-Z]+', content))
        return chinese_chars + english_words


def ensure_directory(directory):
    """确保目录存在"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False


def generate_id():
    """生成唯一ID"""
    return datetime.now().strftime('%Y%m%d%H%M%S')


def truncate_text(text, max_length=100):
    """截断文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + '...'
