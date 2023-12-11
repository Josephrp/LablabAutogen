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
<<<<<<< HEAD
=======
- sign up and get an api key for Bing! Search

## Zilliz Plugin

This plugin allows users to plug in their existing zilliz account to a multiagent framework using autogen and semantic-kernel.

#### Set Up Zilliz
![Screenshot 2023-12-11 131536](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/d1b42e9c-8fa0-4145-bf60-c975277c6f27)
![Screenshot 2023-12-11 131608](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/5b6b1510-631a-43bb-a647-ea892793e821)

#### Create an Account 

1. Navigate to cloud.zilliz.com
2. sign-up


![Screenshot 2023-12-11 131518](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/5d657875-dc31-4f16-a36f-77f8f2391add)
![Screenshot 2023-12-11 131237](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/4747afcf-8e34-40ae-9cd4-47d70a6fb908)
![Screenshot 2023-12-11 131243](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/d90029c5-869b-444d-adc1-6a997cac0976)

#### Create a Cluster
![Screenshot 2023-12-11 131633](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/01af90cd-22d8-4813-b677-c13714c3b79c)
![Screenshot 2023-12-11 131710](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/918eaa0a-cb67-4835-a302-2666193de29c)
![Screenshot 2023-12-11 131739](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/515855a8-1ff8-407f-9184-972848f8b0af)
![Screenshot 2023-12-11 131744](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/c728e6dc-b02d-476b-8b6a-8f5f7c6f8072)

#### AutoCreate a Pipeline
![Screenshot 2023-12-11 131824](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/0b9de3e2-74c2-428f-960a-bf7f2e901904)
![Screenshot 2023-12-11 131913](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/73550d75-9a6d-4454-a12c-1935584cfc92)
![Screenshot 2023-12-11 132006](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/3fd90763-d64d-4194-bd96-cda996921425)

#### AutoCreate all the Pipeline
![Screenshot 2023-12-11 132023](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/7f5a9910-fad7-45c9-9f18-af9e2b876699)
![Screenshot 2023-12-11 132035](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/69b23ec3-ecb8-494d-bb69-c7665d9e31e8)

#### Use Curl to Upload a Document
![Screenshot 2023-12-11 135943](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/21bdfac4-99bf-413a-9cf8-a2fafeb9c837)
![Screenshot 2023-12-11 140115](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/b89f3c69-258f-4311-962f-10f7f5bc0096)
![Screenshot 2023-12-11 132130](https://github.com/Josephrp/semantic-kernel-v1.0-hackathon/assets/18212928/66a17880-699b-4dde-bc8a-d3e37b04e69e)

#### Use Your Credentials + Existing Zilliz Cloud With Semantic Kernel !

## Get Your Bing! Search API Key

1. visit this weblink [https://aka.ms/bingapisignup](https://portal.azure.com/#create/microsoft.bingsearch)
2. open your portal : [https://portal.azure.com/#create/microsoft.bingsearch](https://portal.azure.com/#create/microsoft.bingsearch) 

# **Check the plugins folder for new Semantic Kernel Plugins**
>>>>>>> 8ff1c563cb0c715e932c267d2fe967f50b8aee0d

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
