Запуск:

```bash
cp example.env .env
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python ./src/main_models_1_2.py
python ./src/main_models_4_5.py
python ./src/main_models_6_7.py
```

Миксин AsyncAttrs в Base классе показывает, как использовать отложенный доступ к связанным полям.
Можно также использовать опцию `lazy="joined"` в relationship, чтобы избежать отдельных запросов и сразу через join загружать связанные записи.