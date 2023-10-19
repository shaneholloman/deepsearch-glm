
import os
import json

from deepsearch_glm.nlp_utils import list_nlp_model_configs, init_nlp_model, \
    extract_references_from_doc
from deepsearch_glm.utils.load_pretrained_models import load_pretrained_nlp_models

def test_01_load_nlp_models():
    models = load_pretrained_nlp_models()
    print(f"models: {models}")

    assert "language" in models
    assert "semantic" in models
    assert "name" in models
    assert "reference" in models

def check_dimensions(item):

    assert "headers" in item
    assert "data" in item    

    headers = item["headers"]
    for row in item["data"]:
        assert len(row)==len(headers)

def test_02A_run_nlp_models_on_text():

    model = init_nlp_model("sentence;language;term")
    res = model.apply_on_text("FeSe is a material.")
    print(res.keys())
    
    for label in ["text", "properties", "instances", "relations"]:
        assert label in res

    check_dimensions(res["properties"])
    check_dimensions(res["instances"])
    check_dimensions(res["relations"])        
        
def test_02B_run_nlp_models_on_text():

    filters = ["properties"]
    
    model = init_nlp_model("sentence;language;term", filters)
    res = model.apply_on_text("FeSe is a material.")
    print(res.keys())
    
    for label in ["text", "properties"]:
        assert label in res

    for label in ["instances", "relations"]:
        assert label not in res        

def test_03A_run_nlp_models_on_document():

    with open("./tests/data/docs/1806.02284.json") as fr:
        doc = json.load(fr)
    
    model = init_nlp_model("sentence;language;term;reference")
    res = model.apply_on_doc(doc)
    print(res.keys())

    for label in ["description", "body", "meta",
                  "page-elements", "texts", "tables", "figures",
                  "properties", "instances", "relations"]:
        assert label in res

    check_dimensions(res["properties"])
    check_dimensions(res["instances"])
    check_dimensions(res["relations"])
    
def test_03B_run_nlp_models_on_document():

    with open("./tests/data/docs/1806.02284.json") as fr:
        doc = json.load(fr)

    filters = ["properties"]
        
    model = init_nlp_model("sentence;language;term;reference", filters)
    res = model.apply_on_doc(doc)
    print(res.keys())

    for label in ["dloc", "applied-models",
                  "description", "body", "meta",
                  "page-elements", "texts", "tables", "figures",
                  "properties"]: 
        assert label in res

    for label in ["instances", "relations"]:
        assert label not in res
                  
    check_dimensions(res["properties"])

def test_03C_run_nlp_models_on_document():

    model = init_nlp_model("language;semantic;sentence;term;verb;conn;geoloc;reference")

    source = "./tests/data/docs/1806.02284.json"
    target = "./tests/data/docs/1806.02284.nlp.json"
    
    if False: # generate the test-data
        with open(source) as fr:
            doc = json.load(fr)

        res = model.apply_on_doc(doc)
        extract_references_from_doc(res)
        
        fw = open(target, "w")
        fw.write(json.dumps(res)+"\n")            
        fw.close()
        
        assert True
        
    else:
        with open(source) as fr:
            sdoc = json.load(fr)

        res = model.apply_on_text(sdoc)        

        with open(target) as fr:
            tdoc = json.load(fr)
        
        assert res==tdoc
    
def test_04A_terms():

    model = init_nlp_model("language;semantic;sentence;term;verb;conn;geoloc")

    source = "./tests/data/texts/terms.jsonl"
    target = "./tests/data/texts/terms.nlp.jsonl"
    
    if False: # generate the test-data
        with open(source) as fr:
            lines = fr.readlines()

        fw = open(target, "w")
    
        for line in lines:
            data = json.loads(line)
            res = model.apply_on_text(data["text"])

            fw.write(json.dumps(res)+"\n")
            
        fw.close()

    else:
        with open(target) as fr:
            lines = fr.readlines()
            
        for line in lines:
            data = json.loads(line)
            res = model.apply_on_text(data["text"])

            assert res==data
       
    assert True
    
def test_04B_references():

    model = init_nlp_model("reference")

    source = "./tests/data/texts/references.jsonl"
    target = "./tests/data/texts/references.nlp.jsonl"
    
    if False: # generate the test-data
        
        with open(source) as fr:
            lines = fr.readlines()

        fw = open(target, "w")
    
        for line in lines:
            data = json.loads(line)
            res = model.apply_on_text(data["text"])
            
            fw.write(json.dumps(res)+"\n")
                
        fw.close()
        assert True
        
    else:
        with open(target) as fr:
            lines = fr.readlines()
            
        for line in lines:
            data = json.loads(line)
            res = model.apply_on_text(data["text"])

            assert res==data
    

