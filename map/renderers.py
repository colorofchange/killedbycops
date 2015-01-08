from django_medusa.renderers import StaticSiteRenderer

class MapRenderer(StaticSiteRenderer):
    def get_paths(self):
        return ["/",]
        
renderers = [MapRenderer, ]