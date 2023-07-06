# Graph Language Models

![Cross platform build status](https://github.com/DS4SD/deepsearch-glm/actions/workflows/cmake.yml/badge.svg)
[![PyPI version](https://img.shields.io/pypi/v/deepsearch-glm)](https://pypi.org/project/deepsearch-glm/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/deepsearch-glm)](https://pypi.org/project/deepsearch-glm/)
[![License MIT](https://img.shields.io/github/license/ds4sd/deepsearch-glm)](https://opensource.org/licenses/MIT)

## Install

### CXX compilation

To compile from scratch, simply run the following command in the `deepsearch-glm` root folder, 

```sh
cmake -B ./build; cd build; make install -j
```

### Python installation

To install all the dependent python packages and get the python bindings, simply execute,

```sh
poetry install
```

## Python Interface

To use the python interface, first make sure all dependencies are installed. We use [poetry](https://python-poetry.org/docs/) for that,

```sh
poetry install
```

To run the examples, simply do execute the scripts as `poetry run python <script> <input>`. Examples are,

1. Doing NLP on a single document
```sh
poetry run python3 ./deepsearch_glm/nlp_doc.py -m run-doc -i ../../Articles-v2/2302.05420.json --vpage 10
```
2. Creating a GLM from a single document
```sh
poetry run python ./deepsearch_glm/glm_doc.py --pdf ./data/documents/reports/2022-ibm-annual-report.pdf
```
3. Creating a GLM from documents
```sh
poetry run python ./deepsearch_glm/glm_from_query.py --index esg-report --query "net zero" --force True
```
4. Using a GLM for Q&A on a document
```sh
poetry run python ./deepsearch_glm/glm_docqa.py --pdf ./data/documents/reports/2022-ibm-annual-report.pdf
```

## CXX interface

If you like to be bare-bones, you can also use the executables for NLP and GLM's directly. In general, we
follow a simple scheme of the form

```sh
./nlp.exe -m <mode> -c <JSON-config file>
./glm.exe -m <mode> -c <JSON-config file>
```

In both cases, the modes can be queried directly via the `-h` or `--help`

```sh
./nlp.exe -h
./glm.exe -h
```

and the configuration files can be generated,

```sh
./nlp.exe -m create-configs
./glm.exe -m create-configs
```

### Natural Language Processing (NLP)

After you have generated the configuration files (see above), you can

1. train simple NLP models
```sh
./nlp.exe -m train -c nlp_train_config.json
```
2. leverage pre-trained models
```sh
./nlp.exe -m predict -c nlp_predict.example.json
```

### Graph Language Models (GLM)

1. create a GLM
```sh
./glm.exe -m create -c glm_config_create.json
```
2. explore interactively the GLM
```sh
./glm.exe -m explore -c glm_config_create.json
```

