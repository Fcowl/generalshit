from git import Repo
import datetime

# Укажите путь к вашему репозиторию ('.' для текущей папки проекта)
repo = Repo('.')
commit_hash = repo.head.commit.committed_datetime
print(f"Полный хэш ревизии: {datetime.datetime.strftime(commit_hash,'%d-%m-%Y')}")
