import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Scheming_IsoPlugin(plugins.SingletonPlugin,toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'scheming_iso19115')


    plugins.implements(plugins.IPackageController, inherit=True)

    # or use plugin 'scheming_nerf_index' debug
    def before_index(self, data_dict):
        """
        Map submission dataset fields to Solr fields
        """
        import json
        # keywords
        # data-format
        # responsible-party
        keywords = []
        _complex = data_dict.get('keywords',[])
        for sub in _complex:
            subs = sub.get('keyword',[])
            if subs:
                if not isinstance(subs,list):
                    subs = json.loads(subs)
            for sub_keyword in subs:
                keywords.append('{}_{}'.format(sub.get('type',''),sub_keyword))
        
        data_dict['keywords'] = str(keywords)

        # replace list of dicts with plain text to prevent Solr errors
        _list = []
        _complex = data_dict.get('data-format',[])
        for sub in _complex:
            _list.append('{}_{}'.format(sub.get('name',''),sub.get('version','')))
        data_dict['data-format'] = str(_list) 

        _list = []
        _complex = data_dict.get('responsible-party',[])
        for sub in _complex:
            subs = sub.get('roles',[])
            if subs:
                if not isinstance(subs,list):
                    subs = json.loads(subs)
            for _sub in subs:
                _list.append('{}_{}'.format(sub.get('name',''),_sub))
        data_dict['responsible-party'] = str(_list) 

        return data_dict