###  Silk Assignment

In this Python project we:

1. Fetch hosts from Qualys & CrowdStrike APIs  
2. Normalize & deduplicate them  
3. Visualize OS and host age distributions  

### How to run?

```bash
pip install -r requirements.txt
```

```
export SILK_API_KEY={PLACEHOLDER}
export MONGO_DB_URI={PLACEHOLDER}
```

```
python main.py
```

Now check `/output` folder for results.