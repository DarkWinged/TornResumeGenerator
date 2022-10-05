# TornResumeGenerator

## Introduction
TRG is a simple tool that quickly formats your work stats and other relevant info collected from the Torn API into a customizable resume.

## Basic Setup
### Step 1
Make a copy of `example_config.json` and rename the copy to `config.json`.

### Step 2
Get your API_KEY from torn.

If you are unsure of how to find your API_KEY follow the link below.
https://mixedanalytics.com/knowledge-base/import-torn-api-data-to-google-sheets/#num1

### Step 3
Replace the `"api_key"` entry in the `config.json` with the API_KEY from Step 2.

### Step 4 (Optional)
You can change the output location by editing the `"output_path"` entry in the `config.json`.

## Usage
Simply load up your favorite terminal and run the `TRG.py` like in the example below.
```$ python3 TRG.py -o"Director_name" -c"Company_name"```

## Requirements
```
python 3.10
requests==2.28.1
argparse==1.4.0
```