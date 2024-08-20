from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from creation.models import Post

@registry.register_document
class PostDocument(Document):
    class Index:
        name="Post"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = Post
        fields = ['title','content','author']