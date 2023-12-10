---
title: GeneralistAutogenAgent
emoji: 🌍
colorFrom: gray
colorTo: red
sdk: gradio
sdk_version: 4.0.2
app_file: app.py
pinned: false
license: mit
---

**Check the plugins folder for new Semantic Kernel Plugins**

## Before You Install and Use

- sign up and get an api key for open ai
- sign up and set up a project in [zilliz cloud](https://cloud.zilliz.com/)

## Use and Install on the Command Line

```bash
git clone https://github.com/Tonic-AI/EasyAGI
```

```bash
cd LablabAutogen
```

If you're on Windows :

```bash
set PATH=%PATH%
```
then 

```bash
nano app.py
```

edit line 19 "    ```"openai_api_key": "sk-rR5XXXXm",  # OpenAI API Key``` with your key
and edit lines 25-27 
```python    
    "host": "your_milvus_host",
    "port": "your_milvus_port",
    "collection_name": "your_collection_name"
    ```
with your zilliz cloud credentials. 

then press:

```nano
 control + x
```

Write :

```nano
Y
```

to save then type :

```bash
pip install -r requirements.txt
```

and finally :

```bash
python app.py
```
to run.
