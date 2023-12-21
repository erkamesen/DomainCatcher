# Domain Catcher

Dont miss the perfect domain names. With this script you can catch expired domains and easily buy them.


## Install & Usage

1. *Clone the repository*
```
https://github.com/erkamesen/DomainCatcher.git
```

2. *Change Directory*
```
cd DomainCatcher/
```

3. *Create .env file and set your telegram token like .env.save file*

4. *Set config.yaml file(TLDs & chatIDs for telegram)*
### Local

1. *Create Virtual Environment*
```
python3 -m venv venv
```

2. *Activate*
- *Windows*
```
.\venv\Scripts\activate
```
- *MacOS & Linux*
```
source venv/bin/activate
```

3. *Install dependencies*
```
pip3 install -r requirements.txt
```

4. *Run Script*
```
python main.py
```

### Docker

1. *Build image*
```
docker build . -t <name>
```
2. *Run image*
```
docker run <name>
```


