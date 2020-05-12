import biothings.hub.dataload.uploader
import os

import biothings
import config
biothings.config_for_app(config)


# when code is exported, import becomes relative
try:
    from biorxiv.parser import load_annotations as parser_func
except ImportError:
    from .parser import load_annotations as parser_func


class BiorxivUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source="biorxiv"
    name = "biorxiv"
    __metadata__ = {"src_meta": {}}
    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("No data to load from file for biorxiv")
        return parser_func()

    @classmethod
    def get_mapping(klass):
        return {
            "@type": {
                "normalizer": "keyword_lowercase_normalizer",
                "type": "keyword"
            },
            'fields': {
                'type': 'text'
            },
            'abstract': {
                'type': 'text'
            },
            'pmid': {
                'type': 'integer'
            },
            'author': {
                'properties': {
                    'name': {
                        'type': 'text'
                    },
                    'givenName': {
                        'type': 'text'
                    },
                    'familyName': {
                        'type': 'text'
                    },
                    'affiliation': {
                        'properties': {
                            'name': {
                                'type': 'text'
                            }
                        }
                    }
                }
            },
            "isBasedOn": {
                "properties": {
                    "@type": {
                        "normalizer": "keyword_lowercase_normalizer",
                        "type": "keyword"
                    },
                    "identifier": {
                        "type": "text"
                    },
                    "name": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "datePublished": {
                        "type": "text"
                    }
                }
            },
            "relatedTo": {
                "properties": {
                    "@type": {
                        "normalizer": "keyword_lowercase_normalizer",
                        "type": "keyword"
                    },
                    "identifier": {
                        "type": "text"
                    },
                    "pmid": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "citation": {
                        "type": "text"
                    }
                }
            },
            'funding': {
                'properties': {
                    'funder': {
                        'properties': {
                            'name': {
                                'type': 'text'
                            }
                        }
                    },
                    'identifier': {
                        'type': 'text'
                    }
                }
            },
            'license': {
                'type': 'text'
            },
            'keywords': {
                'normalizer': 'keyword_lowercase_normalizer',
                'type': 'keyword',
                        'copy_to': ['all']
            },
            'publicationType': {
                'normalizer': 'keyword_lowercase_normalizer',
                'type': 'keyword',
                        'copy_to': ['all']
            },
            'name': {
                'type': 'text'
            },
            'journalName': {
                'type': 'text'
            },
            'identifier': {
                'type': 'text'
            },
            'doi': {
                'type': 'text'
            },
            'datePublished': {
                'type': 'keyword'
            },
            'dateModified': {
                'type': 'keyword'
            },
            'issueNumber': {
                'type': 'text'
            },
            'volumeNumber': {
                'type': 'text'
            },
            "curatedBy": {
                "properties": {
                    "@type": {
                        "normalizer": "keyword_lowercase_normalizer",
                        "type": "keyword"
                    },
                    "name": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "versionDate": {
                        "normalizer": "keyword_lowercase_normalizer",
                        "type": "keyword"
                    },
                }
            },
        }
