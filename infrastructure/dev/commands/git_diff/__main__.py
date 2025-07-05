"""
Используйте команду:
python -m infrastructure.dev.commands.git_diff
"""

from .prompt_commit_msg_maker import save_git_diff

if __name__ == '__main__':
    save_git_diff()

