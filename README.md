###  Silk Assignment

In this Python project we:

1. Fetch hosts from Qualys & CrowdStrike APIs  
2. Normalize & deduplicate them  
3. Visualize OS and host age distributions
4. Store results in the MongoDB database

### UI

<img src="https://github.com/user-attachments/assets/fd784bcf-a1a4-483f-823c-e4c1937b9e4b" width="400"/>
<img src="https://github.com/user-attachments/assets/c5c43111-e6a5-4e12-a3c9-001c7ccfdbe1" width="400"/>

### How to run?

```bash
pip install -r requirements.txt
```

```
export SILK_API_KEY={PLACEHOLDER}
```

```
export MONGO_DB_URI={PLACEHOLDER}
```

```
python main.py
```

Now check `/output` folder for results.
