#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
笔记管理模块
提供笔记的增删改查功能
"""

import os
import json
import argparse
from datetime import datetime


class NoteManager:
    """笔记管理器"""
    
    def __init__(self, config_path='config/settings.json'):
        self.config_path = config_path
        self.config = self.load_config()
        self.notes_dir = self.config.get('notes_dir', 'docs')
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'notes_dir': 'docs', 'theme': 'dark'}
    
    def get_all_notes(self):
        """获取所有笔记文件"""
        notes = []
        if not os.path.exists(self.notes_dir):
            return notes
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(self.notes_dir, filename)
                stats = os.stat(filepath)
                notes.append({
                    'name': filename,
                    'path': filepath,
                    'size': stats.st_size,
                    'modified': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
                })
        return notes
    
    def create_note(self, title, content=''):
        """创建新笔记"""
        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(self.notes_dir, filename)
        
        if os.path.exists(filepath):
            raise FileExistsError(f"笔记 '{title}' 已存在")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            if content:
                f.write(content)
            else:
                f.write(f"# {title}\n\n")
        
        return filepath
    
    def read_note(self, title):
        """读取笔记内容"""
        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(self.notes_dir, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"笔记 '{title}' 不存在")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def update_note(self, title, content):
        """更新笔记内容"""
        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(self.notes_dir, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"笔记 '{title}' 不存在")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def delete_note(self, title):
        """删除笔记"""
        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(self.notes_dir, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"笔记 '{title}' 不存在")
        
        os.remove(filepath)
        return True


def main():
    """命令行接口"""
    parser = argparse.ArgumentParser(description='笔记管理工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # list 命令
    subparsers.add_parser('list', help='列出所有笔记')
    
    # create 命令
    create_parser = subparsers.add_parser('create', help='创建笔记')
    create_parser.add_argument('title', help='笔记标题')
    create_parser.add_argument('-c', '--content', help='笔记内容')
    
    # read 命令
    read_parser = subparsers.add_parser('read', help='读取笔记')
    read_parser.add_argument('title', help='笔记标题')
    
    # update 命令
    update_parser = subparsers.add_parser('update', help='更新笔记')
    update_parser.add_argument('title', help='笔记标题')
    update_parser.add_argument('content', help='新内容')
    
    # delete 命令
    delete_parser = subparsers.add_parser('delete', help='删除笔记')
    delete_parser.add_argument('title', help='笔记标题')
    
    args = parser.parse_args()
    
    manager = NoteManager()
    
    if args.command == 'list':
        notes = manager.get_all_notes()
        print(f"共找到 {len(notes)} 篇笔记：")
        for note in notes:
            print(f"- {note['name']} ({note['size']} bytes, {note['modified']})")
    
    elif args.command == 'create':
        try:
            path = manager.create_note(args.title, args.content)
            print(f"笔记已创建：{path}")
        except Exception as e:
            print(f"创建失败：{e}")
    
    elif args.command == 'read':
        try:
            content = manager.read_note(args.title)
            print(content)
        except Exception as e:
            print(f"读取失败：{e}")
    
    elif args.command == 'update':
        try:
            path = manager.update_note(args.title, args.content)
            print(f"笔记已更新：{path}")
        except Exception as e:
            print(f"更新失败：{e}")
    
    elif args.command == 'delete':
        try:
            manager.delete_note(args.title)
            print(f"笔记 '{args.title}' 已删除")
        except Exception as e:
            print(f"删除失败：{e}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
