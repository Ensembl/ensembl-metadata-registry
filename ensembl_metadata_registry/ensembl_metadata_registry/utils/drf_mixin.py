'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2019] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


class SerializerMixin(object):

    def set_related_fields(self, cls, **kwargs):
        many2one = getattr(cls, 'MANY2ONE_SERIALIZER', None)
        one2many = getattr(cls, 'ONE2MANY_SERIALIZER', None)
        entries = []

        if 'context' in kwargs:
            request_obj = kwargs['context']['request']
            query_params = request_obj.query_params
            if 'expand' in query_params:
                entry = query_params['expand']
                entries = entry.split(',') if entry else None
            elif 'expand_all' in query_params and query_params['expand_all'] == 'true':
                if many2one is not None:
                    entries.extend(list(many2one.keys()))
                if one2many is not None:
                    entries.extend(list(one2many.keys()))

            for entry in entries:
                    entry = entry.strip()
                    print('==Entry======' + entry)
                    if many2one is not None and entry in many2one.keys():
                        print('many2one entry from set_related_fields:' + str(entry))
                        self.fields[entry] = many2one[entry](read_only=True)
                    if one2many is not None and entry in one2many.keys():
                        print('one2many entry from set_related_fields: ' + str(entry))
                        self.fields[entry] = one2many[entry](many=True, read_only=True)
