import biothings.hub.dataload.uploader
import os

import requests
import biothings
import config
biothings.config_for_app(config)
import json

MAP_URL = "https://raw.githubusercontent.com/SuLab/outbreak.info-resources/master/outbreak_resources_es_mapping_v3.json"
MAP_VARS = ["@type", "abstract", "date", "author", "citedBy", "curatedBy", "dateModified", "datePublished", "doi", "funding", "identifier", "isBasedOn", "issueNumber", "journalName", "journalNameAbbrev", "keywords", "license", "name", "pmid", "publicationType", "isRelatedTo", "url", "volumeNumber","correction","evaluations","topicCategory"]

# when code is exported, import becomes relative
try:
    from biorxiv.parser import load_annotations as parser_func
except ImportError:
    from .parser import load_annotations as parser_func


class BiorxivUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source="biorxiv"
    name = "biorxiv"
    __metadata__ = {
        "src_meta": {
            "author":{
                "name": "Marco Cano",
                "url": "https://github.com/marcodarko"
            },
            "code":{
                "branch": "master",
                "repo": "https://github.com/outbreak-info/biorxiv.git"
            },
            "url": "https://connect.biorxiv.org/relate/content/181",
            "license": "https://www.biorxiv.org/about-biorxiv"
        }
    }
    idconverter = None

    def load_data(self, data_folder):
        self.logger.info("No data to load from file for biorxiv")
        return parser_func()

    @classmethod
    def get_mapping(klass):
        with open('/opt/home/outbreak/outbreak.api/plugins/biorxiv/mapping.json', 'r') as mapping_file:
            mapping = json.load(mapping_file)
        mapping_dict = { key: mapping[key] for key in MAP_VARS }
        return mapping_dict
