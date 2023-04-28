# Overview
ぶいすぽっ！公式サイトの期間限定受注生産商品の期間をGoogleカレンダーに追加するやつ

# How to use
- ```python src/AllEvents.py```

  歴代すべての商品を追加する

- ```python src/NewEvents.py```

  実行時点でまだ期間が開始していない商品を追加する

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