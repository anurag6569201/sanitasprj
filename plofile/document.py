from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from home.models import recentUpdates

@registry.register_document
class UserDocument(Document):
    class Index:
        name="updates_index"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = recentUpdates
        fields = ['title','content']