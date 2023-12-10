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

## Use and Install

on the command line :

```bash
git clone https://github.com/Tonic-AI/EasyAGI
```

```bash
cd EasyAGI
```

If you're on Windows run the following command and edit the files below using notepad or VSCode and save them accordingly.

```bash
set PATH=%PATH%
```
then edit the OAI_CONFIG_LIST file or on the command line:

```bash
nano OAI_CONFIG_LIST.json
```

enter your keys into the space provided, eg: 

```json
   {
        "model": "gpt-4",
        "api_key": "<your OpenAI API key here>"
    },
    {
        "model": "gpt-4",
        "api_key": "<your Azure OpenAI API key here>",
        "api_base": "<your Azure OpenAI API base here>",
        "api_type": "azure",
        "api_version": "2023-07-01-preview"
    }
```
with your keys or Azure OpenAI deployments

on the command line , press:

```nano
 control + x
```

Write :

```nano
Y
```

to save then run

```bash
nano app.py
```

and edit lines 25-27 of app.py 

```python    
    "host": "your_milvus_host",
    "port": "your_milvus_port",
    "collection_name": "your_collection_name"
```

with your zilliz cloud credentials. 

and line 15 with your Bing! api key then save. 

or if you're on the command line press:

```nano
 control + x
```
Write :

```nano
y
```

to save.

then type the following in your command line

```bash
pip install -r requirements.txt
```

and finally :

```bash
python app.py
```
to run. or install and run the application inside your compiler - like VS Code. 
