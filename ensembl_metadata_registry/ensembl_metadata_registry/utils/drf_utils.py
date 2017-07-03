class DrfUtils(object):

    @classmethod
    def get_related_entities(cls, model, cardinality=None):
        entities = []
        many2one = getattr(model, 'MANY2ONE_RELATED', None)
        one2many = getattr(model, 'ONE2MANY_RELATED', None)

        if(cardinality is None):
            if many2one is not None:
                entities.extend(list(many2one.values()))
            if one2many is not None:
                entities.extend(list(one2many.values()))
        elif (cardinality == 'many2one' or cardinality == 'many2many'):
            if many2one is not None:
                entities.extend(list(many2one.values()))
        elif (cardinality == 'one2many'):
            if one2many is not None:
                entities.extend(list(one2many.values()))
        return entities
