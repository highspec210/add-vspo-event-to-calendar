# Installation
``` install.sh
pip install -r requirements.txt
touch .env
echo CALENDAR_ID="カレンダーID" >> .env
```

# Commit prefix
|  Prefix       |  Description  |
| ----          | ---- |
|  **feature**  |  機能追加  |
|  **fix**      |  バグ修正、クリティカルなバグ修正なら hotfix  |
|  **docs**     |  ドキュメントのみ修正  |
|  **style**    |  空白、セミコロン、行、コーディングフォーマットなどの修正  |
|  **refactor** |  整理 （リファクタリング等）  |
|  **test**     |  テスト追加や間違っていたテストの修正  |
|  **chore**    |  ビルドツールやライブラリで自動生成されたものをコミットするとき  |